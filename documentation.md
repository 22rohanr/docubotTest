## API Endpoints:

### 1. Get Commit Information:
- **Endpoint:** `GET /repos/{owner}/{repo}/commits/{ref}`
- **Description:** Retrieves commit details, including file changes, for a specific repository and reference.
- **Parameters:**
 - `owner`: The owner of the repository. (string)
 - `repo`: The repository name. (string)
 - `ref`: The commit reference (e.g., a branch name or SHA). (string)
- **Response:** Returns a commit object containing file changes and other commit metadata.

### 2. Update Documentation:
- **Endpoint:** `POST /document`
- **Description:** Updates documentation based on provided file changes.
- **Request Body:**
 - `repo_owner`: The owner of the repository. (string)
 - `repo`: The repository name. (string)
 - `files_changed`: A list of changed files. (array of strings)
 - `github_token`: The GitHub authentication token. (string)
- **Response:** Returns a JSON object with an `updated_doc` field containing the updated documentation content.

## New Classes:

### 1. GitHubActionsWorkflow:
- **Description:** Represents a GitHub Actions workflow for documentation generation.
- **Attributes:**
 - `steps`: A list of workflow steps. (array)
- **Methods:**
 - `checkout_code()`: Checks out the repository code.
 - `get_changed_files()`: Retrieves a list of changed files using the GitHub API.
 - `read_changed_files()`: Reads the list of changed files from a file.
 - `call_api()`: Calls the documentation update API with the changed files.
 - `update_documentation()`: Updates the documentation file with the API response.
 - `commit_and_push()`: Commits and pushes changes to the documentation file if updated.
