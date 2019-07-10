

class User: 

    discordid = None
    id = None
    discordname = None
    elo = None

    def __init__(self, id, discordid, discordname, elo):
        self.id = id
        self.discordid = discordid
        self.discordname = discordname
        self.elo = elo 