from bs4 import BeautifulSoup
from selenium import webdriver

import time


driver = webdriver.Chrome()

driver.get('https://treehouse-projects.github.io/horse-land/index.html')
time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())

driver.close()
