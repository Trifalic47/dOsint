from colorama import Fore, Style, init

import requests

init(autoreset=True)


def scanSubdomain(domainName):
    url = f"https://crt.sh/?q=%.{domainName}&output=json"
    response = requests.get(url)
    data = response.json()

    subdomains = set()
    for entry in data:
        name = entry["name_value"]
        lines = name.split("\n")
        for line in lines:
            clean_name = line.replace("*.", "").strip()
            subdomains.add(clean_name)
    for sub in sorted(subdomains):
        print(f"{Fore.GREEN}[+]Found: {Fore.BLUE}{sub}")


if __name__ == "__main__":
    domain = input("Enter domain name:")
    scanSubdomain(domain)
