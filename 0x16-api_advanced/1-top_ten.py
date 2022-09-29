#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """Prints the titles."""
    headers = {'User-Agent': "Mozilla/5.0"}
    url = 'https://www.reddit.com'
    r = requests.get(f'{url}/r/{subreddit}/hot.json?limit=10',
                     headers=headers, allow_redirects=False)

    if r.status_code == 302:
        print('None')
        return
    d = r.json()
    if d.get('data') is None:
        print('None')
        return
    for post in d['data']['children']:
        title = post['data']['title']
        print(title)
