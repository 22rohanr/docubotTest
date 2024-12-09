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
