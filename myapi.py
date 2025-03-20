"""
===============================
    FAST API TUTORIAL
===============================
Script purpost: 
    - To create a simple API using FastAPI
    - To demonstrate the use of Path and Query Parameters
    - To demonstrate the use of Request Body and Post Method
    - To demonstrate the use of Put Method
    - To demonstrate the use of Delete Method

Parameters:
    - Path Parameters
    - Query Parameters
    - BaseModel
    - Optional

Usage:
    - Run the script using the command: fastapi dev myapi.py
    - Open your browser and go to http://127.0.0.1:8000/ to view data
    - To view the API documentation and test API with Swagger UI, go to http://127.0.0.1:8000/docs

===============================


"""








from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

students = {
    1: {
        "name": "John"
        , "age": 17
        , "year": "year 12"
    }
}

class Student(BaseModel):
    name: str
    age : int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

@app.get("/") # Create end point
def index():
    return {"name": "First Data"}

# google.com/get-student/1 - Path Parameters
@app.get("/get-student/{student_id}") # Create end point
def get_student(student_id : int = Path(description="The ID of the student you want to view", gt=0, lt = 10)):
    return students.get(student_id)

# google.com/results?search=python  - Combining Path and Query Parameters
@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int ,name : Optional[str]= None, test : int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}

# Request Body and Post Method

@app.post("/create-student/{student_id}")
def create_student(student_id: int , student : Student):
    if student_id in students:
        return {"Error": "Student Exists"}
    
    students[student_id] = student
    return students[student_id]

# Put Method 
@app.put("/update-student/{student_id}")
def update_student(student_id : int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    if student.name != None:
        students[student_id].name = student.name
    
    if student.age != None:
        students[student_id].age = student.age
    
    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]
    
# Delete Method
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    del students[student_id]
    return {"Message": "Student deleted successfully"}