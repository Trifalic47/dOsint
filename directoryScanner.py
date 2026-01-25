import requests
from colorama import Fore, Style, init
from concurrent.futures import (
    ThreadPoolExecutor,
)

init(autoreset=True)


def check_dir(url, directory):
    full_url = f"{url}/{directory}/"
    try:
        # Use a generic User-Agent so the server doesn't block "python-requests"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(
            full_url, timeout=2, headers=headers, allow_redirects=False
        )

        # 200 = Success, 403 = Forbidden (but it exists!), 301/302 = Redirect
        if response.status_code in [200, 403, 301, 302]:
            print(
                f"{Fore.GREEN}[+]{response.status_code} Found: {Fore.WHITE}{full_url}"
            )
    except Exception:
        pass


def scan_directories():
    domain = input("Enter domain (e.g., tesla.com): ")
    protocol = input("Protocol (http/https): ")
    wordlist_path = input("Path to wordlist: ")

    # 1. Clean the URL
    base_url = f"{protocol}://{domain}"

    # 2. Load the wordlist
    try:
        with open(wordlist_path, "r") as f:
            words = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"{Fore.RED}[!] Wordlist not found.")
        return

    print(f"[*] Scanning {base_url} with {len(words)} words...")

    # 3. Use a ThreadPool to limit to 40 concurrent workers
    with ThreadPoolExecutor(max_workers=40) as executor:
        for word in words:
            executor.submit(check_dir, base_url, word)


if __name__ == "__main__":
    scan_directories()
