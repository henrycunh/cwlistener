from telethon import TelegramClient
from telethon.tl.types import UpdateNewMessage
import re
import time

api_id      = 156713
api_hash    = "ddd9386ca051bff73d53bd6f41896ee5"

phone_number = '+5579996288344'
cw_id = 408101137
client = TelegramClient( 'cwlistener' , api_id, api_hash, update_workers=4 )

def client_main():
    user = client.get_me()
    client.add_update_handler( on_update )
    user_in = ""
    while(user_in != "\q"):
        # Handle user input
        if user_in == 'get':
            get_user_data()
        user_in = input( "> " )

def get_user_data():
    cw_bot = client.get_entity('@chtwrsbot')
    client.send_message( cw_bot, "🏅Me" )
    # while last_message == '':
    #     print('Polling for /me...')
    #     update = client.updates.poll(timeout=.2)
    #     print ("got here")
    #     if isinstance( update, UpdateNewMessage ) and update.message.from_id == cw_id:
    #         last_message = update.message.message
    #         break
    # print( stamina['current'] )

def on_update( update ):
    if isinstance( update, UpdateNewMessage ) and update.message.from_id == cw_id:
        message = update.message.message
        stamina_match = re.search(r"Stamina: (\d+)/(\d+)", message)
        if stamina_match:
            stamina = { 
                'current'   : stamina_match.group(1),
                'max'       : stamina_match.group(2)
            }
        foray_match = re.search( r"click \/go", message )
        if foray_match:
            cw_bot = client.get_entity('@chtwrsbot')
            client.send_message( cw_bot, "/go" )

# Connects the client, asserts on error
assert client.connect()

client.start( phone_number )
client_main()

# if client.is_user_authorized():
# else:
    # client_main()




