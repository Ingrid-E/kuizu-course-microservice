import unittest
from unittest.mock import patch
from app.student_x_course_routes import get_student_course_avg



class TestAPI(unittest.TestCase):
    @patch('pymongo.collection.Collection.find')
    def test_avg_courses(self,mock_get):
        
        mock_get.return_value = [{
                "average": 0,
                "course": "Mathematics",
                "id_course": "63a26336e500246d0921b0e8",
                "shortName": "Math"
            },
            {
                "average": 0,
                "course": "Mathematics",
                "id_course": "63a26657bfd60f401af2ed1f",
                "shortName": "Math"
            }]
        result = get_student_course_avg(1)
        print('this is result: ', result)
        """self.assertEqual(result, ({'success': True, 'data': {'courses': [{'_id': '63a26336e500246d0921b0e8', 'createdAt': '2022-12-13', 'description': 'Math course', 'endAt': '2022-12-20', 'icon': 'icon.png', 'id_teacher': '1', 'name': 'Mathematics', 'shortName': 'Math', 'startAt': '2022-12-18'}, {'_id': '63a2634773c89fd7fde5f473', 'createdAt': '2022-12-13', 'description': 'Math course', 'endAt': '2022-12-20', 'icon': 'icon.png', 'id_teacher': '1', 'name': 'Chemistry', 'shortName': 'Chem', 'startAt': '2022-12-18'}]}}, 200))"""
    
if __name__ == '__main__':
    unittest.main()