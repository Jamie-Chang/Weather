"""Module that talks to darksky API."""
import aiohttp
import asyncio
import os

API_KEY = os.environ['DARK_SKY_API_KEY']

LOCATION = '51.5074,0.1278'


def _get_url():
    return f'https://api.darksky.net/forecast/{API_KEY}/{LOCATION}?units=si'


async def fetch():
    """Fetch the darksky JSON doc at the moment."""
    async with aiohttp.ClientSession() as session:
        async with session.get(get_url()) as response:
            return await response.json()


async def fetch_temperature() -> float:
    """Fetch the current temperature from darksky."""
    temperature_doc = await fetch()
    return temperature_doc.get('currently', {}).get('temperature')
