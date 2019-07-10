from user import User

class Database: 

    users = []

    def __init__(self):
        users = "hallo"

        self.users.append(User(1, 1001, 'jfast', 3600))
        self.users.append(User(2, 223789554786762752, 'hans', 1000))
        self.users.append(User(3, 1003, 'sjaak', 3599))
        self.users.append(User(4, 1004, 'piet', 2900))
     
    def getUserByID(self, id):
        for user in self.users:
            if user.id == id:
                return user