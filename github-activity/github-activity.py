import requests
import json
from  urllib.error import HTTPError, URLError
from urllib.request import urlopen, Request


username = str(input("github-activity "))
res = []

try:
    url = f"https://api.github.com/users/{username}/events"
    # url = "https://api.github.com/users/kamranahmedse/events"
    request = Request(url)
    with urlopen(request) as response:
        activities = json.loads(response.read().decode())
except HTTPError as error:
    if error.code == 404:
        print("User not found.")
    else:
        print(f"HTTP Error {error.code}: {error.reason}")
        exit(1)
except URLError as error:
    print(f"URL Error: {error.reason}")
except Exception as error:
    print(f"Error: {error}")


if len(activities) > 0:
    for activity in activities:
        # types.append(i["type"])
        repo = activity['repo']['name']

        if activity['type'] == 'CreateEvent':
            res.append(f"- created repository {repo}")
        elif activity['type'] == 'PushEvent':
            res.append(
                f"- pushed {len(activity['payload']['commits'])} commits to {repo}")
        elif activity['type'] == 'WatchEvent':
            res.append(f"- starred {repo}")
        elif activity['type'] == 'IssuesEvent':
            res.append(f"- opened issue on {repo}")
        elif activity['type'] == 'IssueCommentEvent':
            res.append(f"- commented on issue on {repo}")
        elif activity['type'] == 'ForkEvent':
            res.append(f"- forked {repo}")
        elif activity['type'] == 'PublicEvent':
            res.append(f"- made repository {repo} public")
        elif activity['type'] == 'PullRequestEvent':
            res.append(f"- opened pull request on {repo}")
        else:
            res.append(f"- did something on {repo}")
else:
    print("No activity found.")

print("\n".join(res))