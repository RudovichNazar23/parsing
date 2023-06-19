from telethon import TelegramClient, events, sync, connection
from telethon.tl.functions.users import GetFullUserRequest

from tg_api_id import api_id
from tg_api_hash import api_hash

lst = [332703068, 5914813738, 5710963988, 5799970696, 5843185336,
       5899028303, 5799846345, 5988909155, 5765618528, 5744269105,
       5811870581, 5749394385, 5821321049, 5831778721, 5908359516,
       5807015533, 5877375636, 5748959968, 5852187682, 5642780248,
       5633717169, 5989940172]

client = TelegramClient("ex_5", api_id, api_hash)

client.start()

res = []

users = [i for i in client.get_participants("https://t.me/Parsinger_Telethon_Test") if int(i.id) in lst]

for user in users:
    user_info = client(GetFullUserRequest(user))
    res.append(int(user_info.full_user.about))

print(sum(res))
