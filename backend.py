from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock car database
car_database = []

# Update an Existing Car 
@app.route('/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id): 
    car = next((c for c in car_database if c["id"] == car_id), None)
    if not car:
        return jsonify({"error": "Car not found"}), 404
    updates = request.json
    car.update(updates) 
    return jsonify({"message": "Car updated", "car": car}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
