import asyncio
import logging
import os

import pytest

from cryptixd_client import CryptixdClient

CRYPTIXD_TEST_HOST = os.getenv("CRYPTIXD_TEST_HOST") or "127.0.0.1"
CRYPTIXD_TEST_PORT = os.getenv("CRYPTIXD_TEST_PORT") or 16110

logging.basicConfig(
    format="%(asctime)s::%(levelname)s::%(name)s::%(message)s",
    level=logging.DEBUG,
    handlers=[logging.StreamHandler()],
)


@pytest.mark.asyncio
async def test_increasing_id():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    await cryptixd_client.get_block_dag_info()
    await cryptixd_client.get_block_dag_info()
    await cryptixd_client.get_block_dag_info()
    await cryptixd_client.get_block_dag_info()
    await cryptixd_client.get_block_dag_info()
    await asyncio.sleep(0.5)
    assert cryptixd_client.next_id == 7


@pytest.mark.asyncio
async def test_get_block_dag_info():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    resp = await cryptixd_client.get_block_dag_info()

    assert resp.get("getBlockDagInfoResponse") is not None
    await asyncio.sleep(0.5)


@pytest.mark.asyncio
async def test_get_block_dag_info_with_notify_spam():
    pass


@pytest.mark.asyncio
async def test_get_current_network():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    resp = await cryptixd_client.get_current_network()

    assert resp.get("getCurrentNetworkResponse") is not None
    await asyncio.sleep(0.5)


@pytest.mark.asyncio
async def test_submit_block():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    resp = await cryptixd_client.submit_block({"verboseData": {}}, False)

    assert resp.get("submitBlockResponse") is not None
    await asyncio.sleep(0.5)


@pytest.mark.asyncio
async def test_get_block_template():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    resp = await cryptixd_client.get_block_template(
        "cryptixd_client:qqkqkzjvr7zwxxmjxjkmxxdwju9kjs6e9u82uh59z07vgaks6gg62v8707g73",
        "",
    )

    assert resp.get("getBlockTemplateResponse") is not None
    await asyncio.sleep(0.5)


@pytest.mark.asyncio
async def test_get_peer_addresses():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    resp = await cryptixd_client.get_peer_addresses()

    assert resp.get("getPeerAddressesResponse") is not None
    await asyncio.sleep(0.5)


# @pytest.mark.asyncio
# async def test_get_sink():
#     cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
#     resp = await cryptixd_client.get_sink()
#
#     assert resp.get("getSinkResponse") is not None
#     await asyncio.sleep(.5)


@pytest.mark.asyncio
async def test_get_mempool_entry():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    resp = await cryptixd_client.get_mempool_entry("123", False, False)

    assert resp.get("getMempoolEntryResponse") is not None
    await asyncio.sleep(0.5)


@pytest.mark.asyncio
async def test_get_mempool_entries():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    resp = await cryptixd_client.get_mempool_entries(False, False)

    assert resp.get("getMempoolEntriesResponse") is not None
    await asyncio.sleep(0.5)


@pytest.mark.asyncio
async def test_get_connected_peer_info():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    resp = await cryptixd_client.get_connected_peer_info()

    assert resp.get("getConnectedPeerInfoResponse") is not None
    await asyncio.sleep(0.5)


@pytest.mark.asyncio
async def test_add_peer():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    resp = await cryptixd_client.add_peer("127.0.0.2", is_permanent=False)

    assert resp.get("addPeerResponse") is not None
    await asyncio.sleep(0.5)


@pytest.mark.asyncio
async def test_submit_transaction():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    resp = await cryptixd_client.submit_transaction({"version": 1}, allow_orphan=False)

    assert resp.get("submitTransactionResponse") is not None
    await asyncio.sleep(0.5)


@pytest.mark.asyncio
async def test_submit_transaction_replacement():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    resp = await cryptixd_client.submit_transaction_replacement({"version": 1})

    assert resp.get("submitTransactionReplacementResponse") is not None
    await asyncio.sleep(0.5)


@pytest.mark.asyncio
async def test_get_block():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    resp = await cryptixd_client.get_block("123", include_transactions=True)

    assert resp.get("getBlockResponse") is not None
    await asyncio.sleep(0.5)


@pytest.mark.asyncio
async def test_get_block_color():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    resp = await cryptixd_client.get_block_color(
        "5698d2bdb83f674cd2e7f4cad52b3bd26326083ddb3ef4521c43151e25862fc4"
    )

    assert resp.get("getCurrentBlockColorResponse") is not None
    await asyncio.sleep(0.5)


@pytest.mark.asyncio
async def test_get_subnetwork():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    resp = await cryptixd_client.get_subnetwork("00000000000001")

    assert resp.get("getSubnetworkResponse") is not None
    await asyncio.sleep(0.5)


