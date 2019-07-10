
from user import User
from match import Match

class Wachtlijst: 

    users = []

    def add(self, user):
        self.users.append(user)

    def matching(self, user):

        # kijken of wachtlijst meerdere spelers bevat
        if self.users.__len__ >= 2:
            firstuser = self.users.pop(0)
            seconduser = self.user.pop(0)
            
            match = Match(firstuser, seconduser)
            

