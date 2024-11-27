from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock car database
car_database = []

# Add a New Car
@app.route('/cars', methods=['POST'])
def add_car():
    car = request.json
    if not car or "make" not in car or "model" not in car or "year" not in car:
        return jsonify({"error": "Invalid input. 'make', 'model', and 'year' fields are required."}), 400
    car["id"] = len(car_database) + 1
    car_database.append(car)
    return jsonify({"message": "Car added", "car": car}), 201

# Update an Existing Car
@app.route('/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    car = next((c for c in car_database if c["id"] == car_id), None)
    if not car:
        return jsonify({"error": "Car not found"}), 404
    updates = request.json
    car.update(updates)
    return jsonify({"message": "Car updated", "car": car}), 200

# Delete a Car
@app.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    car = next((c for c in car_database if c["id"] == car_id), None)
    if not car:
        return jsonify({"error": "Car not found"}), 404
    car_database.remove(car)
    return jsonify({"message": "Car deleted", "car": car}), 200

# Get a Car by ID
@app.route('/cars/<int:car_id>', methods=['GET'])
def get_car(car_id):
    car = next((c for c in car_database if c["id"] == car_id), None)
    if not car:
        return jsonify({"error": "Car not found"}), 404
    return jsonify({"car": car}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
