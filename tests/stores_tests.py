import json


def store_list_test(self):
    """Test cases for list store endpoint"""
    response = self.app.get('/v1/stores')
    self.assertEqual(response.status_code, 200)
    json_response = json.loads(response.data)
    assert len(json_response["data"]) > 0
