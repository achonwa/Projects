import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

def find_emails(query1, query2, website):
    # List to store found emails
    emails = set()
    visited_urls = set()  # To keep track of visited pages to avoid loops

    def search_page(url):
        """Searches the specified page for emails and checks for queries."""
        try:
            # Send a request to the URL
            response = requests.get(url, timeout=5)
            response.raise_for_status()
        except requests.RequestException:
            return  # Ignore pages that can't be loaded

        # Parse the page content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Check if the page has content related to the queries
        if query1.lower() in soup.text.lower() and query2.lower() in soup.text.lower():
            # Find all email addresses
            new_emails = set(re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', soup.text))
            emails.update(new_emails)

        # Find links on the page to continue crawling
        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(url, href)
            
            # Only proceed with the links within the same website
            if website in full_url and full_url not in visited_urls:
                visited_urls.add(full_url)
                search_page(full_url)

    # Start searching from the homepage
    search_page(website)

    return list(emails)

# Usage example
query1 = "data science"
query2 = "machine learning"
website = "https://linkedin.com"
emails = find_emails(query1, query2, website)
print("Emails found:", emails)
