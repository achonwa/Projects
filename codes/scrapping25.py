import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
import time

def find_emails(query1, query2, website, max_depth=2):
    emails = set()  # To store found emails
    visited_urls = set()  # To track visited pages to avoid reprocessing
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

    def search_page(url, depth):
        """Search the specified page for emails and keywords, following links up to max_depth."""
        if depth > max_depth:
            return

        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Failed to retrieve {url}: {e}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')

        # Only process if both queries are found in the page text
        if query1.lower() in soup.text.lower() and query2.lower() in soup.text.lower():
            new_emails = set(re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', soup.text))
            emails.update(new_emails)

        # Find all links and recursively process them if within the website domain
        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(url, href)

            if full_url.startswith(website) and full_url not in visited_urls:
                visited_urls.add(full_url)
                time.sleep(0.5)  # Pause to avoid overwhelming the server
                search_page(full_url, depth + 1)

    # Start the crawl from the homepage
    visited_urls.add(website)
    search_page(website, 0)

    return list(emails)

# Example usage
query1 = "@gmail.com"
query2 = "@yahoo.com"
website = "https://google.com"
emails = find_emails(query1, query2, website)
print("Emails found:", emails)
