import unittest
from unittest.mock import patch
from app.student_x_course_routes import remove_student

class FlaskTestCase(unittest.TestCase):
    @patch('pymongo.collection.Collection.delete_one')
    def test_delete_item(self,mock_delete):
        mock_delete = remove_student()
        response = mock_delete.delete('/remove-student', data={
        "id_student":"1",
        "id_course":"63a26336e500246d0921b0e8"
    })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"data": {
        "title": "Student Deleted"},
        "success": True
})

if __name__ == '__main__':
    unittest.main()