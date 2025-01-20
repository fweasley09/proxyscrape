# ASCII Art Header
print(r'''
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
import time

# Function to scrape proxies from a public proxy website
def scrape_proxies(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract proxy data (IP, port, and type)
        proxies = []
        for row in soup.find_all('tr'):
            columns = row.find_all('td')
            if len(columns) >= 3:  # Ensure there are enough columns
                ip = columns[0].text.strip()
                port = columns[1].text.strip()
                proxy_type = columns[4].text.strip().lower()  # Assuming proxy type is in the 5th column
                proxies.append(f"{proxy_type}://{ip}:{port}")

        return proxies
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return []

# List of public proxy websites (add more as needed)
proxy_sites = [
    "https://free-proxy-list.net/",
    "https://www.us-proxy.org/",
    "https://www.sslproxies.org/",
    "https://free-proxy-list.net/anonymous-proxy.html",
]

# File to save scraped proxies
output_file = "scraped_proxies.txt"

# Main script
if __name__ == "__main__":
    all_proxies = []

    for site in proxy_sites:
        print(f"Scraping proxies from: {site}")
        proxies = scrape_proxies(site)
        all_proxies.extend(proxies)
        time.sleep(2)  # Pause between requests to avoid being blocked

    # Remove duplicates and save to file
    all_proxies = list(set(all_proxies))
    with open(output_file, "w") as file:
        file.write("\n".join(all_proxies))

    print(f"Scraped {len(all_proxies)} unique proxies.")
    print(f"Proxies saved to {output_file}.")
