import argparse
import os
from colorama import Fore, Style, init
from modules.subdomains import scanSubdomain
from modules.directoryScanner import scan_directories
from modules.dns_recon import startDnsLookup
from modules.metadata import metadata

import requests

init(autoreset=True) # Initialize colorama

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OSINT Deep Scraper")
    parser.add_argument("-d", "--domain", required=True, help="Domain name to scan")
    parser.add_argument("-p", "--protocol", default="http", help="Protocol (e.g., http, https)")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to the wordlist file")
    parser.add_argument("-s", "--save", help="Specify a directory name to save the output files.")
    args = parser.parse_args()

    domain = args.domain
    protocol = args.protocol
    wordlist_path = args.wordlist

    if args.save:
        output_dir = args.save
        os.makedirs(output_dir, exist_ok=True)

    print(f"{Fore.YELLOW}[*] Starting subdomain scan for {domain}...")
    subdomains = scanSubdomain(domain)
    print(f"{Fore.GREEN}[+] Found {len(subdomains)} subdomains.")
    for sub in subdomains:
        print(f"{Fore.BLUE}  {sub}")

    if args.save:
        with open(os.path.join(output_dir, "subdomains.txt"), "w") as f:
            for sub in subdomains:
                f.write(sub + "\n")

    print(f"{Fore.YELLOW}[*] Starting directory scan for {domain}...")
    directories = scan_directories(domain, protocol, wordlist_path)
    print(f"{Fore.GREEN}[+] Found {len(directories)} directories.")
    for d in directories:
        print(f"{Fore.BLUE}  {d}")

    if args.save:
        with open(os.path.join(output_dir, "directories.txt"), "w") as f:
            for d in directories:
                f.write(d + "\n")

    print(f"{Fore.YELLOW}[*] Starting DNS lookup for {domain}...")
    dns_records = startDnsLookup(domain)
    print(f"{Fore.GREEN}[+] Found {len(dns_records)} DNS records.")
    for record in dns_records:
        print(f"{Fore.BLUE}  {record}")

    if args.save:
        with open(os.path.join(output_dir, "dns.txt"), "w") as f:
            for record in dns_records:
                f.write(record + "\n")

    print(f"{Fore.YELLOW}[*] Starting metadata scan for {domain}...")
    metadata_results = metadata(domain, protocol)
    print(f"{Fore.GREEN}[+] Found {len(metadata_results)} metadata entries.")
    for meta in metadata_results:
        print(f"{Fore.BLUE}  {meta}")

    if args.save:
        with open(os.path.join(output_dir, "metadata.txt"), "w") as f:
            for meta in metadata_results:
                f.write(meta + "\n")

        # Create combined.txt
        with open(os.path.join(output_dir, "combined.txt"), "w") as combined_file:
            combined_file.write("--- Subdomains ---\n")
            for sub in subdomains:
                combined_file.write(sub + "\n")
            combined_file.write("\n--- Directories ---\n")
            for d in directories:
                combined_file.write(d + "\n")
            combined_file.write("\n--- DNS Records ---\n")
            for record in dns_records:
                combined_file.write(record + "\n")
            combined_file.write("\n--- Metadata ---\n")
            for meta in metadata_results:
                combined_file.write(meta + "\n")

    print(f"{Fore.GREEN}[+] Scan complete.")
