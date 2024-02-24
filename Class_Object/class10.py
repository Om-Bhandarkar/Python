class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay 
        self.email = first + "." + last  + "@company.com"

    def fulName(self):
        print("Full Name : {} {}".format(self.first,self.last))
    
    def empSal(self):
        print ("Employee Normal Salary : ", self.pay)

    def raise_Sal(self):
        self.pay = int(self.pay) * 1.04
        print("Raised Salary : {}".format(self.pay))

emp1 = Employee(first=input("Enter First Name : ") ,last=input("Enter Last Name : "),pay=int(input("Enter Your Salary : ")))
# emp1.fulName()
print(Employee.fulName(emp1))
emp1.raise_Sal()