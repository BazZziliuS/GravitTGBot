import aiohttp


async def get_weather(city: str) -> str | None:
    url = f"https://wttr.in/{city}?format=3"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as resp:
                if resp.status != 200:
                    return None
                text = await resp.text()
                if "Unknown location" in text:
                    return None
                return text.strip()
    except (aiohttp.ClientError, TimeoutError):
        return None
