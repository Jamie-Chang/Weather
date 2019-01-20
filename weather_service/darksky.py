import aiohttp
import asyncio
import os

API_KEY = os.environ['DARK_SKY_API_KEY']

LOCATION = '51.5074,0.1278'


def get_url():
    return f'https://api.darksky.net/forecast/{API_KEY}/{LOCATION}?units=si'


async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get(get_url()) as response:
            return await response.json()
