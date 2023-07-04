from github import Github
import os

TOKEN = os.getenv('GH_TOKEN')
# BRANCH_NAME = os.getenv('BRANCH_NAME')
REPOSITORY_URL = "PiotrBrzostowski/B"

g = Github(TOKEN)

def auto_merge():
    repo = g.get_repo(REPOSITORY_URL)
    pull_request = repo.get_pull(0)
    print(pull_request.title)

auto_merge()
