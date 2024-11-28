## API Endpoints:

### 1. Update an Existing Car:
- Endpoint: `/cars/<int:car_id>`
- Method: `PUT`
- Parameters:
 - `car_id` (int): The unique identifier of the car to be updated.
 - `request.json` (dict): A dictionary containing the updates to be made to the car's data.
- Response: Returns a JSON object with a success message and the updated car data, or an error message if the car is not found.

### 2. Get a Car by ID:
- Endpoint: `/cars/<int:car_id>`
- Method: `GET`
- Parameters:
 - `car_id` (int): The unique identifier of the car to retrieve.
- Response: Returns a JSON object with the car data, or an error message if the car is not found.

### 3. Delete a Car:
- Endpoint: `/cars/<int:car_id>`
- Method: `DELETE`
- Parameters:
 - `car_id` (int): The unique identifier of the car to be deleted.
- Response: Returns a JSON object with a success message and the deleted car data, or an error message if the car is not found.

### 4. Get All Cars:
- Endpoint: `/cars`
- Method: `GET`
- Response: Returns a JSON object containing a list of all cars in the database.
