#!/usr/bin/python3
"""Returns a list with the titles of hot articles for a given subreddit."""


import requests


def recurse(subreddit, after='', hot_list=[]):
    """Return a list."""
    headers = {'User-Agent': "Mozilla/5.0"}
    url = 'https://www.reddit.com'
    r = requests.get('{}/r/{}/hot.json?after={}'.format(url, subreddit, after)
                     headers=headers, allow_redirects=False)
    if r.status_code == 302:
        return None
    d = r.json()
    if d.get('data') is None:
        return None
    for post in d['data']['children']:
        title = post['data']['title']
        hot_list.append(title)
    if d['data']['after'] is None:
        return hot_list
    return recurse(subreddit, d['data']['after'], hot_list)
