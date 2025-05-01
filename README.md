This is a simple gRPC client for a python application which communiactes with the Cryptix node called CRYPTIXD.

The module is based on asyncio, since the Cryptix BlockDAG is unbelievable fast and also needs the support of notifications.

# Usage: see playground.py

    import asyncio

    from cryptixd_client.modules.CryptixdClient import CryptixdClient
    
    
    async def main():
        cryptixd_client = CryptixdClient("127.0.0.1", 16110)
    
        # print the info message
        print(await cryptixd_client.get_info())
    
        # returns
        # {'getInfoResponse': {'p2pId': 'a9728d7e-c07b-4641-936c-6c7442b819f8', 'serverVersion': '0.13.4',
        # 'isUtxoIndexed': True, 'isSynced': True, 'hasNotifyCommand': True, 'hasMessageId': True,
        # 'mempoolSize': '0'}, 'id': '0'}
    
    
        # now let's set up some notifications
        # the decorator registers an async callback function and requests the notification automatically

        @cryptixd_client.notify_virtual_daa_score_changed
        async def received_new_daa_score(c):
            print(f"The DAA score is: {c['virtualDaaScoreChangedNotification']['virtualDaaScore']}")
    
        @cryptixd_client.notify_virtual_daa_score_changed
        async def received_new_daa_score2(c):
            print(f"The DAA2 score is: {c['virtualDaaScoreChangedNotification']['virtualDaaScore']}")
    
        @cryptixd_client.notify_block_added
        async def received_new_daa_score(c):
            print(f"New Cryptix block: {c['blockAddedNotification']['block']['verboseData']['hash']}")
    
        # wait to see some notifcations :-)
        await asyncio.sleep(60)
    
    
    
    asyncio.run(main())
    
    
