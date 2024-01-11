class Boss:
  def report(self):
      print("Mein Boss Hu")


class Manager1(Boss):
   def report(self):
      print("Manager1 : report to Boss")


class Manager2(Boss):
   def report(self):
      print("Manager2 : report to Boss")


class TeamLead1(Manager1,Manager2):
   def report(self):
      print("TeamLead1 : report to Manager1 and Manager2")


class TeamLead2(Manager1,Manager2):
   def report(self):
      print("TeamLead2 : report to Manager1 and Manager2")


class Developer(TeamLead1,TeamLead2):
   def report(self):
      print("Developer : report to TeamLead1 and TeamLead2")

print(Developer.mro())
'''
[<class '__main__.Developer'>, <class '__main__.TeamLead1'>, <class '__main__.TeamLead2'>, <class '__main__.Manager1'>, <class '__main__.Manager2'>, <class '__main__.Boss'>, <class 'object'>]
'''