import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def download_site(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    executor = ThreadPoolExecutor(max_workers=5)
    with requests.Session() as session:
        futures = []
        for url in sites:
            futures.append(executor.submit(download_site, url, session))
        for future in as_completed(futures):
            future.result()


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "https://uol.com.br",
        "https://www.yahoo.com.br",
    ] * 40
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"{len(sites)} sites em {duration} segundos")