from bs4 import BeautifulSoup
from colorama import Fore, Style, init
from random_header_generator import HeaderGenerator

import requests

init(autoreset=True)

if __name__ == "__main__":
    url = "https://www.google.com"
    tags_list = ['a', 'img', 'video', 'meta']

    generator = HeaderGenerator()
    header = generator()

    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.content, 'lxml')

    for tag in tags_list:
        tag_names = soup.find_all(tag)
        if tag_names == []:
            print(f"{Fore.CYAN}[-]No tag found {Fore.RED}{tag}")
            continue
        print(f"{Fore.YELLOW}[+]Scraping Tag: {Fore.BLUE}{tag}")

        for tag_individual in tag_names:
            if tag == 'a':
                value = tag_individual.get('target')
                if value is None:
                    print(f"{Fore.GREEN}{tag_individual['href']}")
                else:
                    print(f"{Fore.GREEN}{tag_individual['href']} {
                          Fore.BLUE}Method: {Fore.GREEN}{tag_individual['target']}")
            elif tag in ['img', 'src']:
                value = tag_individual.get('src')
                if value is not None:
                    print(f"{Fore.GREEN}{tag_individual['src']}")
                else:
                    print(f"{Fore.GREEN}{tag_individual}")
            else:
                print(f"{Fore.GREEN}{tag_individual}")
