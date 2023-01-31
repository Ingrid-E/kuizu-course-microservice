from flask import Blueprint, request
from app.database import dbConnection
from app.courses_model import Course
from bson.objectid import ObjectId
from flask_cors import CORS
from config import HerokuConfig
import boto3
import uuid


db = dbConnection()
courses_db = db['Course']
courses_routes = Blueprint("courses_routes", __name__)
student_x_course_db = db['StudentXCourse']
CORS(courses_routes)

s3 = boto3.client('s3', 
    aws_access_key_id = HerokuConfig.S3_ACCESS_KEY,
    aws_secret_access_key =HerokuConfig.S3_SECRET_ACCESS_KEY,
    region_name = HerokuConfig.S3_BUCKET_REGION,
)

@courses_routes.route("/", methods=['POST'])
def create_course():
    try:
        courseImage = request.files.get('icon')
        unique_id = str(uuid.uuid1())
        filenameKey = 'courses/{}'.format(unique_id+courseImage.filename.replace(" ", "_"))
        s3.upload_fileobj(
            Fileobj = courseImage,
            Bucket = HerokuConfig.S3_BUCKET_NAME,
            Key = filenameKey,
            ExtraArgs={
            'ACL': 'public-read',
            'ContentType': courseImage.content_type
        })
        namefile = 'https://kuizuapp-bucket.s3.amazonaws.com/'+filenameKey
        course = Course({
            'icon': namefile,
            'name': request.form.get('name'),
            'description': request.form.get('description'),
            'shortName': request.form.get('shortName'),
            'createdAt': request.form.get('createdAt'),
            'startAt': request.form.get('startAt'),
            'endAt': request.form.get('endAt'),
            'id_teacher': request.form.get('id_teacher'),
        })
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
            courseDB = course.toDBCollection()
            courseDB['_id'] = ObjectId(id)
            student_x_course_db.update_one({"_id":ObjectId(courses["_id"])}, {"$set":{"course":courseDB}})
        return {"success":True, "data":{"title":"Course Updated!", "course":str(id)}}, 200
    except Exception as ex:
        print(ex)
        return {"success":False, "data":{"title":"Internal Server Error"}}, 500