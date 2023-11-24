import requests
from bs4 import BeautifulSoup
import time

def find_first_link(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    content_div = soup.find(id='mw-content-text').find(class_='mw-parser-output')

    for element in content_div.find_all('p', recursive=False):
        if element.find('a', recursive=False):
            return 'https://en.wikipedia.org' + element.find('a', recursive=False).get('href')

    return None

def get_to_philosophy():
    url = 'https://en.wikipedia.org/wiki/Special:Random'
    visited_urls = [url]

    while url:
        print(url)
        first_link = find_first_link(url)
        if not first_link:
            print('No links found, stopping search!')
            break
        elif first_link in visited_urls:
            print('Stuck in a loop, stopping search!')
            break
        elif 'Philosophy' in first_link:
            print('Reached Philosophy!')
            break
        else:
            visited_urls.append(first_link)
            url = first_link
            time.sleep(2)  # Sleep to prevent overloading Wikipedia's servers

get_to_philosophy()
