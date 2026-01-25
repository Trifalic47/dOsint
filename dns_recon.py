# Importing specific functions from libraries
from colorama import Fore, Style, init

# Import full libraries
import requests
import dns.resolver

# Doing some initialization for the code so it works properly
init(autoreset=True)


def startDnsLookup(domainName):
    records = ["A", "AAAA", "CNAME", "MX", "NS", "TXT", "SRV", "SOA", "PTR", "CAA"]
    for record in records:
        try:
            res = dns.resolver.resolve(domainName, record)
            for ans in res:
                print(f"[+]Found {record}: {Fore.BLUE}{ans.to_text()}")
        except dns.resolver.NoAnswer:
            print(f"[-]{record}: {Fore.YELLOW}Not Found")
        except dns.resolver.LifetimeTimeout:
            print(f"[-]{record}: {Fore.YELLOW}Not Found")


if __name__ == "__main__":
    domainName = input("Enter the domain name to get the dns record:")
    startDnsLookup(domainName)
