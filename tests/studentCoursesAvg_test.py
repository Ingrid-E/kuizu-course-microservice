import unittest
from flask import Flask, jsonify
from flask.testing import FlaskClient

# Create a Flask app
app = Flask(__name__)

# Define a route that returns a JSON response
@app.route('/student-courses-avg/34', methods=['GET'])
def api_endpoint():
        return jsonify({'key': 'value'})

class TestAPI(unittest.TestCase):
    def setUp(self):
        # Create a FlaskClient instance for the app
        self.client = FlaskClient(app)

    def test_get_request(self):
        # Send a GET request to the endpoint using the client
        response = self.client.get('/student-courses-avg/34')

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Check the response data
        self.assertEqual(response.get_json(), {'key': 'value'})

if __name__ == '__main__':
    unittest.main()
