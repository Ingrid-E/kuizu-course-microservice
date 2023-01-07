from unittest.mock import patch
import unittest
from app.courses_routes import update_course
from flask import Request

class TestAPI(unittest.TestCase):
    def test_my_route(client):
        with patch('pymongo.collection.Collection.update_one') as mock_some_class:
            # Set up the mock
            Request
            result = update_course("63a26f79d1793078e3908878")
            instance = mock_some_class.return_value
            instance.do_something.return_value = {
            "data": {
            "course": "63a26f79d1793078e3908878",
            "title": "Course Updated!"
    },
            "success": True
}
        # Make the request and assert the response
        response = client.put('/63a26f79d1793078e3908878', data={
        "icon":"icon20.png",
        "name":"Mathematic",
        "description":"Math courses",
        "shortName":"Math",
        "createdAt":"2022-12-13",
        "endAt":"2022-12-20",
        "startAt":"2022-12-18",
        "id_teacher":"1"
    })
        assert response.status_code == 200
        assert response.data == b'mocked result'


if __name__ == '__main__':
    unittest.main()