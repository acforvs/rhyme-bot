from random import choice

import requests
from bs4 import BeautifulSoup

from static import SETTINGS

proxies = {
    'https': 'https://' + choice(SETTINGS['PROXIES'])
}

def get(word: str) -> str:
    url = 'https://rifme.net/r/{}/0'.format(word)
    agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    headers = {'User-Agent': agent}
    print(proxies)
    res = requests.get(url,
                       timeout=15,
                       proxies=proxies,
                       headers=headers)
    print(res.text)
    assert res.status_code == 200, 'request failed'
    return res.text


def get_rhymes_list(word: str) -> list:
    try:
        html = get(word)
        soup = BeautifulSoup(html, 'html.parser')
        word_table = soup.find_all("li",
                                   attrs={'class': 'riLi'})
        words = [word.get_text() for word in word_table]
        return words
    except:
        return []

def get_random_rhyme(word: str) -> str:
    words_list = get_rhymes_list(word)
    try:
        return choice(words_list)
    except:
        return ''
