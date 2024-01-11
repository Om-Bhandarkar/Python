class Boss:
    def report(self):
        print("I am Boss")

class Manager1(Boss):
    def report(self):
        print("Manage1 : report to Boss")
        

class Manager2(Boss):
    def report(self):
        print("Manager2 : report to Boss")


class TeamLead1(Manager1,Manager2):
    def report(self):
        print("TeamLead1 : report to the Manager1 and Manager2")


class TeamLead2(Manager1,Manager2):
    def report(self):
        print("TeamLead2 : report to the Manager1 and Manager2")

class Developer(TeamLead1,TeamLead2):
    def report(self):
        print("Developer : report to TeamLead1,Teamlead2")

obj = Developer()

obj.report()
