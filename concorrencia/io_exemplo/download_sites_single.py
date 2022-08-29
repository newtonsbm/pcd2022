import requests
import time


def download_site(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    for url in sites:
        session = requests.Session()
        download_site(url, session)


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