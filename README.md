This file, FetchBackendAPI.py, is a Flask-based backend API for processing and scoring receipts. Here's a brief explanation of its components and functionality:

1. **Imports**: The necessary modules such as Flask, uuid, json, and math are imported.
2. **Flask App Initialization**: A Flask application named "Fetch" is initialized.
3. **Global Variables**: A dictionary `receiptScoreDict` is initialized to store receipt scores.
4. **Function `calculate_total_points(data_dict)`**: This function calculates the total points for a given receipt based on various criteria:
5. **Route `POST /receipts/process`**: This route processes a receipt, calculates its points using the `calculate_total_points` function, and stores the result in `receiptScoreDict`. It returns a JSON response with a unique receipt ID and status.
6. **Route `GET /receipts/<id>/points`**: This route retrieves the points for a specific receipt ID from `receiptScoreDict` and returns them in a JSON response. If the receipt ID is not found, it returns an error message.
7. **Main Block**: The Flask app runs in debug mode if the script is executed directly.


Some curl commands for ease of testing.

curl -X POST http://127.0.0.1:5000/receipts/process \
  -H "Content-Type: application/json" \
  -d @example-2.json

curl -X POST http://127.0.0.1:5000/receipts/process \
  -H "Content-Type: application/json" \
  -d @example-1.json

curl -X GET http://127.0.0.1:5000/receipts/<id_from_above_request>/points
