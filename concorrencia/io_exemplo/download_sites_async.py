import time
import asyncio
import aiohttp

async def download_site(url, session):
    async with session.get(url) as response:
        content = await response.text()
        print(f"Read {len(content)} from {url}")



async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            tasks.append(download_site(url, session))
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "https://uol.com.br",
        "https://www.yahoo.com.br",
    ] * 40
    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"{len(sites)} sites em {duration} segundos")