import requests
import os

def set_status_bypass():
    # Fetch labels from the GitHub API
    api_url = f"https://api.github.com/repos/{os.environ['REPO']}/pulls/{os.environ['PR_NUMBER']}/labels"
    headers = {"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"}
    response = requests.get(api_url, headers=headers)
    
    # Check if the response was successful
    if response.status_code == 200:
        try:
            labels = [label['name'] for label in response.json()]
            print("Labels found:", labels)
        except (TypeError, KeyError) as e:
            print("Error parsing labels:", e)
            print("Response content:", response.text)
            return  # Exit if error in parsing labels

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
            result = requests.post(status_url, headers=headers, json=data)
            print("Status update response:", result.status_code, result.text)
    else:
        print("Failed to fetch labels:", response.status_code, response.text)

if __name__ == "__main__":
    set_status_bypass()
