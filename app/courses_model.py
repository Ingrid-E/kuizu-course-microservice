class Course:
    def __init__(self, data):
        self.icon = data["icon"]
        self.name =  data["name"]
        self.description = data["description"]
        self.shortName = data["shortName"]
        self.createdAt = data["createdAt"]
        self.startAt = data["startAt"]
        self.endAt = data["endAt"]
        self.id_teacher = data["id_teacher"]
    
    def toDBCollection(self):
        return{
            'icon': self.icon,
            'name': self.name,
            'description': self.description,
            'shortName': self.shortName,
            'createdAt': self.createdAt,
            'startAt': self.startAt,
            'endAt': self.endAt,
            'id_teacher': self.id_teacher
        }