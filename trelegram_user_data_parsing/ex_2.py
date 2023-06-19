from tg_api_id import api_id
from tg_api_hash import api_hash

from telethon import TelegramClient, events, sync, connection


client = TelegramClient("ex_2", api_id, api_hash)

client.start()

members_data = client.get_participants("https://t.me/Parsinger_Telethon_Test")

res = []

for member in members_data:
    res.append(
        str(member.id) + " " + str(member.first_name) + " " + str(member.last_name) + " " + str(member.phone)

    )

print(res)
