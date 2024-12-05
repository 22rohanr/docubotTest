## API Endpoints:

### 1. Update an Existing Car:
- Endpoint: `/cars/<car_id>`
- Method: `PUT`
- Parameters:
 - `car_id` (int): The ID of the car to be updated.
- Request Body:
 - `updates` (JSON): JSON object containing the fields to update.
- Response:
 - Returns a JSON object with updated car details on success, or an error message.
 - Status Codes: 200 (OK) for successful updates, 404 (Not Found) if the car ID is invalid.
