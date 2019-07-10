


class Match:
    user1 = None
    user2 = None
    score1 = None
    score2 = None
    winner = None
    loser = None
    users = {}

    def __init__(self, user1, user2):
        self.user1 = user1
        self.user2 = user2
        self.users[user1] = 0 # Jeroen
        self.users[user2] = 0 # Eddie
  
    def submitscore(self, user, score):
        self.users[user] = score

    def process(self):
        if self.users[self.user1] > self.users[self.user2]:
            self.winner = self.user1 
        else:
            self.winner = self.user2