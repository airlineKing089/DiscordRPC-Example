# import modules
import time
from pypresence import Presence

client_id = input("Client ID: ")
state = input("State: ")
details = input("Details: ")
large_image = input("Large Image Name: ")
small_image = input("Small Image Name: ")
large_image_text = input("Large Image Details: ")

class DiscordRPC():
    def RPC_Start(client_id, state, details, large_image, small_image, large_image_text):
        if isinstance(client_id) is True:
            # connect to the RPC
            RPC = Presence(client_id)
            RPC.connect()
            
            # updates the rpc
            print(RPC.update(state=state, details=details, large_image=large_image, small_image=small_image, large_text=large_image_text, start=time.time()))
            
            # while loop to keep it running
            while True:
                time.sleep(15)
               
    def RPC_Exit():
        Presence.close()

drpc = DiscordRPC()

drpc.RPC_Start(client_id, state, details, large_image, small_image, large_image_text)
