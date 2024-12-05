## API Endpoints:

### 1. Update an Existing Car:
- Endpoint: `/cars/<car_id>`
- Method: `PUT`
- Parameters:
 - `car_id` (int): The unique identifier of the car to be updated.
- Request Body:
 - `updates` (JSON): A JSON object containing key-value pairs of fields to be updated. For example: `{"color": "Red", "owner": "Alice"}`.
- Response:
 - Returns a JSON object with the updated car details, including any modified fields.
 - Success Response: `{"message": "Car updated", "car": {"id": 1, "make": "Toyota", "model": "Camry", "year": 2022, "color": "Red", "owner": "Alice"}}`
 - Error Response: `{"error": "Car not found"}`
- Status Codes:
 - 200 OK: Successful update.
 - 404 Not Found: If the provided `car_id` is not found in the database.

### 2. Get a Car by ID:
- Endpoint: `/cars/<car_id>`
- Method: `GET`
- Parameters:
 - `car_id` (int): The ID of the car to retrieve.
- Response:
 - Returns a JSON object with the car details.
 - Success Response: `{"car": {"id": 1, "make": "Toyota", "model": "Camry", "year": 2022}}`.
 - Error Response: `{"error": "Car not found"}`.
- Status Codes:
 - 200 OK: Car found and returned.
 - 404 Not Found: If the requested `car_id` is not in the database.

### 3. Delete a Car:
- Endpoint: `/cars/<car_id>`
- Method: `DELETE`
- Parameters:
 - `car_id` (int): The ID of the car to be deleted.
- Response:
 - Returns a JSON object confirming the deletion and including the deleted car details.
 - Success Response: `{"message": "Car deleted", "car": {"id": 1, "make": "Toyota", "model": "Camry", "year": 2022}}`.
 - Error Response: `{"error": "Car not found"}`.
- Status Codes:
 - 200 OK: Car successfully deleted.
 - 404 Not Found: If the specified `car_id` does not exist.

### 4. Add a New Car:
- Endpoint: `/cars`
- Method: `POST`
- Request Body:
 - `new_car` (JSON): A JSON object containing the details of the new car, including "make", "model", and "year" fields. For example: `{"make": "Honda", "model": "Civic", "year": 2023, "color": "Blue"}`.
- Response:
 - Returns a JSON object with a confirmation message and the added car details.
 - Success Response: `{"message": "Car added", "car": {"id": 2, "make": "Honda", "model": "Civic", "year": 2023, "color": "Blue"}}`.
 - Error Response: `{"error": "Invalid input. 'make', 'model', and 'year' fields are required."}`.
- Status Codes:
 - 201 Created: New car added successfully.
 - 400 Bad Request: If the request body is missing required fields.
