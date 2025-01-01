# selenium_middleware.py

from scrapy import signals
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from scrapy.http import HtmlResponse
import time

# class SeleniumMiddleware:
#     def __init__(self):
#         # Set up the Selenium driver (using Chrome in this example)
#         self.driver = webdriver.Chrome()

#     def process_request(self, request, spider):
#         self.driver.get(request.url)
#         time.sleep(2)  # Adjust delay as necessary for content to load
#         body = self.driver.page_source
#         return HtmlResponse(self.driver.current_url, body=body, encoding='utf-8', request=request)

#     def __del__(self):
#         self.driver.quit()


class SeleniumMiddleware:
    def __init__(self):
        # Set up the Selenium driver (using Firefox with GeckoDriver)
        service = Service(executable_path='path/to/geckodriver')  # Replace with the path to your geckodriver if needed
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')  # Run in headless mode (no GUI)
        self.driver = webdriver.Firefox(service=service, options=options)

    def process_request(self, request, spider):
        self.driver.get(request.url)
        time.sleep(2)  # Adjust the delay as necessary for the page content to load fully
        body = self.driver.page_source
        return HtmlResponse(self.driver.current_url, body=body, encoding='utf-8', request=request)

    def __del__(self):
        self.driver.quit()




       
