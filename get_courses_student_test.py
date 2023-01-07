import unittest
from unittest.mock import patch
from app.student_x_course_routes import find_student_courses



class TestAPI(unittest.TestCase):
    @patch('pymongo.collection.Collection.find')
    def test_course_get_courses(self,mock_get):
        
        mock_get.return_value = [
            {
                "_id": "63a26336e500246d0921b0e8",
                "createdAt": "2022-12-13",
                "description": "Math course",
                "endAt": "2022-12-20",
                "icon": "icon.png",
                "id_teacher": "1",
                "name": "Mathematics",
                "shortName": "Math",
                "startAt": "2022-12-18"
            },
            {
                "_id": "63a26657bfd60f401af2ed1f",
                "createdAt": "2022-12-13",
                "description": "Math course",
                "endAt": "2022-12-20",
                "icon": "icon.png",
                "id_teacher": "1",
                "name": "Mathematics",
                "shortName": "Math",
                "startAt": "2022-12-18"
            },
            {
                "_id": "63a3b316d2c6833acef3c489",
                "createdAt": "2022-12-13",
                "description": "Math course",
                "endAt": "2022-12-20",
                "icon": "icon.png",
                "id_teacher": "1",
                "name": "Test1",
                "shortName": "T1",
                "startAt": "2022-12-18"
            }
        ]
        result = find_student_courses(1)
        print('this is result: ', result)
        """self.assertEqual(result, ({'success': True, 'data': {'courses': [{'_id': '63a26336e500246d0921b0e8', 'createdAt': '2022-12-13', 'description': 'Math course', 'endAt': '2022-12-20', 'icon': 'icon.png', 'id_teacher': '1', 'name': 'Mathematics', 'shortName': 'Math', 'startAt': '2022-12-18'}, {'_id': '63a2634773c89fd7fde5f473', 'createdAt': '2022-12-13', 'description': 'Math course', 'endAt': '2022-12-20', 'icon': 'icon.png', 'id_teacher': '1', 'name': 'Chemistry', 'shortName': 'Chem', 'startAt': '2022-12-18'}]}}, 200))"""
    
if __name__ == '__main__':
    unittest.main()