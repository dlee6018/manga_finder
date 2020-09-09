import webbrowser
import requests
from bs4 import BeautifulSoup


res = requests.get(
    'https://mangarawr.com/manga/kaguya-sama-wa-kokurasetai-tensai-tachi-no-renai-zunousen/')
# soup = BeautifulSoup(res.text, 'html.parser')
# url = soup.find(
#     'a', href='https://mangarawr.com/manga/kaguya-sama-wa-kokurasetai-tensai-tachi-no-renai-zunousen/chapter-199/')
# print(url)


soup = BeautifulSoup(res.text, 'html.parser')
links_with_text = []
for a in soup.find_all('a', href=True):
    if a.text:
        links_with_text.append(a['href'])
url = links_with_text[28]
webbrowser.open(url)
