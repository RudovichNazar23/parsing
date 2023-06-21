from telethon import TelegramClient, events, sync, connection

from tg_api_id import api_id
from tg_api_hash import api_hash

USER_ID = 5807015533

res = []

ids = []

with TelegramClient("ex_3", api_id, api_hash) as client:
    messages = client.iter_messages("https://t.me/Parsinger_Telethon_Test")

