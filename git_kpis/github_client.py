import json
from github import Github


class GitHubClient:
    def __init__(self):
        self.github = self._get_github()

    @staticmethod
    def _get_github():
        with open("secrets.json") as f:
            data = json.load(f)
        session_token = data["accessToken"]
        return Github(session_token)

    def get_comparison(self, repository_name, base_tag, head_tag):
        github = self._get_github()
        comparison = github.get_repo(repository_name).compare(base_tag, head_tag)
        return comparison

    def get_release(self, repository_name, tag):
        github = self._get_github()
        return github.get_repo(repository_name).get_release(tag)
