from pyrogram import Client, filters

from modules.plugins_1system.settings.main_settings import module_list, file_list
from prefix import my_prefix

@Client.on_message(filters.command("calc", prefixes=my_prefix()) & filters.me)
async def calucate(client, message):
    list_m = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя,;"'
    try:
        msg = ''.join(message.text.lower().split()[1:])
        for s in list_m:
            msg = msg.replace(s, '')
        try:
            res = eval(msg)
            await message.edit(f"Result : {res}")
        except Exception as exc:
            await message.edit(f"Error : {exc}")
    except IndexError:
        await message.edit("Error : No input")
    