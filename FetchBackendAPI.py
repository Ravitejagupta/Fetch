from flask import Flask, jsonify, request
import uuid
import json
import math

app = Flask("Fetch")

# Initialize a counter variable
receiptScoreDict = {}

def calculate_total_points(data_dict):
    totalPoints = 0

    # Retailer points
    try:
        for char in data_dict["retailer"]:
            if char.isalnum():
                totalPoints += 1

        if float(data_dict["total"]).is_integer():
            totalPoints += 50

        if (float(data_dict["total"]) / 0.25).is_integer():
            totalPoints += 25

        totalPoints += (len(data_dict["items"]) // 2) * 5

        for item in data_dict["items"]:
            if len(item["shortDescription"].strip()) % 3 == 0:
                totalPoints += math.ceil(float(item["price"]) * 0.2)

        if int(data_dict["purchaseDate"].split("-")[-1]) % 2 == 1:
            totalPoints += 6

        # PurchaseTime Calculation
        hour_, min_ = data_dict["purchaseTime"].split(":")
        if int(hour_) * 60 + int(min_) in range(841, 960):
            totalPoints += 10
    except (KeyError, ValueError, TypeError) as e:
        raise

    return totalPoints

@app.route('/receipts/process', methods=['POST'])
def process_receipt():
    new_uuid = str(uuid.uuid4())
    data = request.get_json()
    data_dict = json.loads(json.dumps(data))

    try:
        totalPoints = calculate_total_points(data_dict)
        receiptScoreDict[new_uuid] = totalPoints
        return jsonify({"id": new_uuid, "status": "200 OK"}), 200
    except (KeyError, ValueError, TypeError) as e:
        return jsonify({"error": f"Invalid receipt format: {e}"}), 400

@app.route('/receipts/<id>/points', methods=['GET'])
def get_points(id):
    try:
        points = receiptScoreDict[id]
        return jsonify({"points": points}), 200
    except KeyError:
        return jsonify({"error": "Receipt ID not found"}), 400

if __name__ == '__main__':
    app.run(debug=True)