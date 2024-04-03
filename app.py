# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

courses = [
    {"course_number": 10381, "course_title": "English in Business Context s B1", "course_level": "B1", "type_of_exam": "60-minute written exam", "exam_requirement": "Minimum 75% attendance rate", "sws": 2},
    {"course_number": 10451, "course_title": "Business English B2: Economy and Society", "course_level": "B2", "type_of_exam": "60-minute written exam", "exam_requirement": "Minimum 75% attendance rate", "sws": 2},
    {"course_number": 10481, "course_title": "English in Business Contexts B2", "course_level": "B2", "type_of_exam": "60-minute written exam", "exam_requirement": "Minimum 75% attendance rate", "sws": 2},
    {"course_number": 10441, "course_title": "Business English B2: Writing and Communication Skills", "course_level": "B2", "type_of_exam": "60-minute written exam", "exam_requirement": "Minimum 75% attendance rate", "sws": 2},
    {"course_number": 10361, "course_title": "Intensive Language Course Business English B2", "course_level": "B2", "type_of_exam": "60-minute written exam", "exam_requirement": "Minimum 75% attendance rate", "sws": 2},
    {"course_number": 10551, "course_title": "Business English C1: Economy and Society", "course_level": "C1", "type_of_exam": "60-minute written exam", "exam_requirement": "Minimum 75% attendance rate", "sws": 2},
    {"course_number": 10565, "course_title": "Business English C1: Strategies and Management", "course_level": "C1", "type_of_exam": "60-minute written exam", "exam_requirement": "Minimum 75% attendance rate", "sws": 2},
    {"course_number": 10591, "course_title": "Intensive Language Course Business English C1", "course_level": "C1", "type_of_exam": "60-minute written exam", "exam_requirement": "Minimum 75% attendance rate", "sws": 2},
    {"course_number": 10475, "course_title": "Intensive Language Course General Technical English B2", "course_level": "B2", "type_of_exam": "60-minute written exam", "exam_requirement": "Minimum 75% attendance rate", "sws": 2},
]

@app.get("/courses")
def get_courses():
    response_data = jsonify(courses)
    print(f"Response content: {response_data}")
    return response_data

if __name__ == "__main__":
    app.run(debug=True)

