from telethon import TelegramClient, events, sync, connection

from tg_api_id import api_id
from tg_api_hash import api_hash


client = TelegramClient("ex_1", api_id, api_hash)
client.start()

members = client.get_participants("https://t.me/Parsinger_Telethon_Test")

res = []

for member in members:
    res.append(str(member.first_name) + " " + str(member.last_name))

print(res)