@pytest.mark.asyncio
async def test_get_virtual_chain_from_block():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    resp = await cryptixd_client.get_virtual_chain_from_block("00000000000001", False)

    assert resp.get("getVirtualChainFromBlockResponse") is not None
    await asyncio.sleep(0.5)


@pytest.mark.asyncio
async def test_get_blocks():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    resp = await cryptixd_client.get_blocks("00000000000001", False, False)

    assert resp.get("getBlocksResponse") is not None
    await asyncio.sleep(0.5)


@pytest.mark.asyncio
async def test_get_block_count():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    resp = await cryptixd_client.get_block_count()

    assert resp.get("getBlockCountResponse") is not None
    await asyncio.sleep(0.5)


@pytest.mark.asyncio
async def test_get_headers():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    resp = await cryptixd_client.get_headers("1", 1, False)

    assert resp.get("getHeadersResponse") is not None
    await asyncio.sleep(0.5)


@pytest.mark.asyncio
async def test_get_balance_by_address():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    resp = await cryptixd_client.get_balance_by_address(
        "cryptixd_client:qqkqkzjvr7zwxxmjxjkmxxdwju9kjs6e9u82uh59z07vgaks6gg62v8707g73"
    )

    assert resp.get("getBalanceByAddressResponse") is not None
    await asyncio.sleep(0.5)


@pytest.mark.asyncio
async def test_get_utxos_by_addresses():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    resp = await cryptixd_client.get_utxos_by_addresses(
        ["cryptixd_client:qqkqkzjvr7zwxxmjxjkmxxdwju9kjs6e9u82uh59z07vgaks6gg62v8707g73"]
    )

    assert resp.get("getUtxosByAddressesResponse") is not None
    await asyncio.sleep(0.5)


@pytest.mark.asyncio
async def test_get_balances_by_addresses():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    resp = await cryptixd_client.get_balances_by_addresses(
        ["cryptixd_client:qqkqkzjvr7zwxxmjxjkmxxdwju9kjs6e9u82uh59z07vgaks6gg62v8707g73"]
    )

    assert resp.get("getBalancesByAddressesResponse") is not None
    await asyncio.sleep(0.5)


@pytest.mark.asyncio
async def test_get_sink_blue_score():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    resp = await cryptixd_client.get_sink_blue_score()

    assert resp.get("getSinkBlueScoreResponse", {}).get("blueScore") is not None
    await asyncio.sleep(0.5)


@pytest.mark.asyncio
async def test_ban():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    resp = await cryptixd_client.ban("127.0.0.2")

    assert resp.get("banResponse") is not None
    await asyncio.sleep(0.5)


@pytest.mark.asyncio
async def test_get_info():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    resp = await cryptixd_client.get_info()

    assert resp.get("getInfoResponse", {}).get("p2pId") is not None
    await asyncio.sleep(0.5)


@pytest.mark.asyncio
async def test_get_coin_supply():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    resp = await cryptixd_client.get_coin_supply()

    assert resp.get("getCoinSupplyResponse").get("circulatingSompi") is not None
    await asyncio.sleep(0.5)


@pytest.mark.asyncio
async def test_ping():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    resp = await cryptixd_client.ping()

    assert resp.get("pingResponse") is not None
    await asyncio.sleep(0.5)


@pytest.mark.asyncio
async def test_get_server_info():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    resp = await cryptixd_client.get_server_info()

    assert resp.get("getServerInfoResponse") is not None
    await asyncio.sleep(0.5)


@pytest.mark.asyncio
async def test_get_sync_status():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    resp = await cryptixd_client.get_sync_status()

    assert resp.get("getSyncStatusResponse") is not None
    await asyncio.sleep(0.5)


@pytest.mark.asyncio
async def test_get_fee_estimate():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    resp = await cryptixd_client.get_fee_estimate()

    assert resp.get("getFeeEstimateResponse") is not None
    await asyncio.sleep(0.5)


@pytest.mark.asyncio
async def test_get_daa_score_timestamp_estimate():
    cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
    resp = await cryptixd_client.get_daa_score_timestamp_estimate([75993518, 75999518])

    assert resp.get("getDaaScoreTimestampEstimateResponse") is not None
    await asyncio.sleep(0.5)


# @pytest.mark.asyncio
# async def test_estimate_network_hashes_per_secondestimate_network_hashes_per_second():
#     cryptixd_client = CryptixdClient(CRYPTIXD_TEST_HOST, CRYPTIXD_TEST_PORT)
#     resp = await cryptixd_client.estimate_network_hashes_per_second(1, "123")
#
#     assert resp.get("estimateNetworkHashesPerSecond") is not None
#     await asyncio.sleep(.5)
