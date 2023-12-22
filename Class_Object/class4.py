class Student:

    def __init__(self):
        print("In Constructor")
        self.studId = 4
        self.studName = "Om"

    def studentInfo(self):
        print(self.studId)
        print(self.studName)


stud = Student()
stud.studentInfo()
