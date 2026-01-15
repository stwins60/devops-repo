import asyncio
from client import AsyncHTTPClient
from tasks import run_concurrent_tasks

async def main():
    """Main async function"""
    print("Starting async application...")
    
    # Create HTTP client
    async with AsyncHTTPClient() as client:
        # Fetch multiple URLs concurrently
        urls = [
            'https://api.github.com',
            'https://httpbin.org/get',
            'https://jsonplaceholder.typicode.com/posts/1'
        ]
        
        results = await client.fetch_all(urls)
        for url, result in zip(urls, results):
            print(f"Fetched {url}: {len(result)} bytes")
    
    # Run concurrent tasks
    await run_concurrent_tasks()
    
    print("Application completed!")

if __name__ == '__main__':
    asyncio.run(main())
