from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://treehouse-projects.github.io/horse-land/index.html')
soup = BeautifulSoup(html.read(), 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))

site_links = []

# Here's a function that will receive a website's internal link and parse the html on that page.

def internal_links(linkURL):
    html = urlopen('https://treehouse-projects.github.io/horse-land/{}'.format(linkURL))
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find('a', href=re.compile('(.html)$'))  # anchor tags


if __name__ == '__main__':
    urls = internal_links("index.html")

    while len(urls) > 0:
        page = urls.attrs['href']
        if page not in site_links:
            site_links.append(page)

            print(page)
            print('\n=============\n')
            urls = internal_links(page)
        else:
            break
