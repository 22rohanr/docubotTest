# GitHub Action: Combined Workflow

## Overview
This GitHub Action workflow is designed to automate the process of updating documentation based on changes made to the repository. It utilizes a custom API to generate documentation for modified files and integrates with GitHub's pull request and push events.

## Triggers
- **Push Event:** The workflow is triggered when a push is made to any branch in the repository.
- **Pull Request Event:** It also activates when a pull request is opened against the 'main' branch.

## Jobs
### Documentation Job
- **Runs on:** Ubuntu-latest runner.
- **Steps:**
 1. **Checkout Code:** Checks out the repository code.
 2. **Get Changed Files:** Uses a GitHub script to retrieve a list of changed files in the commit and saves it to a file named `changedFiles.txt`.
 3. **Read Changed Files:** Reads the `changedFiles.txt` file and stores the list of changed files in a variable.
 4. **Call the API:** Constructs a JSON payload with the changed files and other metadata, then sends a request to the specified API endpoint (`https://ff7g7qlsji.execute-api.us-east-2.amazonaws.com/document`).
 5. **Update Documentation:** Saves the API response containing the updated documentation to a file named `response.txt`.
 6. **Commit and Push Changes:** Commits and pushes the updated documentation to the repository if changes are detected.

## API Endpoint
### Endpoint: https://ff7g7qlsji.execute-api.us-east-2.amazonaws.com/document
- **Method:** POST
- **Request Body:**
 - `repo_owner` (string): The owner of the repository.
 - `repo` (string): The name of the repository.
 - `files_changed` (array of strings): A list of changed file paths.
 - `github_token` (string): The GitHub authentication token.
- **Response:** Returns a JSON object containing the updated documentation content in a field named `updated_doc`.

## Environment Variables
- `GITHUB_TOKEN`: A GitHub-provided token for authentication, used for committing and pushing changes.
