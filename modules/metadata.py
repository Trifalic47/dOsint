from bs4 import BeautifulSoup
from colorama import Fore, Style, init
from random_header_generator import HeaderGenerator

import requests

init(autoreset=True)


def metadata(url, protocol):
    fullUrl = f"{protocol}://{url}"
    tags_list = ['a', 'img', 'video', 'meta']
    metadata_results = []

    generator = HeaderGenerator()
    header = generator()

    response = requests.get(fullUrl, headers=header)
    soup = BeautifulSoup(response.content, 'lxml')

    for tag in tags_list:
        tag_names = soup.find_all(tag)
        if tag_names == []:
            metadata_results.append(f"[-]No tag found {tag}")
            continue
        metadata_results.append(f"[+]Scraping Tag: {tag}")

        for tag_individual in tag_names:
            if tag == 'a':
                value = tag_individual.get('target')
                if value is None:
                    metadata_results.append(f"{tag_individual['href']}")
                else:
                    metadata_results.append(f"{tag_individual['href']} Method: {tag_individual['target']}")
            elif tag in ['img', 'src']:
                value = tag_individual.get('src')
                if value is not None:
                    metadata_results.append(f"{tag_individual['src']}")
                else:
                    metadata_results.append(f"{tag_individual}")
            else:
                metadata_results.append(f"{tag_individual}")
    return metadata_results


if __name__ == "__main__":
    domain = "youtube.com"
    protocol = "https"
    metadata(domain, protocol)
