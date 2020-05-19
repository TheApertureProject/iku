import discord
from discord.ext import commands
from discord.ext.commands import Cog
import mysql.connector
import os

DBU = os.environ["DB_USERNAME"]
DBM = os.environ["DB_PASSWORD"]
DBN = os.environ["DB_NAME"]
DBH = os.environ["DB_HOST"]
DBP = os.environ["DB_PORT"]

conn = mysql.connector.connect(user=DBU, password=DBM, database=DBN, host=DBH, port=DBP)

botcursor = conn.cursor()

class Datacom(Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["start"])
    async def register(self, ctx):
        msg = await ctx.send("<a:loading:712211273743597618> | Création de votre profil utilisateur en cours.")
        try:
            botcursor.execute("INSERT INTO data(userid INT, money INT, Level INT), VALUES ({}, {}, {})".format(ctx.author.id, 1000, 1))
        except Exception as e:
            print(e)
        a = f""":white_check_mark: | Votre profil a bien été créé, {ctx.author.mention}. Voici vos statistiques de départ :
> :heart_decoration: Rang : 1
> :credit_card: Crédits : 1000
Affichez à tout moment ces statistiques avec la commande `profil`. Amusez-vous bien !"""
        await msg.edit(content=a)

def setup(bot):
    bot.add_cog(Datacom(bot))
