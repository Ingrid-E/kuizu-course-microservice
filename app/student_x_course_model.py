class StudentXCourse:
    def __init__(self, id_student, course, addedAt):
        self.id_student = id_student
        self.course =  course
        self.addedAt = addedAt
        
    def toDBCollection(self):
        return{
            'id_student': self.id_student,
            'course': self.course,
            'addedAt': self.addedAt
        }