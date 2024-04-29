import requests
import os

def set_status_bypass():
    # Fetch labels from the GitHub API
    api_url = f"https://api.github.com/repos/{os.environ['REPO']}/pulls/{os.environ['PR_NUMBER']}/labels"
    headers = {"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"}
    response = requests.get(api_url, headers=headers)
    labels = [label['name'] for label in response.json()]

    # Check if specific label is present
    if 'skip-codecov' in labels:
        # Construct the URL to update the status
        status_url = f"https://api.github.com/repos/{os.environ['REPO']}/statuses/{os.environ['GITHUB_SHA']}"
        # Define the data for the status update
        data = {
            "state": "success",
            "context": os.environ['CODECOV_CONTEXT'],
            "description": "Codecov check bypassed by label",
            "target_url": ""  # Optional: URL to more details or explanation
        }
        # Make the POST request to set the status
        requests.post(status_url, headers=headers, json=data)

if __name__ == "__main__":
    set_status_bypass()
