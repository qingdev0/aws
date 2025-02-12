"""
GitHub service module for interacting with GitHub API.
"""

import json
import os
from typing import Any, Dict

import requests
from aws_lambda_powertools import Logger

logger = Logger()


def trigger_workflow(message: str) -> None:
    """
    Trigger GitHub Actions workflow using repository dispatch event.
    """

    github_token = os.environ["GITHUB_TOKEN"]
    owner = os.environ["GITHUB_OWNER"]
    repo = os.environ["GITHUB_REPO"]
    workflow_name = os.environ["WORKFLOW_NAME"]

    url = f"https://api.github.com/repos/{owner}/{repo}/dispatches"

    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json",
    }

    payload: Dict[str, Any] = {
        "event_type": workflow_name,
        "client_payload": {"message": message},
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=30)
    response.raise_for_status()

    logger.info(
        "Successfully triggered GitHub workflow",
        status_code=response.status_code,
        workflow=workflow_name,
    )
