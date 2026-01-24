# dOsint – Deep OSINT Reconnaissance Tool

<img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python version"> 
<img src="https://img.shields.io/badge/Status-Under%20Development-orange?style=for-the-badge" alt="Project status">
<img src="https://img.shields.io/github/license/trifalicprime/dOsint?style=for-the-badge" alt="License">

**dOsint** is a modular, passive-first OSINT reconnaissance tool written in Python.  
Its main goal is to help security researchers, bug bounty hunters and red teamers quickly map a target's **external attack surface** using public data sources.

> **Focus**: speed, modularity, minimal footprint, Obsidian-friendly output

## 🎯 Current Modules

| Module              | Technique                     | Data Source          | Sends packets to target? | Output examples                                 |
| ------------------- | ----------------------------- | -------------------- | ------------------------ | ----------------------------------------------- |
| Subdomain enum      | Certificate Transparency logs | crt.sh               | No                       | dev, staging, api, admin, old, test...          |
| DNS reconnaissance  | Common record types lookup    | Public DNS resolvers | No                       | TXT (SPF, DMARC, keys?), MX, NS, A, CNAME       |
| Web metadata scrape | Filetype-specific crawling    | Target website       | Yes (light)              | Author names, software versions, internal paths |
| (planned) Shodan    | Exposed services & banners    | Shodan API           | No                       | open ports, IoT, VPN endpoints, server types    |

## 🛠️ Tech Stack

```text
Python ≥ 3.9
├── requests             → HTTP / JSON APIs
├── dnspython            → DNS queries
├── beautifulsoup4       → HTML parsing
├── colorama             → colored terminal output
├── aiohttp (planned)    → faster async HTTP
└── python-dotenv        → API key management
📥 Installation
Bash# 1. Clone repository
git clone https://github.com/trifalicprime/dOsint.git
cd dOsint

# 2. Create & activate virtual environment (recommended)
python -m venv venv
source venv/bin/activate    # Linux / macOS
venv\Scripts\activate       # Windows

# 3. Install dependencies
pip install -r requirements.txt
🚀 Quick Start
Bashpython main.py
textTarget domain (without http/https): example.com

[*] Starting passive reconnaissance on example.com
[>] Subdomain enumeration via crt.sh ........ 47 found
[>] DNS record enumeration .................. 6 records
[>] Metadata & file analysis ................ 3 interesting files
[✓] Report saved → reports/example.com-2025-08-17.md
📄 Obsidian Integration (Recommended)
dOsint automatically creates markdown reports compatible with Obsidian:

Saves files in ./reports/ folder
Uses frontmatter + clean hierarchy
Adds helpful tags: #target #recon #osint #pending-review

Example generated report structure:
Markdown---
domain: example.com
date: 2025-08-17
tool: dOsint v0.1
---

# Recon Report: example.com

**Tags:** #target #recon #pending

## Subdomains (47)

- app.example.com
- dev.example.com
- staging.example.com
- api-v2.example.com
...

## DNS Records

**MX**
→ mx1.example.com (priority 10)
→ mx2.google.com (priority 20)

**TXT**
→ "v=spf1 include:_spf.google.com ~all"
→ "google-site-verification=abc123..."

## Interesting Files / Metadata

- /docs/Annual-Report-2024.pdf
  → Author: Johnathan R.
  → Software: Microsoft Word 2016
...
⚠️ Legal & Ethical Reminder
This tool is provided for educational purposes and authorized security testing only.
The author is not responsible for misuse or damage caused by this software.
Always obtain explicit permission before testing any target you do not own.
📋 Roadmap (planned features)

 Asynchronous HTTP client (aiohttp)
 Shodan & Censys integration
 Email harvesting from crawled pages
 Wayback Machine / common.js analysis
 Passive SSL certificate fingerprinting
 JSON / CSV export besides Markdown
 Configurable rate-limiting & proxy support

📄 License
MIT License
Made with 🖤 by trifalicprime
textThis version looks professional yet shows that the project is still growing. Feel free to modify version numbers, add badges, shields.io icons, or change the tone to be more aggressive / stealth depending on your target audience.

Good luck with the project!

```
