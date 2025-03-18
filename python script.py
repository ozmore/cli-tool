import os
import requests
import argparse

# GitHub API Token (Set this as an environment variable for security)
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USER = "your-github-username"  # Replace with your GitHub username
API_URL = "https://api.github.com"

headers = {"Authorization": f"token {GITHUB_TOKEN}"}

def create_repo(repo_name, private=True):
    url = f"{API_URL}/user/repos"
    data = {"name": repo_name, "private": private}
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully!")
    else:
        print("Error:", response.json())

def list_repos():
    url = f"{API_URL}/user/repos"
    response = requests.get(url, headers=headers)
    repos = response.json()
    for repo in repos:
        print(repo["name"], "-", repo["html_url"])

def delete_repo(repo_name):
    url = f"{API_URL}/repos/{GITHUB_USER}/{repo_name}"
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"Repository '{repo_name}' deleted successfully!")
    else:
        print("Error:", response.json())

def main():
    parser = argparse.ArgumentParser(description="GitHub Repo Manager CLI")
    parser.add_argument("action", choices=["create", "list", "delete"], help="Action to perform")
    parser.add_argument("--name", help="Repository name (required for create & delete)")
    args = parser.parse_args()

    if args.action == "create" and args.name:
        create_repo(args.name)
    elif args.action == "list":
        list_repos()
    elif args.action == "delete" and args.name:
        delete_repo(args.name)
    else:
        print("Invalid arguments! Use --help for usage info.")

if __name__ == "__main__":
    main()
