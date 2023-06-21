import os

from telethon import TelegramClient, events, sync, connection
from telethon.tl.types import InputMessagesFilterPhotos

from tg_api_id import api_id
from tg_api_hash import api_hash


# with TelegramClient("ex_5", api_id, api_hash) as client:
#     all_messages = client.get_messages("https://t.me/Parsinger_Telethon_Test", filter=InputMessagesFilterPhotos, limit=21)
#
#     for message in all_messages:
#         client.download_media(message, file="photos/img")


def get_size(folder: str):
    return sum(
        [os.path.getsize(f"{folder}/{file}") for file in os.listdir(folder)]
    )


print(get_size("photos"))
