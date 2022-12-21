from flask import Flask
from app.courses_routes import courses_routes
from app.student_x_course_routes import student_x_course_routes
from app.json_encoder import JSONEncoder

def create_app():
    app = Flask(__name__)
    app.json_encoder = JSONEncoder
    app.config.from_object('config.DevConfig')
    app.register_blueprint(courses_routes)
    app.register_blueprint(student_x_course_routes)
    return app


