import asyncio
import aiohttp
from aiogram import Bot, Dispatcher, types

API_TOKEN = '7051035349:AAEDGlpEKBgbOFYXgV1fG9N_zSNNRQtyw5E'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


WEBHOOK_URL = 'https://jango.uz/api/get/list/order/'


chat_id = '-4285472798'

old_data = []


async def fetch_data():
    async with aiohttp.ClientSession() as session:
        async with session.get(WEBHOOK_URL) as response:
            data = await response.json()
    return data

async def send_data_to_chat(data):
    for item in data:
        message = f"Name: {item['name']}\nLast Name: {item['last']}\nPhone Number: {item['phone']}\nAddress: {item['addres']}\nLiters: {item['liter']}"
        await bot.send_message(chat_id=chat_id, text=message)

async def check_for_new_data():
    global old_data
    while True:
        data = await fetch_data()
        new_data = [item for item in data if item not in old_data]
        if new_data:
            await send_data_to_chat(new_data)
            old_data += new_data
        await asyncio.sleep(10)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(check_for_new_data())
