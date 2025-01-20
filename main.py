# ASCII Art Header
# ===========================================
#  ________          ________           _____ _      ________     _____   ___  
# |  ____\ \        / /  ____|   /\    / ____| |    |  ____\ \   / / _ \ / _ \ 
# | |__   \ \  /\  / /| |__     /  \  | (___ | |    | |__   \ \_/ / | | | (_) |
# |  __|   \ \/  \/ / |  __|   / /\ \  \___ \| |    |  __|   \   /| | | |\__, |
# | |       \  /\  /  | |____ / ____ \ ____) | |____| |____   | | | |_| |  / / 
# |_|        \/  \/   |______/_/    \_\_____/|______|______|  |_|  \___/  /_/  
# ===========================================

import requests
from bs4 import BeautifulSoup
import schedule
import time
import re

# Proxy websites
PROXY_SITES = [
    # ... (list remains the same)
]

# Proxy storage
PROXIES = []

def scrape_proxies():
    global PROXIES
    PROXIES = []
    
    for site in PROXY_SITES:
        try:
            response = requests.get(site, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract proxies from each site
            proxies = soup.find_all('tr')
            for proxy in proxies:
                ip = proxy.find('td').text
                port = proxy.find('td', class_='port').text
                
                # Detect proxy protocol
                protocol = None
                if "socks4" in ip.lower():
                    protocol = "socks4"
                    ip = ip.replace("socks4://", "").replace("socks4@", "")
                elif "socks5" in ip.lower():
                    protocol = "socks5"
                    ip = ip.replace("socks5://", "").replace("socks5@", "")
                elif "http" in ip.lower():
                    protocol = "http"
                else:
                    protocol = "http"  # Default protocol
                
                # Format proxy string
                if protocol == "http":
                    proxy_str = f"http://{ip}:{port}"
                elif protocol in ["socks4", "socks5"]:
                    proxy_str = f"{protocol}://{ip}:{port}"
                
                PROXIES.append(proxy_str)
                
        except Exception as e:
            print(f"Error scraping {site}: {e}")
            
    print(f"Scraped {len(PROXIES)} proxies")
    
    # Save proxies to file
    with open('proxies.txt', 'w') as f:
        for proxy in PROXIES:
            f.write(proxy + "\n")

def main():
    schedule.every(1).minutes.do(scrape_proxies)  # Run every 1 minute
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
