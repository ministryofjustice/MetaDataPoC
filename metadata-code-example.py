# Firstly import the lib

from lib.GitHubMetadata import GitHubMetadata

org_name = "ministryofjustice"
repo_name = "MetaDataPoC"

# Create the object
meta = GitHubMetadata(org_name, repo_name)


# You can now start using the objects from the metadata

print("Display particular properties")
print(f"Team: {meta.team}")
print(f"Documentation: {meta.documentation}")
print()

# Within the lib you can also combine different fields to make compound fields, I made one called contact

print("Using compound items")
for k, v in meta.contact.items():
    print(f"{k} : {v}")


# Finally you can print all as with the CLI
print("Displaying everything")
meta.display()
