import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, urlparse
import time

def scrape_emails_by_niche(niche1, niche2, website_url, max_depth=2):
    visited_urls = set()  # Track visited URLs to avoid revisiting
    found_emails = set()  # Store found emails
    base_domain = urlparse(website_url).netloc  # To restrict to the same domain
    
    def is_valid_url(url):
        """Check if URL belongs to the same domain and has not been visited."""
        parsed_url = urlparse(url)
        return parsed_url.netloc == base_domain and url not in visited_urls
    
    def find_emails_in_page(url, depth):
        """Recursively finds emails in the page and follows links."""
        if depth > max_depth:
            return  # Stop recursion if max depth is reached

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Check if the page contains niche-related content
            text = soup.get_text().lower()
            if niche1.lower() in text or niche2.lower() in text:
                # Find all emails in text
                emails = set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text))
                found_emails.update(emails)
            
            # Find all internal links on the page
            for link in soup.find_all('a', href=True):
                href = urljoin(website_url, link['href'])
                if is_valid_url(href):
                    visited_urls.add(href)  # Mark as visited
                    find_emails_in_page(href, depth + 1)  # Recursive call

        except requests.RequestException as e:
            print('Error accessing')

    # Initialize the search from the main URL
    visited_urls.add(website_url)
    find_emails_in_page(website_url, depth=0)
    
    return list(found_emails)

# Example usage
niche1 = "technology"
niche2 = "innovation"
website_url = "https://www.google.com"
emails = scrape_emails_by_niche(niche1, niche2, website_url, max_depth=3)
print("Found emails:", emails)
