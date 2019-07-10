
import discord
from database import Database

database = Database()
user = database.getUserByID(1)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        userid = message.author.id
        naam = message.author.display_name
        print(userid, naam)
        if message.content[0] == '/':
            blocks = message.content[1:].split(' ')

            if blocks[0] == "match":
                # Gooien iemand in wachtlijst 
                
                


            if blocks[0] == "accept":
                if len(blocks) > 1: 
                    print('mention')
                else: 
                    print('geen mention')
        

            print(blocks)
        else: 
            print('geen commando')



        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run('NTk3MTkzMDcwMTM5OTMyNjc0.XSEhkQ.sUAsFCQgPjY4iauAjrWUSp-AuNs')