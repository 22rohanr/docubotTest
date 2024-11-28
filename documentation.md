# GitHub Action: Combined Workflow

## Overview
This GitHub Action workflow automates the process of updating documentation based on changes made to the repository. It is triggered by both push events to any branch and pull requests to the main branch. The workflow fetches the list of changed files, sends this information to an API, and updates the documentation with the API's response.

## Workflow Structure

### 1. Checkout Code
- **Action:** `actions/checkout@v2`
- **Description:** Checks out the repository code, allowing access to the files and commit history.

### 2. Get Changed Files
- **Action:** `actions/github-script@v6`
- **Description:** Retrieves the list of changed files in the current commit using a GitHub Script.
 - **Parameters:**
 - `script`: A JavaScript code snippet that fetches the commit SHA, retrieves the list of changed files, and logs/saves the file names.

### 3. Read Changed Files
- **Description:** Reads the list of changed files from the file created in the previous step.

### 4. Call the API
- **Description:** Constructs a JSON payload containing the repository owner, repository name, list of changed files, and the GitHub token. The payload is sent to a specified API endpoint via a cURL request.
 - **Parameters:**
 - `repo_owner`: The owner of the repository.
 - `repo`: The name of the repository.
 - `files_changed`: A JSON array of changed file paths.
 - `github_token`: The GitHub token for authentication.

### 5. Update Documentation
- **Description:** Saves the API response to a file named `response.txt`.

### 6. Commit and Push Changes
- **Description:** Checks if the documentation file (`documentation.md`) has been updated. If changes are detected, the file is committed and pushed to the repository.
 - **Parameters:**
 - `env.GITHUB_TOKEN`: The GitHub token for authentication and committing changes.
