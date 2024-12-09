## API Endpoints:

### 1. Update an Existing Car:
- Endpoint: `/cars/<car_id>`
- Method: `PUT`
- Parameters:
 - `car_id` (int): The ID of the car to be updated.
- Request Body:
 - `updates` (JSON): A JSON object containing the fields to be updated, e.g., `{"color": "Blue", "owner": "Bob"}`.
- Response:
 - Returns a JSON object with the updated car information.
 - Success Response: `{"message": "Car updated", "car": {"id": <car_id>, "make": "<make>", "model": "<model>", "year": <year>, "color": "<updated_color>", "owner": "<updated_owner>"}}`.
 - Error Response: `{"error": "Car not found"}`.
- Status Codes:
 - 200 OK: Update successful.
 - 404 Not Found: Car with the provided ID does not exist.

### 2. Get Car by ID:
- Endpoint: `/cars/<car_id>`
- Method: `GET`
- Parameters:
 - `car_id` (int): The ID of the car to retrieve.
- Response:
 - Returns a JSON object with the car details.
 - Success Response: `{"car": {"id": <car_id>, "make": "<make>", "model": "<model>", "year": <year>, "color": "<color>", "owner": "<owner>"}}`.
 - Error Response: `{"error": "Car not found"}`.
- Status Codes:
 - 200 OK: Car found and returned.
 - 404 Not Found: Car with the provided ID does not exist.

### 3. Delete a Car:
- Endpoint: `/cars/<car_id>`
- Method: `DELETE`
- Parameters:
 - `car_id` (int): The ID of the car to be deleted.
- Response:
 - Returns a JSON object confirming the deletion.
 - Success Response: `{"message": "Car deleted", "car": {"id": <car_id>, "make": "<make>", "model": "<model>", "year": <year>}}`.
 - Error Response: `{"error": "Car not found"}`.
- Status Codes:
 - 200 OK: Car successfully deleted.
 - 404 Not Found: Car with the provided ID does not exist.

### 4. Add a New Car:
- Endpoint: `/cars`
- Method: `POST`
- Request Body:
 - `new_car` (JSON): A JSON object containing the new car details, e.g., `{"make": "Honda", "model": "Civic", "year": 2023, "color": "Silver", "owner": "Charlie"}`.
- Response:
 - Returns a JSON object with a confirmation message and the added car details.
 - Success Response: `{"message": "Car added", "car": {"id": <new_id>, "make": "<make>", "model": "<model>", "year": <year>, "color": "<color>", "owner": "<owner>"}}`.
 - Error Response: `{"error": "Invalid input. 'make', 'model', and 'year' fields are required."}`.
- Status Codes:
 - 201 Created: Car successfully added.
 - 400 Bad Request: Invalid input or missing required fields.
