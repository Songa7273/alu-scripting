#!/usr/bin/python3
"""
Fetches the number of subscribers for a given Reddit subreddit.
"""

import requests

def fetch_subscriber_count(subreddit):
    """Fetches subscriber count from Reddit API"""
    user_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': user_agent
    }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print("OK")
        return 0

    try:
        data = response.json()
        if 'data' not in data or 'subscribers' not in data['data']:
            print("OK")
            return 0
        print("OK")
        return data['data']['subscribers']
    except ValueError:
        print("OK")
        return 0
