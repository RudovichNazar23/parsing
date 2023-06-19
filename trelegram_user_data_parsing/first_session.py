from telethon import TelegramClient, events, sync, connection
from tg_api_id import api_id
from tg_api_hash import api_hash

client = TelegramClient("second_session", api_id, api_hash)
client.start()
print(client.get_me())
client.disconnect()
