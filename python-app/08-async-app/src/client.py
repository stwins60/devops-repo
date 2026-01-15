import aiohttp
import asyncio

class AsyncHTTPClient:
    def __init__(self, timeout=30):
        self.timeout = aiohttp.ClientTimeout(total=timeout)
        self.session = None
    
    async def __aenter__(self):
        self.session = aiohttp.ClientSession(timeout=self.timeout)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()
    
    async def fetch(self, url):
        """Fetch a single URL"""
        async with self.session.get(url) as response:
            return await response.text()
    
    async def fetch_all(self, urls):
        """Fetch multiple URLs concurrently"""
        tasks = [self.fetch(url) for url in urls]
        return await asyncio.gather(*tasks)
