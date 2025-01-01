import scrapy
from urllib.parse import urljoin
import re

class EmailSpider(scrapy.Spider):
    name = 'email_spider'

    # User inputs
    query1 = "daniel"  # Keyword 1
    query2 = "freddy"  # Keyword 2
    start_urls = ['https://google.com']  # Start URL
    max_depth = 25  # Depth limit

    custom_settings = {
        'DEPTH_LIMIT': max_depth,  # Sets maximum depth for crawling
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    }

    def parse(self, response):
        # Check if both query keywords are present on the page
        print(f"Scraping URL: {response.url}")  # Shows which URL is being scraped
        print(response.text[:500]) 
        page_text = response.text.lower()
        #if self.query1.lower() in page_text and self.query2.lower() in page_text:
            # Find all email addresses on the page
        emails = set(re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', response.text))
        if emails:
            yield {
                    'url': response.url,
                    'emails': list(emails)
                }

        # Follow links to other pages on the same domain
        for link in response.css('a::attr(href)').getall():
            full_url = urljoin(response.url, link)
            # Only follow links within the same domain
            if self.start_urls[0] in full_url:
                yield scrapy.Request(full_url, callback=self.parse)
