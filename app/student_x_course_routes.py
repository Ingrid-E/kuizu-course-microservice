from flask import Blueprint, request, jsonify
from app.database import dbConnection
from app.student_x_course_model import StudentXCourse
from bson.objectid import ObjectId
from datetime import date


db = dbConnection()
courses_db = db['Course']
student_x_course_db = db['StudentXCourse']
student_x_course_routes = Blueprint("studentXcourse_routes", __name__)

@student_x_course_routes.route("/add-student", methods=['POST'])
def create_course():
    data = request.get_json()
    try:
        course = courses_db.find_one({"_id":ObjectId(data["id_course"])})
        if(course == None):
            return {"success":False, "data":{"title":"Course doesn't exist"}}, 404
        student_x_course = StudentXCourse(data["id_student"], course,str(date.today()))
        res = student_x_course_db.insert_one(student_x_course.toDBCollection())
        return {"success":True, "data":{"title":"Student Added"}}, 200
    except Exception as ex:
        print(ex)
        return {"success":False, "data":{"title":"Internal Server Error"}}, 500

@student_x_course_routes.route("/delete-course/<id_course>", methods=['DELETE'])
def delete_course(id_course):
    try:
        course = courses_db.find_one_and_delete({"_id":ObjectId(id_course)})
        student_x_course_db.delete_many({"course":course})
        return {"success":True, "data":{"title":"Course Deleted"}}, 200
    except Exception as ex:
        print(ex)
        return {"success":False, "data":{"title":"Internal Server Error"}}, 500

@student_x_course_routes.route("/remove-student", methods=['DELETE'])
def remove_student():
    data = request.get_json()
    try:
        res = student_x_course_db.delete_one({"id_student":data["id_student"], "course._id":ObjectId(data["id_course"])})
        print(res.deleted_count)
        if(res.deleted_count <= 0):
            return {"success":False, "data":{"title":"Student not deleted, is the id correct?"}}, 404
        return {"success":True, "data":{"title":"Student Deleted"}}, 200
    except Exception as ex:
        print(ex)
        return {"success":False, "data":{"title":"Internal Server Error"}}, 500

@student_x_course_routes.route("/student-courses/<id_student>", methods=['GET'])
def find_student_courses(id_student):
    try:
        data = student_x_course_db.find({"id_student":int(id_student)})
        courses_list = []
        for student in data:
            student = dict(student)
            courses_list.append(student["course"])
        return {"success":True, "data":{"courses": courses_list}}, 200
    except Exception as ex:
        print(ex)
        return {"success":False, "data":{"title":"Internal Server Error"}}, 500