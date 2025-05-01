import os

import pytest

from cryptixd_client.modules.CryptixdStream import CryptixdStream

CRYPTIXD_TEST_HOST = os.getenv("CRYPTIXD_TEST_HOST") or "127.0.0.1"
CRYPTIXD_TEST_PORT = os.getenv("CRYPTIXD_TEST_PORT") or 16110


@pytest.mark.asyncio
async def test_init():
    cryptixd_thread = CryptixdStream(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)

    await cryptixd_thread.send("getBlockDagInfoRequest", id=1234)
    response = await cryptixd_thread.read(1234)

    assert response.get("getBlockDagInfoResponse").get("networkName") == "cryptix-mainnet"
