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

### 2. Retrieve a Car by ID:
- Endpoint: `/cars/<car_id>`
- Method: `GET`
- Parameters:
 - `car_id` (int): Unique identifier of the car.
- Response:
 - Returns a JSON object with car details on success, or an error message.
 - Status Codes: 200 (OK) if found, 404 (Not Found) otherwise.

### 3. Delete a Car:
- Endpoint: `/cars/<car_id>`
- Method: `DELETE`
- Parameters:
 - `car_id` (int): ID of the car to delete.
- Response:
 - Returns a success message and deleted car details on success, or an error message.
 - Status Codes: 200 (OK) if deleted, 404 (Not Found) for invalid car ID.

### 4. Retrieve All Cars:
- Endpoint: `/cars`
- Method: `GET`
- Response:
 - Returns a JSON list of all cars.
 - Status Code: 200 (OK)

### 5. Add a New Car:
- Endpoint: `/cars`
- Method: `POST`
- Request Body:
 - `new_car` (JSON): JSON object with 'make', 'model', and 'year' fields.
- Response:
 - Returns a success message and added car details on success, or an error message.
 - Status Codes: 201 (Created) for successful addition, 400 (Bad Request) for invalid input.

### 6. Filter Cars by Year:
- Endpoint: `/cars/year/<year>`
- Method: `GET`
- Parameters:
 - `year` (int): The year to filter cars.
- Response:
 - Returns a JSON list of matching cars, or an error message.
 - Status Code: 200 (OK)
