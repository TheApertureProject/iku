import discord
from discord.ext import commands
from discord.ext.commands import Cog
import os

DBU = os.environ["DB_USERNAME"]
DBM = os.environ["DB_PASSWORD"]
DBN = os.environ["DB_NAME"]
DBH = os.environ["DB_HOST"]
DBP = os.environ["DB_PORT"]

conn = mariadb.connect(user=DBU, password=DBM, database=DBN, host=DBH, port=DBP)

botcursor = conn.cursor()

class Datacom(Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["start"])
    async def register(self, ctx):
        

def setup(bot):
    bot.add_cog(Datacom(bot)
