#!/usr/bin/python3
"""
Module to query the Reddit API and print the titles of the first 10 hot posts
"""
import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts 
    of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
    
    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "my_reddit_script/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if subreddit exists
    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            print(post["data"]["title"])
    except KeyError:
        print(None)

