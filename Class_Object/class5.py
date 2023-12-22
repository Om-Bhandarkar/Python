class Student:

    def __init__(self):
        print("In Constructor")
        self.studId = int(input("Enter Student Id : "))
        self.studName = input("Enter Student Name : ")

    def studentInfo(self):
        print("Student Id : {}".format(self.studId))
        print("Student Name : {}".format(self.studName))


stud = Student()
stud.studentInfo()
