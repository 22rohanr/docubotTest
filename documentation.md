## API Endpoints:

### 1. Update an Existing Car:
- Endpoint: `/cars/<int:car_id>`
- Method: `PUT`
- Parameters:
 - `car_id` (int): The ID of the car to be updated.
 - `request.json` (dict): A JSON object containing the fields to update. This should include the new values for the car's attributes.
- Response: Returns a JSON response with a status message and the updated car data, or an error message with a 404 status code if the car is not found.

### 2. Get a Car by ID:
- Endpoint: `/cars/<int:car_id>`
- Method: `GET`
- Parameters:
 - `car_id` (int): The unique identifier of the car to retrieve.
- Response: Returns a JSON object containing the car data with a 200 status code, or an error message with a 404 status code if the car is not found.

### 3. Delete a Car:
- Endpoint: `/cars/<int:car_id>`
- Method: `DELETE`
- Parameters:
 - `car_id` (int): The ID of the car to be deleted.
- Response: Returns a JSON response with a success message and the deleted car data, or an error message with a 404 status code if the car is not found.

### 4. Get All Cars:
- Endpoint: `/cars`
- Method: `GET`
- Response: Returns a JSON object containing a list of all cars in the database with a 200 status code.

### 5. Add a New Car:
- Endpoint: `/cars`
- Method: `POST`
- Parameters:
 - `request.json` (dict): A JSON object containing the new car data. This should include 'make', 'model', and 'year' fields.
- Response: Returns a JSON response with a success message and the added car data, or an error message with a 400 status code if the input is invalid.

### 6. Search Cars by Attribute:
- Endpoint: `/cars/search`
- Method: `GET`
- Parameters:
 - `attribute` (str): The attribute to search for (e.g., 'make', 'model', 'year').
 - `value` (str): The value to match against the attribute.
- Response: Returns a JSON object containing a list of cars that match the given attribute and value, with a 200 status code. If the query parameters are missing, it returns a 400 status code with an error message.
