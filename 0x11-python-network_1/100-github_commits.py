#!/usr/bin/python3
"""
    Module to implement a python script that prints
    the latest 10 commits from given repository and
    user
"""
import requests
import sys


def get_commits(repo, owner):
    """Prints the latest 10 commits from given repo"""
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()[:10]
        for commit in commits:
            sha = commit['sha']
            author = commit['commit']['author']['name']
            print("{}: {}".format(sha, author))
        else:
            print("Error: {}".format(response.status_code))


if __name__ == "__main__":
    if len(sys.argv) == 3:
        repo_name = sys.argv[1]
        owner_name = sys.argv[2]
        get_commits(repo_name, owner_name)
    else:
        print("Usage: <filename> <repository_name> <owner_name>")
