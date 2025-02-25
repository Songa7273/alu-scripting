#!/usr/bin/python3
"""
This module contains functions for querying the Reddit API.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None: Prints the titles or None if the subreddit is invalid.
    """
    # Reddit API URL for hot posts in a subreddit
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    
    # Set a custom User-Agent to avoid too many requests error
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    # Set parameters to limit to 10 posts and prevent following redirects
    params = {
        'limit': 10
    }
    
    # Make the request to the Reddit API
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract and print the titles of the first 10 hot posts
        posts = data.get('data', {}).get('children', [])
        
        for post in posts:
            print(post.get('data', {}).get('title'))
    else:
        # If not a valid subreddit, print None
        print(None)
