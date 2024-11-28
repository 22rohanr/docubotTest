## API Endpoints:

### 1. Update an Existing Car:
- Endpoint: `/cars/<int:car_id>`
- Method: `PUT`
- Parameters:
 - `car_id` (int): The unique identifier of the car to be updated.
- Request Body:
 - `updates` (JSON): A JSON object containing the fields to update in the car record.
- Response:
 - Returns a JSON object with a success message and the updated car details, or an error message if the car is not found.
 - Status Codes: 200 (OK) for successful updates, 404 (Not Found) if the car ID is not found.

### 2. Get a Car by ID:
- Endpoint: `/cars/<int:car_id>`
- Method: `GET`
- Parameters:
 - `car_id` (int): The unique identifier of the car to retrieve.
- Response:
 - Returns a JSON object containing the car details, or an error message if the car is not found.
 - Status Codes: 200 (OK) if the car is found, 404 (Not Found) otherwise.

### 3. Delete a Car:
- Endpoint: `/cars/<int:car_id>`
- Method: `DELETE`
- Parameters:
 - `car_id` (int): The unique identifier of the car to be deleted.
- Response:
 - Returns a JSON object with a success message and the deleted car details, or an error message.
 - Status Codes: 200 (OK) if deleted, 404 (Not Found) if the car ID is not found.

### 4. Get All Cars:
- Endpoint: `/cars`
- Method: `GET`
- Response:
 - Returns a JSON object containing a list of all cars in the database.
 - Status Code: 200 (OK)

### 5. Add a New Car:
- Endpoint: `/cars`
- Method: `POST`
- Request Body:
 - `new_car` (JSON): A JSON object containing the new car details, including 'make', 'model', and 'year' fields.
- Response:
 - Returns a JSON object with a success message and the added car's details, or an error message for invalid input.
 - Status Codes: 201 (Created) for successful addition, 400 (Bad Request) for invalid input.

### 6. Get Cars by Year:
- Endpoint: `/cars/year/<int:year>`
- Method: `GET`
- Parameters:
 - `year` (int): The year to filter cars by.
- Response:
 - Returns a JSON object with a list of cars matching the specified year, or an error message if no cars match.
 - Status Code: 200 (OK)
