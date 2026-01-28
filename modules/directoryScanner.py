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
            return response.status_code, full_url
    except Exception:
        pass
    return None


def scan_directories(domain, protocol, wordlist_path):
    # domain = input("Enter domain (e.g., tesla.com): ")
    # 1. Clean the URL
    base_url = f"{protocol}://{domain}"

    # 2. Load the wordlist
    try:
        with open(wordlist_path, "r") as f:
            words = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"{Fore.RED}[!] Wordlist not found.")
        return []

    print(f"[*] Scanning {base_url} with {len(words)} words...")
    found_directories = []
    # 3. Use a ThreadPool to limit to 40 concurrent workers
    with ThreadPoolExecutor(max_workers=40) as executor:
        futures = [executor.submit(check_dir, base_url, word) for word in words]
        for future in futures:
            result = future.result()
            if result:
                status_code, full_url = result
                print(
                    f"{Fore.GREEN}[+]{status_code} Found: {Fore.WHITE}{full_url}"
                )
                found_directories.append(full_url)
    return found_directories


if __name__ == "__main__":
    domain = "google.com"
    protocol = "https"
    wordlist_path = input("Wordlist path:")
    scan_directories(domain, protocol, wordlist_path)
