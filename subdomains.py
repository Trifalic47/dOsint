from colorama import Fore, Style, init

import requests

init(autoreset=True)

if __name__ == "__main__":
    url = "https://crt.sh/?q=%25.tesla.com&output=json"
    response = requests.get(url)
    data = response.json()

    # print(data)

    # Fetching subdomain from the JSON
    subdomain = set()  # This will automatically remove the duplicate
    for entry in data:
        # Get the name_value from the entry
        name = entry["name_value"]

        # Split from \n to prevent new line characters
        lines = name.split("\n")
        # print(lines)

        for line in lines:
            clean_name = line.replace("*.", "").strip()
            subdomain.add(clean_name)
    for sub in sorted(subdomain):
        print(f"[+]Found:{Fore.BLUE}{sub}")
