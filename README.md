# MetaDataPoC

Repo for quick GitHub Repo Meta Data - how we could use it

## Demo
[![asciicast](https://asciinema.org/a/4hrDhBSbzLWoRzRgx2IGaO6oy.svg)](https://asciinema.org/a/4hrDhBSbzLWoRzRgx2IGaO6oy)

## Snippets

### Bash

```
# All data
curl -s https://raw.githubusercontent.com/ministryofjustice/MetaDataPoC/main/METADATA.json | jq

# Support
curl -s https://raw.githubusercontent.com/ministryofjustice/MetaDataPoC/main/METADATA.json | jq '.support'

# Team + Email
curl -s https://raw.githubusercontent.com/ministryofjustice/MetaDataPoC/main/METADATA.json | jq '.team + ": " + .email'
```

### CLI

```
# Usage
python3 metadata-cli-example.py ministryofjustice MetaDataPoC -h

# Team
python3 metadata-cli-example.py ministryofjustice MetaDataPoC team

# Email
python3 metadata-cli-example.py ministryofjustice MetaDataPoC email

# All data
python3 metadata-cli-example.py ministryofjustice MetaDataPoC display
```

### Python

```
from lib.GitHubMetadata import GitHubMetadata

org_name = "ministryofjustice"
repo_name = "MetaDataPoC"

meta = GitHubMetadata(org_name, repo_name)

print("Display particular property")
print(f"Team: {meta.team}")
print(f"Documentation: {meta.documentation}")
print()

print("Using compound items")
for k, v in meta.contact.items():
    print(f"{k} : {v}")
print()

print("Display all")
meta.display()
```
