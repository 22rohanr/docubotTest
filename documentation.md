## GitHub Action: Combined Workflow

### API Endpoints:
- **Endpoint:** `https://4wybp1tvb2.execute-api.us-east-2.amazonaws.com/document`
 **Method:** POST
 **Description:** Sends a JSON payload to the API to request updated documentation.
 **Parameters:**
 - `repo_owner`: String. The owner of the repository.
 - `repo`: String. The name of the repository.
 - `files_changed`: JSON array. A list of changed file paths.
 - `github_token`: String. The GitHub authentication token.

## New Classes:

### `ChangedFiles` Class:
- **Purpose:** Represents a collection of changed files and provides methods to interact with the list.
- **Methods:**
 - `writeFile()`: Writes the list of changed files to a file.
 - `getFiles()`: Returns the list of changed files.

### `APIRequest` Class:
- **Purpose:** Handles the API request and response processing.
- **Methods:**
 - `sendRequest()`: Sends the JSON payload to the API and returns the response.
 - `processResponse()`: Parses the API response and extracts the updated documentation content.

### `DocumentationUpdater` Class:
- **Purpose:** Coordinates the documentation update process.
- **Methods:**
 - `updateDocumentation()`: Updates the documentation file with the API response.
 - `commitAndPush()`: Commits and pushes changes to the repository if the documentation is updated.
