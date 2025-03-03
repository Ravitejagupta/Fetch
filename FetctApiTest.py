import unittest
import json
from FetchBackendAPI import app, receiptScoreDict

class FetchApiTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_process_receipt_valid(self):
        receipt_data = {
            "retailer": "Target",
            "purchaseDate": "2022-01-01",
            "purchaseTime": "14:30",
            "total": "35.00",
            "items": [
                {"shortDescription": "item1", "price": "10.00"},
                {"shortDescription": "item2", "price": "25.00"}
            ]
        }
        response = self.app.post('/receipts/process', data=json.dumps(receipt_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertIn("id", response_data)
        self.assertEqual(response_data["status"], "200 OK")

    def test_process_receipt_invalid(self):
        receipt_data = {
            "retailer": "Target",
            "purchaseDate": "2022-01-01",
            "purchaseTime": "14:30",
            "total": "35.00"
            # Missing items
        }
        response = self.app.post('/receipts/process', data=json.dumps(receipt_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.data)
        self.assertIn("error", response_data)

    def test_get_points_valid(self):
        receipt_data = {
            "retailer": "Target",
            "purchaseDate": "2022-01-01",
            "purchaseTime": "14:30",
            "total": "35.00",
            "items": [
                {"shortDescription": "item1", "price": "10.00"},
                {"shortDescription": "item2", "price": "25.00"}
            ]
        }
        response = self.app.post('/receipts/process', data=json.dumps(receipt_data), content_type='application/json')
        response_data = json.loads(response.data)
        receipt_id = response_data["id"]

        response = self.app.get(f'/receipts/{receipt_id}/points')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertIn("points", response_data)

    def test_get_points_invalid(self):
        response = self.app.get('/receipts/invalid_id/points')
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.data)
        self.assertIn("error", response_data)

if __name__ == '__main__':
    unittest.main()