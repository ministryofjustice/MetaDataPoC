import requests
import base64
import json


class GitHubMetadata:
    def __init__(self, org, repo, file_path="METADATA.json", token=None):
        self.org = org
        self.repo = repo
        self.token = token
        self.headers = {'Accept': 'application/vnd.github.v3+json'}
        if self.token and token != None:
            self.headers['Authorization'] = f'token {self.token}'
        self.file_path = file_path
        self._load_data()

    def _load_data(self):
        """Load data from the METADATA.json file on GitHub."""
        response = requests.get(
            f'https://api.github.com/repos/{self.org}/{self.repo}/contents/{self.file_path}', headers=self.headers)
        if response.status_code != 200:
            print(response)
            raise Exception("Failed to fetch METADATA.json!")
        data = response.json()
        encoded_content = data['content']
        decoded_content = base64.b64decode(encoded_content).decode('utf-8')
        self.data = json.loads(decoded_content)

    def get(self, key, default=None):
        """Retrieve metadata by key."""
        return self.data.get(key, default)

    @property
    def team(self):
        return self.get('team')

    @property
    def email(self):
        return self.get('email')

    @property
    def slack(self):
        return self.get('slack')

    @property
    def support(self):
        return self.get('support')

    @property
    def documentation(self):
        return self.get('documentation')

    @property
    def contact(self):
        return {
            "email": self.email,
            "slack": self.slack,
            "support": self.support
        }

    @property
    def all(self):
        return self.data.items()

    def display(self):
        """Prints the entire metadata content."""
        for key, value in self.all:
            print(f"{key}: {value}")
