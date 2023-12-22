class Company:
    compName = "FaceBook"

    def __init__(self):
        print("In Constructor")
        self.empId = 12
        self.empName = "Kanha"

    def compInfo(self):
        print(self.empId)
        print(self.empName)
        # print(compName)


emp1 = Company()

emp1.compInfo()
