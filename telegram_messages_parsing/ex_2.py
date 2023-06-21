from telethon import TelegramClient, events, sync, connection

from tg_api_id import api_id
from tg_api_hash import api_hash

with TelegramClient("ex_2", api_id, api_hash) as client:
    messages = client.iter_messages("https://t.me/Parsinger_Telethon_Test")

    for i in messages:
        if i.pinned:
            print(i.from_id.user_id)
            break
