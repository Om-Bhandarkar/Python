class IPL:

    company_Name = "Cisco"

    def __init__(self, jerNo, player_name):

        self.jerNo = jerNo

        self.player_name = player_name

    def player_info(self):

        print(self.jerNo)

        print(self.player_name)

        print(IPL.company_Name)

d = IPL(jerNo = 7, player_name = "MSDhoni")

d.player_info()

