# import modules
import time
from pypresence import Presence

class DiscordRPC():
    def RPC_Start(client_id):
        if isinstance(client_id) is True:
            # connect to the RPC
            RPC = Presence(client_id)
            RPC.connect()
            
            # updates the rpc
            print(RPC.update(state="STATE HERE", details="DETAILS HERE", large_image="NAME OF LARGE IMAGE HERE", small_image="NAME OF SMALL IMAGE HERE", large_text="LARGE IMAGE TEXT HERE", start=time.time()))
            
            # while loop to keep it running
            while True:
                time.sleep(15)
               
    def RPC_Exit():
        Presence.close()
