import json
import discord
import requests
import asyncio
import aiohttp
from discord import Client


async def async_translate_text(text: str, token: str, source: str, target: str, discord_client: discord.User, user_id: int):
    headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "source": source,
        "target": target
    }
    url = f"https://api.nlpcloud.io/v1/async/nllb-200-3-3b/translation"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            result = await response.text()
            result = json.loads(result)
            url_second = result["url"]
            await asyncio.sleep(10)
            await check_task_status(url_second, token, discord_client, user_id)


async def check_task_status(url: str, token: str, discord_client: discord.User, user_id: int):
    headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }
    url = url
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            result = await response.text()
            if result == "":
                await asyncio.sleep(10)
                await check_task_status(url, token, discord_client, user_id)
            result = json.loads(result)
            if result["http_code"] == 200:
                print(f"Task {url} is completed")
                user = await discord_client.fetch_user(user_id)
                content = json.loads(result["content"])
                await user.send(content["translation_text"])
            else:
                print(f"Task {url} is in progress")
                await asyncio.sleep(10)
                await check_task_status(url, token, discord_client, user_id)
