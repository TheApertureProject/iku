import discord
from discord.ext import commands
from discord.ext.commands import Cog
from databases import Database
import os
import asyncio

sql_connect_url = os.environ["JAWSDB_URL"]

database = Database(sql_connect_url)

class Datacom(Cog):

    def __init__(self, bot):
        self.bot = bot
        bot.loop.create_task(database.connect())


    @commands.command(aliases=["start"])
    async def register(self, ctx):

        msg = await ctx.send("<a:loading:712211273743597618> | Création de votre profil utilisateur en cours.")
        
        await database.execute("DROP TABLE data")
        await database.execute("CREATE TABLE maindata (UserId INT, Balance INT, LastDaily INT, LastWork INT, Level INT)")

        UserId = ctx.author.id
        Balance = 1000
        Level = 1

        try:
            await database.execute("INSERT INTO MainData (UserId, Balance, Level) VALUES ({}, {}, {})".format(UserId, Balance, Level))
        except Exception as e:
            print(e)
        a = f""":white_check_mark: | Votre profil a bien été créé, {ctx.user.mention}. Voici vos statistiques de départ :

> :heart_decoration: Rang : `{Level}`
> :credit_card: Crédits : `{Balance}`
> :id: ID d'enregistrement : {UserId}

Affichez à tout moment ces statistiques avec la commande `profil`.
Pour en savoir plus sur les différentes manières d'obtenir plus de crédits, utilisez la commande `work help`.

Amusez-vous bien ! :heart:"""
        await msg.edit(content=a)

def setup(bot):
    bot.add_cog(Datacom(bot))
