class Person:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")

class Student(Person):
    def __init__(self,name,age,address,student_id):
        super().__init__(name,age,address)
        self.student_id = student_id
        self.grades ={}
        self.courses =[]
    def add_grade(self,subject,grade):
        if subject in self.courses:
            self.grades[subject] = grade

            print(f"Grade {grade} added for {self.name} in {subject}")
        else:
            print(f" Cannot assisgn grade {self.name} in not enroll in the {subject}")
    def enroll_course(self,course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"{course} added successfully")
        else: 
            print(f"{self.name} is already enrolled in {course}.")
   
    def display_student_info(self):
        print(f"Student Information\n Name: {self.name}\n Id: {self.student_id}\n Age: {self.age}\n Addesss: {self.address}\n Enrolled courses: {self.courses}\n Grades : {self.grades}")
class Course:
    def __init__(self,course_name,course_code,instructor):
        self.course_name = course_name    
        self.course_code = course_code 
        self.instructor = instructor
        self.students = []
    def add_student(self,student):
        if student not in self.students:
            self.students.append(student)
            print(f"Student: {student.name}(ID:{student.student_id}) enrolled in {self.course_name}(Code: {self.course_code})")

        else:
            print(f"Student: {student.name}(ID:{student.student_id}) already enrolled in {self.course_name}(Code: {self.course_code})")



    def display_course_info(self): 
        print(f"Course Information:\n Course Name: {self.course_name}\n Code: {self.course_code}\n Instructor: {self.instructor}")
        for student in self.students:
            print(f" Course inrolled students name :{student.name} (ID: {student.student_id})")

total_students ={}
total_courses ={}
def add_new_student():
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    address = input("Enter Address: ")
    student_id = input("Enter student id: ")
    student = Student(name, age, address, student_id)
    total_students[student_id] = student 
    print(f"Student {name} (ID: {student_id}) added successfully")

def add_new_course():
    course_name =input("Enter Course Name: ")
    course_code =input("Enter Course Code: ")
    instructor =input("Enter Instructor Name: ")
    course = Course(course_name,course_code,instructor)
    total_courses[course_code]= course
    print(f"Course {course_name} (Code: {course_code}) created with instructor {instructor}")

def Enroll_Student_in_Course():
    student_id = input("Enter Student ID: ")
    course_code = input("Enter Course Code: ")
    if student_id in total_students and course_code in total_courses:
        student = total_students[student_id]
        course = total_courses[course_code]
        student.enroll_course(course.course_name)
        course.add_student(student)
    
    else: 
        if student_id not in total_students:
            print("Student not found.")
        else:
            print("Course not found.")

def Add_Grade_for_Student():
    student_id = input("Enter Student ID: ")
    course_code = input("Enter Course Code: ")
    grade  = input("Enter Grade: ")
    if student_id in total_students and course_code in total_courses:
        student = total_students[student_id]
        course = total_courses[course_code]
        if course.course_name in student.courses:
            student.add_grade(course.course_name,grade)
        else:
            print(f"Student {student.name} is not enrolled in the course {course.course_name}.")

    else:
        print(f"Student {student.name} is not enrolled in the course {course.course_name}.")


        
def Display_Student_Details():
    student_id = input("Enter Student ID: ")
    if student_id in total_students:
        student = total_students[student_id]
        student.display_student_info()
    else:
        print("student not found")

def Display_Course_Details():
    course_code = input("Enter Course Code: ")
    if course_code in total_courses:
        course = total_courses[course_code]
        course.display_course_info()
    else:
        print("invalid course id")
import json
def save_data():
    data = {    "total_students": {
            sid: {
                "name": student.name,
                "age": student.age,
                "address": student.address,
                "student_id": student.student_id,
                "grades": student.grades,
                "courses": student.courses
            } for sid, student in total_students.items()
        },
        "total_courses": {
            cid: {
                "course_name": course.course_name,
                "course_code": course.course_code,
                "instructor": course.instructor,
                "students": [s.student_id for s in course.students]
            } for cid, course in total_courses.items()
        }
    }
                    
    with open ("data.json", "w") as file:
        json.dump(data,file,indent = 4)
    print("all students and courses data saved successfully")

def load_data():
    global total_students,total_courses
    try:
        with open("data.json","r") as file:
            data = json.load(file)
            for sid, student_data in data["total_students"].items():
                student = Student(
                    student_data["name"],
                    student_data["age"],
                    student_data["address"],
                    student_data["student_id"]
                )
                student.grades = student_data["grades"] 
                student.courses = student_data["courses"]
                total_students[sid]= student
            for cid, course_data in data["total_courses"].items():
                course = Course(
                    course_data["course_name"],
                    course_data["course_code"],
                    course_data ["instructor"]
                )
                for sid in course_data["students"]:
                    course.add_student(total_students[sid])
                    print("data loaded successfully")
                    total_courses[cid]= course
    except FileNotFoundError as e:
        print("file not found")


print("East west University Student Management System")
while True:
    
    print("""1. Add New Student
    2. Add New Course
    3. Enroll Student in Course
    4. Add Grade for Student
    5. Display Student Details
    6. Display Course Details
    7. Save Data to File
    8. Load Data from File
    0. Exit""")
    num1 = input("Choose an Option: ")
    if num1 == "1":
        add_new_student()
    elif num1 == "2":
        add_new_course()
        
    elif num1 == "3":
        Enroll_Student_in_Course()

    elif num1 == "4":
        Add_Grade_for_Student()
        

    elif num1 == "5":
        Display_Student_Details()

    elif num1 == "6":
        Display_Course_Details()
    
    elif num1 == "7":
       save_data()
    elif num1 == "8":
        load_data()
        
    elif num1 == "0":
        break
    else:
        print("Invalid option. Please choose a valid menu option.")
