class Human():
    def __init__(self, id="", name="", DoB=""):
        self.id=id
        self.name=name
        self.DoB=DoB
    def getName(self):
        return self.name
    def getId(self):
        return self.id
    def getDoB(self):
        return self.DoB
    def setName(self,name):
        self.name=name
    def setId(self,id):
        self.id=id
    def setDoB(self,DoB):
        self.DoB=DoB
    def toPrint(self):
        result= f"{self.id} {self.name} {self.DoB}"
        return result
class Student(Human):
    def __init__(self, course="", score="", id="", name="", DoB=""):
        super().__init__(id,name,DoB)
        self.course=course
        self.score=score
    def getCourse(self):
        return self.course
    def getScore(self):
        return self.score
    def setCourse(self,course):
        self.course=course
    def setScore(self,score):
        self.score=score
    def toPrint(self):
        return f"{super().toPrint()} {self.course} {self.score}"
# class Score():
# def __init__(self,)
class Course():
    def __init__(self, id='', name='', students=list([])):
        self.id=id
        self.name=name
        self.students=students
    def getName(self):
        return self.name
    def getId(self):
        return self.id
    def getStudents(self):
        return self.students
    def setName(self,name):
        self.name=name
    def setId(self,id):
        self.id=id
    #Overwrite student array
    def setStudents(self,students):
        self.students = students
    def addStudent(self,students):
        if(isinstance(students,list)):
            self.students= self.students+students
        else:
            print("Wrong type of input")
    def toPrint(self):
        return f"{self.id} {self.name}"
class StudentMarkManagement():
    def __init__(self, courses=list([])):
        self.courses=courses
    def getCourses(self):
        return self.courses
    def setCourses(self,courses):
        self.courses=courses
    def inputStudents(self, nameCourse, students):
        for i in range(len(self.courses)):
            if(self.courses[i].getName()==nameCourse):
                self.courses[i].addStudents(students)
            print("Done")
    def inputCourses(self,courses):
        if(isinstance(courses,list)):
            self.courses= self.courses+courses
        else:
            print("Wrong type of input")
    def inputMarks(self, marks, course):
        #Assume that marks is kind of {nameStudent: mark}
        if(isinstance(marks,dict)):
            cou=[]
            for i in range(len(self.courses)):
                if(self.courses[i].getName()==course):
                    cou=self.courses[i]
                    break
            for i in cou.getStudents():
                i.setScore(marks[i.getName()])
        else:
            print("Wrong type of input")
    def listCourses(self):
        result=""
        for i in self.courses:
            result+=i.getName()
        return result
    def listStudent(self,course):
        cou=[]
        result=""
        for i in range(len(self.courses)):
                if(self.courses[i].getName()==course):
                    cou=self.courses[i]
                    break
        for i in cou.getStudents():
            result+=i.getName()
            result+="\n"
        return result
    def showMarks(self,course):
        cou=[]
        result=""
        for i in range(len(self.courses)):
                if(self.courses[i].getName()==course):
                    cou=self.courses[i]
                    break
        for i in cou.getStudents():
            result+=i.toPrint()
            result+="\n"
        return result





