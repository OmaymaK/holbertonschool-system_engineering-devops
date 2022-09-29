#!/usr/bin/python3
"""Parses the title of all hot articles, and prints a sorted count."""


import requests


def count_words(subreddit, word_list, after='', hot_list={}):
    """Parse the title."""
    headers = {'User-Agent': "Mozilla/5.0"}
    url = 'https://www.reddit.com'
    r = requests.get('{}/r/{}/hot.json?after={}?limit=100'
                     .format(url, subreddit, after),
                     headers=headers, allow_redirects=False)
    if r.status_code == 302:
        return None
    d = r.json()
    if d.get('data') is None:
        return None
    for post in d['data']['children']:
        title = post['data']['title'].lower().split(' ')
        for word in title:
            if word in word_list and hot_list.get(word):
                if hot_list.get(word):
                    hot_list[word] += 1
                else:
                    hot_list[word] = 0

    if d['data']['after'] is None:
        for word in sorted(hot_list, key=lambda x: x[1]):
            print(word[0], word[1])

    return count_words(subreddit, d['data']['after'], hot_list)
