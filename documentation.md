## API Endpoints:

### 1. Update an Existing Car:
- Endpoint: `/cars/<int:car_id>`
- Method: `PUT`
- Parameters:
 - `car_id` (int): The unique identifier of the car to be updated.
- Request Body:
 - `updates` (JSON): A dictionary containing the fields to be updated in the car record.
- Response:
 - Returns a JSON object with a success message and the updated car details, or an error message if the car is not found.
 - Status Codes: 200 (OK) if updated successfully, 404 (Not Found) if the car ID is not found.

### 2. Get a Car by ID:
- Endpoint: `/cars/<int:car_id>`
- Method: `GET`
- Parameters:
 - `car_id` (int): The unique identifier of the car to retrieve.
- Response:
 - Returns a JSON object with the car details, or an error message if the car is not found.
 - Status Codes: 200 (OK) if the car is found, 404 (Not Found) if the car ID is not found.

### 3. Delete a Car:
- Endpoint: `/cars/<int:car_id>`
- Method: `DELETE`
- Parameters:
 - `car_id` (int): The unique identifier of the car to be deleted.
- Response:
 - Returns a JSON object with a success message and the deleted car details, or an error message if the car is not found.
 - Status Codes: 200 (OK) if deleted successfully, 404 (Not Found) if the car ID is not found.

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
 - `new_car` (JSON): A dictionary containing the details of the new car, including 'make', 'model', and 'year' fields.
- Response:
 - Returns a JSON object with a success message and the added car details, or an error message if the input is invalid.
 - Status Codes: 201 (Created) if the car is added successfully, 400 (Bad Request) if the input is invalid.

### 6. Search Cars by Attribute:
- Endpoint: `/cars/search`
- Method: `GET`
- Query Parameters:
 - `attribute` (str): The attribute to search for (e.g., 'make', 'model', 'year').
 - `value` (str): The value to match against the specified attribute.
- Response:
 - Returns a JSON object with a list of matching cars, or an error message if the query parameters are missing.
 - Status Codes: 200 (OK) if the search is successful, 400 (Bad Request) if required query parameters are missing.
