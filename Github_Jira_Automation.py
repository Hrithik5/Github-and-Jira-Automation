# The URL, API_TOKEN, EMAIL can be saved in .env file also.

import requests
from requests.auth import HTTPBasicAuth
import json

url = "JIRA API"
API_TOKEN = "API TOKEN OF JIRA"
EMAIL = "EMAIL"

auth = HTTPBasicAuth(EMAIL, API_TOKEN)

headers = {"Accept": "application/json", "Content-Type": "application/json"}

payload = json.dumps(
    {
        "fields": {
            "description": {
                "content": [
                    {
                        "content": [{"text": "My first jira ticket", "type": "text"}],
                        "type": "paragraph",
                    }
                ],
                "type": "doc",
                "version": 1,
            },
            "project": {"key": "HC"},
            "issuetype": {"id": "10001"},
            "summary": "First JIRA Ticket",
        },
        "update": {},
    }
)

response = requests.request("POST", url, data=payload, headers=headers, auth=auth)

print(
    json.dumps(
        json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")
    )
)
