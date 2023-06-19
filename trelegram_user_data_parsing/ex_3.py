import os

from tg_api_id import api_id
from tg_api_hash import api_hash


from telethon import TelegramClient, events, sync, connection


client = TelegramClient("ex_3", api_id, api_hash)

client.start()

members = client.get_participants("https://t.me/Parsinger_Telethon_Test")

for i, user in enumerate(members):
    client.download_profile_photo(user, f"{i}", download_big=True)


def get_size(folder: str):
    return sum(
        [os.path.getsize(f"{folder}/{file}") for file in os.listdir(folder)]
    )


print(get_size(""))
client.log_out()
