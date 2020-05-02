import discord
from discord.ext import commands
from discord.ext.commands import Cog
import os

DBU = os.environ["DB_USERNAME"]
DBP = os.environ["DB_PASSWORD"]
DBN = os.environ["DB_NAME"]
DBH = os.environ["DB_HOST"]
DBP = os.environ["DB_PORT"]

conn = mariadb.connect(user='root', password='default', database='iku_test', host='localhost', port='3306')

botcursor = conn.cursor()

class Datacom(Cog):

    def __init__(self, bot):
        self.bot = bot

    

def setup(bot):
    bot.add_cog(Datacom(bot)
