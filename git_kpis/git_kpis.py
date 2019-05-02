# coding=utf-8
"""
Calculate lead time metrics from GitHub

Requires python 3.6+, requests. 
** You are strongly recommended to work in a python virtualenv or conda environment **
"""

import sys
import logging
import argparse
import re
import datetime

from pprint import pprint

from .logging import get_logger
from .github_client import GitHubClient

_logger = get_logger(__name__)


def parse_args(args):
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-B", "--base", type=str, required=True, help="The base tag version")
    parser.add_argument("-H", "--head", type=str, required=True, help="The head tag version")
    parser.add_argument(
        "-R", "--repository", type=str, required=True, help="The name of the repository. For example, PyGithub/PyGithub"
    )
    parser.add_argument(
        "-K", "--key", type=str, required=True, help="The name of the project key to search for in commit messages")

    parser.add_argument("--debug", action="store_true", default=False)
    parsed = parser.parse_args(args)

    if parsed.debug:
        _logger.setLevel(logging.DEBUG)

    return parsed


def main():
    args = parse_args(sys.argv[1:])
    _logger.info(f"repository: {args.repository}")
    _logger.info(f"base: {args.base}")
    _logger.info(f"head: {args.head}")
    _logger.info(f"debug: {args.debug}")

    client = GitHubClient()

    base_version = args.base
    head_version = args.head
    repository = args.repository
    key = args.key

    tag_created_at = client.get_release(repository, head_version).created_at

    comparison = client.get_comparison(repository, base_version, head_version)
    differences = []
    for commit in comparison.commits:
        git_commit = commit.commit
        if re.search(r".*" + key + ".*", git_commit.message, re.I):
            difference = tag_created_at - git_commit.author.date
            # We want to filter out commit date == tag date
            if difference > datetime.timedelta(0):
                differences.append(difference)

    print()
    print("Lead time: ", sum(differences, datetime.timedelta()) / len(differences))
    print()


if __name__ == "__main__":
    main()
