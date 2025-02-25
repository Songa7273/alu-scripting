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
        'User-Agent': 'linux:alu-script:v1.0.0 (by /u/Songa7273)'
    }

    # Make the request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract and print the titles of the first 10 hot posts
        posts = data.get('data', {}).get('children', [])

        for i, post in enumerate(posts):
            if i >= 10:
                break
            print(post.get('data', {}).get('title'))
    else:
        # If not a valid subreddit, print None
        print(None)
