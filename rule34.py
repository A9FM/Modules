from pyrogram import Client, filters
from modules.plugins_1system.settings.main_settings import module_list, file_list

from prefix import my_prefix
from requirements_installer import install_library

install_library('xmltodict')

from random import randint

import requests
import xmltodict


@Client.on_message(filters.command("r34", prefixes=my_prefix()) & filters.me)
async def rulka(cilent , message):
    try:
        arg = '_'.join(message.text.lower().split()[1:])
        try:
            url = f"https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&tags={arg}"
            response = requests.get(url)
            dict_data = xmltodict.parse(response.text)
            da , len_post = dict_data['posts']['post'] , len(dict_data['posts']['post'])
            num = randint(0, len_post-1)
            url_res = da[num]['@file_url']
            await message.edit(f'🔞 Нашли результат по {arg} : {url_res}')
        except KeyError:
            await message.edit(f'Ничего не найдено!')
        except IndexError:
            await message.edit(f'Ничего не найдено!')
    except IndexError:
        await message.edit('Нет агрументов!')

module_list['Rule34'] = f'{my_prefix()}r34 (tag)'
file_list['Doxx'] = 'rule34.py'
