#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively count the occurrences of given keywords in the titles of hot
    articles from a subreddit using the Reddit API.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): List of keywords to count occurrences for.
        after (str): Reddit API parameter indicating the starting post ID
        for pagination.
        counts (dict): Dictionary to store keyword counts.
    Returns:
        dict: Dictionary containing keyword counts.
    """
    if counts is None:
        counts = {}

    # Reddit API endpoint URL for hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    # Custom User-Agent to avoid Too Many Requests error
    headers = {"User-Agent": "Custom User Agent"}
    # Reddit API parameters for pagination and avoiding duplicates
    params = {"after": after}

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise HTTPError for bad requests

        # Parse the JSON response
        data = response.json()
        posts = data["data"]["children"]

        # Count occurrences of keywords in post titles
        for post in posts:
            title = post["data"]["title"].lower()
            for word in word_list:
                # Check for whole words (not substrings)
                if f" {word.lower()} " in f" {title} ":
                    counts[word] = counts.get(word, 0) + 1

        # Get the ID of the last post for pagination
        after = data["data"]["after"]

        # Recursive call with the next page of posts
        if after:
            return count_words(subreddit, word_list, after, counts)
        else:
            # Print the sorted keyword counts in descending order
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    except requests.HTTPError as err:
        if err.response.status_code == 404:
            # If the subreddit is not found, print nothing
            pass
        else:
            # Handle other HTTP errors by printing the status code and nothing
            print(f"Error: {err.response.status_code}")
