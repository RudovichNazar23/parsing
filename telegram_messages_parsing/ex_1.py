from telethon import TelegramClient, events, sync, connection

from tg_api_id import api_id
from tg_api_hash import api_hash


res = 0

with TelegramClient("ex_1", api_id, api_hash) as client:
    messages = [int(i.message) for i in client.iter_messages("https://t.me/Parsinger_Telethon_Test") if i.message]

print(sum(messages))
