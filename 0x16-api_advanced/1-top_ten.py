#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a given subreddit
    using the Reddit API.

    Args:
        subreddit (str): The name of the subreddit to query.
    """
    # Reddit API endpoint URL for hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    # Custom User-Agent to avoid Too Many Requests error
    headers = {"User-Agent": "Custom User Agent"}

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad requests

        # Parse the JSON response and retrieve the titles of first 10 posts
        data = response.json()
        posts = data["data"]["children"][:10]
        for post in posts:
            print(post["data"]["title"])
    except requests.HTTPError as err:
        if err.response.status_code == 404:
            # If the subreddit is not found, print None
            print("None")
        else:
            # Handle other HTTP errors by printing the status code and None
            print(f"Error: {err.response.status_code}")
            print("None")
