#!/usr/bin/env python3
"""
List Changed Roles

This script fetches the main branch, computes the diff between origin/main and HEAD,
and prints a JSON array of roles (directories under "roles/") that have changed.
"""

import os
import subprocess
import json
import sys

def run_command(command, allow_failure=False):
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if not allow_failure and result.returncode != 0:
        sys.exit(result.returncode)
    return result.stdout.strip()

def main():
    # Fetch the main branch
    run_command(["git", "fetch", "origin", "main"])

    # Get the list of changed files between origin/main and HEAD
    diff_output = run_command(["git", "diff", "--name-only", "origin/main...HEAD"], allow_failure=True)
    changed_files = diff_output.splitlines() if diff_output else []

    # Identify roles changed (directories under roles/)
    roles = {file.split('/')[1] for file in changed_files if file.startswith("roles/") and len(file.split('/')) >= 2}
    roles_list = sorted(roles)

    # Print the JSON array to standard output
    print(json.dumps(roles_list))

if __name__ == '__main__':
    main()
