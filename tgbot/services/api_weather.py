import aiohttp


class WTTR:
    def __init__(self, city: str, fmt: int = 3):
        self.url = f"https://wttr.in/{city}?format={fmt}"
        self.session = aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=10))

    async def get_weather(self) -> str | None:
        try:
            async with self.session as session:
                async with session.get(self.url) as resp:
                    if resp.status != 200:
                        return None
                    text = await resp.text()
                    if "Unknown location" in text:
                        return None
                    return text.strip()
        except (aiohttp.ClientError, TimeoutError):
            return None
