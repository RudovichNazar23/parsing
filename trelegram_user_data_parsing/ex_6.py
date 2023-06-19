from telethon import TelegramClient, events, sync, connection
from telethon.tl.functions.users import GetFullUserRequest

from tg_api_id import api_id
from tg_api_hash import api_hash

lst = ['Anthony_Hills', 'Craig_Moody', 'Kathleen_Browns', 'Vicki_Baileys', 'Jorge_Garrett',
       'Larry_Summers', 'Tommy_Sullivan', 'Edward_Murrray', 'Nicholas_Gonzales',
       'Virgina_Garcia', 'Denise_Barker', 'Jessie_Wright', 'Mary_Baileyn',
       'Claytons_Riley', 'Joshuan_Chandler', 'Jameson_Powell', 'Harry_Valdes',
       'Chriss_Yong', 'Sarah_Wilis', 'Frances_Ross', 'Joseph_Anderson'
       ]

client = TelegramClient("ex_6", api_id, api_hash)

client.start()

users = [
    i for i in client.get_participants("https://t.me/Parsinger_Telethon_Test") if i.username in lst
]

res = []

for user in users:
    user_info = client(GetFullUserRequest(user))
    res.append(int(user_info.full_user.about))

print(sum(res))


client.log_out()
