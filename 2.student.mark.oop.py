# The Human class represents a human with an ID, name, and date of birth (dob).
# It has getters and setters for each of these attributes, and a to_print() method for printing the human's details.
class Human:
    def __init__(self, id="", name="", dob=""):
        self.__id = id
        self.__name = name
        self.__dob = dob

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_dob(self, dob):
        self.__dob = dob

    def to_print(self):
        return f"{self.__id} {self.__name} {self.__dob}"


# The Student class inherits from the Human class and adds a course and score attribute.
# It also overrides the to_print() method to include the course and score.
class Student(Human):
    def __init__(self, course="", score="", id="", name="", dob=""):
        super().__init__(id, name, dob)
        self.__course = course
        self.__score = score

    def get_course(self):
        return self.__course

    def get_score(self):
        return self.__score

    def set_course(self, course):
        self.__course = course

    def set_score(self, score):
        self.__score = score

    def to_print(self):
        return f"{super().to_print()} {self.__course} {self.__score}"


# The Course class represents a course with an ID, name, and a list of students.
# It has getters and setters for each of these attributes, and methods to add and remove students from the list.
# It also has a to_print() method for printing the course's details.
class Course:
    def __init__(self, id='', name='', students=None):
        self.__id = id
        self.__name = name
        self.__students = students or []

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_students(self):
        return self.__students

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_students(self, students):
        self.__students = students

    def add_student(self, student):
        self.__students.append(student)

    def remove_student(self, student):
        self.__students.remove(student)

    def to_print(self):
        return f"{self.__id} {self.__name}"


# The StudentMarkManagement class manages a list of courses and provides methods to add and remove courses and students,
# add marks for students, list all courses and students, and show marks for a particular course.
class StudentMarkManagement:
    def __init__(self, courses=None):
        self.__courses = courses or []

    def get_courses(self):
        return self.__courses

    def set_courses(self, courses):
        self.__courses = courses

    def add_course(self, course):
        self.__courses.append(course)

    def remove_course(self, course):
        self.__courses.remove(course)

    def add_student(self, course, student):
        for c in self.__courses:
            if c.get_name() == course:
                c.add_student(student)

    def remove_student(self, course, student):
        for c in self.__courses:
            if c.get_name() == course:
                c.remove_student(student)

    def add_mark(self, course, student, mark):
        for c in self.__courses:
            if c.get_name() == course:
                for s in c.get_students():
                    if s.get_name() == student:
                        s.set_score(mark)

    def list_courses(self):
        return [c.get_name() for c in self.__courses]

    def list_students(self, course):
        for c in self.__courses:
            if c.get_name() == course:
                return [s.to_print() for s in c.get_students()]

    def show_marks(self, course):
        for c in self.__courses:
            if c.get_name() == course:
                return [s.to_print() for s in c.get_students()]