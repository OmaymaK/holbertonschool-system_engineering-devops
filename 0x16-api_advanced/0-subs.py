#!/usr/bin/python3
"""Returns the number of subscribers."""
import requests


def number_of_subscribers(subreddit):
    """Get number of subs."""
    headers = {'User-Agent': "Mozilla/5.0"}
    r = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json',
                     headers=headers, allow_redirects=False)
    if r.status_code == 302:
        return 0
    d = r.json()
    try:
        s = d['data']['subscribers']
    except Exception:
        return 0
    return s
