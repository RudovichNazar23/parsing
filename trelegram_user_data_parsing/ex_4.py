import os

# from tg_api_id import api_id
# from tg_api_hash import api_hash
#
# from telethon import TelegramClient, events, sync, connection
#
#
# with TelegramClient("ex_4", api_id, api_hash) as client:
#     all_members = client.get_participants("https://t.me/Parsinger_Telethon_Test")
#
#     for member in all_members:
#         for iter_photo in client.iter_profile_photos(member):
#             client.download_media(iter_photo, file="img/")


def get_size(folder: str):
    return sum(
        [os.path.getsize(f"{folder}/{file}") for file in os.listdir(folder)]
    )
