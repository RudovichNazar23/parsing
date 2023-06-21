from telethon import TelegramClient, events, sync, connection

from tg_api_id import api_id
from tg_api_hash import api_hash

res = 0

with TelegramClient("ex_4", api_id, api_hash) as client:
    all_messages = client.iter_messages("https://t.me/Parsinger_Telethon_Test")

    for message in all_messages:
        if message.from_id is not None:
            if message.from_id.user_id == 5807015533:
                res += int(message.message) if message.message.isdigit() else 0
        else:
            break
print(res)
