import argparse

from lib.GitHubMetadata import GitHubMetadata


def main():
    parser = argparse.ArgumentParser(
        description="Fetch metadata for a given GitHub repository.")
    parser.add_argument('org_name', type=str, help='GitHub organization name.')
    parser.add_argument('repo_name', type=str,
                        help='GitHub repository name within the organization.')
    parser.add_argument('action', type=str, choices=["display", "team", "email", "support",
                        "slack", "documentation", "contact"], help='Value you want.')  # Add this line
    parser.add_argument('--token', type=str, default=None,
                        help='Optional GitHub API token for authentication.')

    args = parser.parse_args()
    meta = GitHubMetadata(org=args.org_name,
                          repo=args.repo_name,
                          token=args.token)

    result = getattr(
        meta, args.action, f"Method/Property '{args.action}' not found in GitHubMetadata class.")
    if callable(result):
        result()
    else:
        print(result)


if __name__ == '__main__':
    main()
