# encoding: utf-8
import asyncio
import logging

import grpc
from google.protobuf import json_format

from ..cryptix_grpc import messages_pb2_grpc
from ..cryptix_grpc.messages_pb2 import CryptixdRequest

MAX_MESSAGE_LENGTH = 1024 * 1024 * 1024  # 1GB

_logger = logging.getLogger(__name__)


# pipenv run python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/rpc.proto ./protos/messages.proto ./protos/p2p.proto


class CryptixdStream(object):
    def __init__(self, cryptixd_host: str, cryptixd_port: int = 16110):
        self.__cryptixd_host = cryptixd_host
        self.__cryptixd_port = cryptixd_port

        self.__command_queue = asyncio.queues.Queue()
        self.__read_queue = {}

        self.__channel = grpc.aio.insecure_channel(
            f"{cryptixd_host}:{cryptixd_port}",
            compression=grpc.Compression.Gzip,
            options=[
                ("cryptix_grpc.max_send_message_length", MAX_MESSAGE_LENGTH),
                ("cryptix_grpc.max_receive_message_length", MAX_MESSAGE_LENGTH),
            ],
        )

        self.__stub = messages_pb2_grpc.RPCStub(self.__channel)
        asyncio.get_running_loop().create_task(self.__loop())

        self.__callback_functions = {}

    async def read(self, msg_id: int):
        try:
            return await self.__read_queue[msg_id].get()
        finally:
            self.__read_queue.pop(msg_id)

    async def send(self, command: str, params: dict = None, id: int | None = None):
        self.__read_queue[id] = asyncio.queues.Queue()
        await self.__command_queue.put((id, command, params))

    async def __loop(self):
        async for resp in self.__stub.MessageStream(self.yield_cmd()):
            msg = json_format.MessageToDict(resp, including_default_value_fields=True)
            if resp.id in self.__read_queue:
                await self.__read_queue[resp.id].put(msg)

            _logger.debug(f"recv: {msg}")
            for callback in self.__callback_functions.get(next(iter(msg)), []):
                await callback(msg)

    async def yield_cmd(self):
        while True:
            (id, cmd, params) = await self.__command_queue.get()
            _logger.debug(f"send: {cmd}")
            msg = CryptixdRequest()
            msg.id = id
            msg2 = getattr(msg, cmd)
            payload = params

            if payload:
                if isinstance(payload, dict):
                    json_format.ParseDict(payload, msg2)
                if isinstance(payload, str):
                    json_format.Parse(payload, msg2)

            msg2.SetInParent()
            yield msg

    async def register_callback(self, response, callback):
        self.__callback_functions[response] = self.__callback_functions.get(
            response, []
        ) + [callback]
