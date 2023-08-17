from typing import Union
import pyrogram
from fastapi import FastAPI
from settings import *
import asyncio

def on_start():
    asyncio.create_task(client.start())

client = pyrogram.Client('bot', api_id, api_hash)
app = FastAPI(on_startup=on_start())

@app.get("/send_bot/")
async def read_root(username:str, id: str):
    await client.send_message(username, id)
    await asyncio.sleep(3)
    result = ''
    async for i in client.get_chat_history(username, limit=2):
        if i.from_user.username == username:
            result = i.text
    if 'not found' in result.lower():
        return {"result": False}
    else:
        result = result.splitlines()
        for i in result:
            if 'Balance' in i:
                result = i.strip().split(': ')[-1]
        if '$' in result:
            result = result.split(' ')[-1].replace(',', ' ').strip()
            if float(result) >= 25:
                pass
            else:
                pass
        elif '₽' in result:
            result = result.split(' ')[-1].replace(',', ' ').strip()
            if float(result) >= 2200:
                return {"result": 'more'} 
            else:
                return {"result": 'less'} 
        elif '₸' in result:
            result = result.split(' ')[-1].replace(',', ' ').strip()
            if float(result) >= 11150:
                return {"result": 'more'} 
            else:
                return {"result": 'less'} 
        elif '₴' in result:
            result = result.split(' ')[-1].replace(',', ' ').strip()
            if float(result) >= 950:
                return {"result": 'more'} 
            else:
                return {"result": 'less'} 
        elif 'Rp' in result:
            result = result.split(' ')[-1].replace(',', ' ').strip()
            if float(result) >= 80:
                return {"result": 'more'} 
            else:
                return {"result": 'less'} 
        else: 
            try:
                result = float(result.replace(',', ' ').strip())
                if result >= 25:
                    return {"result": 'more'} 
                else:
                    return {"result": 'less'} 
            except:
                return {"result": False}
#uvicorn main:app --reload