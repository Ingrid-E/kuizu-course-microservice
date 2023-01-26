import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(current_dir, '..', '..')))
print(sys.path)
import unittest
from unittest.mock import patch
from app.courses_routes import get_all, find_course, find_teacher_courses

class TestAPI(unittest.TestCase):
    @patch('pymongo.collection.Collection.find')
    def test_course_get_all(self,mock_get):
        
        mock_get.return_value = [{'_id': "1", 'icon': 'icon.png', 'name': 'Mathematics', 'description': 'Math course',
         'shortName': 'Math', 'createdAt': '2022-12-13', 'startAt': '2022-12-18', 'endAt': '2022-12-20', 'id_teacher': '1'}]
        result = get_all()
        print('this is result (get_all):\n', result)
        self.assertEqual(result, ({'success': True, 'data': {'courses': [{'_id': '1', 'icon': 'icon.png', 'name': 'Mathematics', 'description': 'Math course', 'shortName': 'Math', 'createdAt': '2022-12-13', 'startAt': '2022-12-18', 'endAt': '2022-12-20', 'id_teacher': '1'}]}}, 200))

    @patch('pymongo.collection.Collection.find_one')
    def test_course_find_course(self,mock_find_one):
        
        mock_find_one.return_value = {
            "_id": "63a26336e500246d0921b0e8",
            "createdAt": "2022-12-13",
            "description": "Math course",
            "endAt": "2022-12-20",
            "icon": "icon.png",
            "id_teacher": "1",
            "name": "Mathematics",
            "shortName": "Math",
            "startAt": "2022-12-18"
        }
        result = find_course("63a26336e500246d0921b0e8")
        print('this is result (find_course):\n', result)
        self.assertEqual(result, ({'success': True, 'data': {'course': {'_id': '63a26336e500246d0921b0e8', 'createdAt': '2022-12-13', 
        'description': 'Math course', 'endAt': '2022-12-20', 'icon': 'icon.png', 'id_teacher': '1', 'name': 'Mathematics', 'shortName': 'Math', 'startAt': '2022-12-18'}}}, 200))
        
    @patch('pymongo.collection.Collection.find')
    def test_course_find_teacher_courses(self,mock_get):
        
        mock_get.return_value = [{
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
                "_id": "63a2634773c89fd7fde5f473",
                "createdAt": "2022-12-13",
                "description": "Math course",
                "endAt": "2022-12-20",
                "icon": "icon.png",
                "id_teacher": "1",
                "name": "Chemistry",
                "shortName": "Chem",
                "startAt": "2022-12-18"
            }]
        result = find_teacher_courses(1)
        print('this is result (find_teacher_courses):\n', result)
        self.assertEqual(result, ({'success': True, 'data': {'courses': [{'_id': '63a26336e500246d0921b0e8', 'createdAt': '2022-12-13', 'description': 'Math course', 'endAt': '2022-12-20', 'icon': 'icon.png', 'id_teacher': '1', 'name': 'Mathematics', 'shortName': 'Math', 'startAt': '2022-12-18'}, {'_id': '63a2634773c89fd7fde5f473', 'createdAt': '2022-12-13', 'description': 'Math course', 'endAt': '2022-12-20', 'icon': 'icon.png', 'id_teacher': '1', 'name': 'Chemistry', 'shortName': 'Chem', 'startAt': '2022-12-18'}]}}, 200))
    
if __name__ == '__main__':
    unittest.main()
