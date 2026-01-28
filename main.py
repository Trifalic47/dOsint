from colorama import Fore, Style, init
from subdomains import scanSubdomain
from directoryScanner import (
    check_dir, scan_directories
)
from dns_recon import startDnsLookup
from metadata import metadata

import requests

init(autoreset=True)

if __name__ == "__main__":
    domain = input(f"{Fore.GREEN}Enter the domain name:{Fore.BLUE}")
    protocol = input(f"{Fore.GREEN}Enter the protocol name:{Fore.BLUE}")
    wordlist_path = input(f"{Fore.GREEN}Enter the wordlist_path:{Fore.BLUE}")
    scanSubdomain(domain)
    scan_directories(domain, protocol, wordlist_path)
    startDnsLookup(domain)
    metadata(domain, protocol)
