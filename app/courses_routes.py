from flask import Blueprint, request, jsonify
from app.database import dbConnection
from app.courses_model import Course
from bson.objectid import ObjectId
from flask_cors import CORS

db = dbConnection()
courses_db = db['Course']
courses_routes = Blueprint("courses_routes", __name__)
student_x_course_db = db['StudentXCourse']
CORS(courses_routes)

@courses_routes.route("/", methods=['POST'])
def create_course():
    data = request.get_json()
    try:
        course = Course(data)
        res = courses_db.insert_one(course.toDBCollection())
        return {"success":True, "data":{"title":"Course Created!", "course":str(res.inserted_id)}}, 201
    except Exception as ex:
        print(ex)
        return {"success":False, "data":{"title":"Internal Server Error"}}, 500

@courses_routes.route("/<id>", methods=['GET'])
def find_course(id):
    try:
        course = courses_db.find_one({"_id":ObjectId(id)})
        return {"success":True, "data":{"course": dict(course)}}, 200
    except Exception as ex:
        print(ex)
        return {"success":False, "data":{"title":"Internal Server Error"}}, 500

@courses_routes.route("/", methods=['GET'])
def get_all():
    try:
        courses = courses_db.find()
        courses_list = []
        for course in courses:
            courses_list.append(dict(course))
        return {"success":True, "data":{"courses": courses_list}}, 200
    except Exception as ex:
        print(ex)
        return {"success":False, "data":{"title":"Internal Server Error"}}, 500


@courses_routes.route("/teacher-courses/<id_teacher>", methods=['GET'])
def find_teacher_courses(id_teacher):
    try:
        courses = courses_db.find({"id_teacher":id_teacher})
        courses_list = []
        for course in courses:
            courses_list.append(dict(course))
        return {"success":True, "data":{"courses": courses_list}}, 200
    except Exception as ex:
        print(ex)
        return {"success":False, "data":{"title":"Internal Server Error"}}, 500

@courses_routes.route("/<id>", methods=['PATCH', 'PUT'])
def update_course(id):
    data = request.get_json()
    try:
        data_student_x_course = student_x_course_db.find({"course._id":ObjectId(id)})
        course = Course(data)
        courses_db.update_one({"_id":ObjectId(id)}, 
                                        {"$set":course.toDBCollection()})

        for courses in data_student_x_course:
            courses = dict(courses)
            print(courses)
            student_x_course_db.update_one({"_id":ObjectId(courses["_id"])}, {"$set":{"course":course.toDBCollection()}})
        return {"success":True, "data":{"title":"Course Updated!", "course":str(id)}}, 200
    except Exception as ex:
        print(ex)
        return {"success":False, "data":{"title":"Internal Server Error"}}, 500
