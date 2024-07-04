import urllib.request
from html.parser import HTMLParser
import time

class LinkFinder(HTMLParser):
    def __init__(self):
        super().__init__()
        self.recording = 0
        self.data = []

    def handle_starttag(self, tag, attrs):
        if tag == 'p' and not self.recording:
            self.recording = 1
        if tag == 'a' and self.recording == 1:
            for name, value in attrs:
                if name == 'href':
                    if value.startswith('/wiki/'):
                        self.data.append(value)
                        self.recording = 0
                        break

    def handle_endtag(self, tag):
        if tag == 'p' and self.recording:
            self.recording = 0

def find_first_link(url):
    request = urllib.request.urlopen(url)
    html = request.read().decode('utf-8')
    link_finder = LinkFinder()
    link_finder.feed(html)

    if link_finder.data:
        return 'https://en.wikipedia.org' + link_finder.data[0]
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