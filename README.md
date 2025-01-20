# proxyscrape
Here is a Python script using requests and BeautifulSoup to scrape free proxies from public proxy websites. It scrapes proxy IP addresses and ports, storing them in a text file for further use

# Features of the Script:
- Multiple Sources: Scrapes from multiple popular proxy list websites.
- Duplicate Removal: Ensures no duplicate proxies in the output.
- Error Handling: Gracefully handles errors during scraping.
- Customizable: You can add more proxy sites to the proxy_sites list.
- Output: Saves the scraped proxies to a file named scraped_proxies.txt.

# Dependencies:
```bash
pip install requests beautifulsoup4
