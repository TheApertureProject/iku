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

    @commands.command()
    async def clear(self, ctx):
        await database.execute("DROP TABLE maindata")
        await database.execute("CREATE TABLE maindata (user_id BIGINT, balance BIGINT, last_daily INT, last_work INT, level INT)")
        await ctx.send("cleared")


    @commands.command(aliases=["start"])
    async def register(self, ctx):

        msg = await ctx.send("<a:loading:712211273743597618> | Création de votre profil utilisateur en cours.")

        UserId = ctx.author.id
        Balance = 0
        Level = 1

        try:
            await database.execute("INSERT INTO maindata (user_id, balance, level) VALUES ({}, {}, {})".format(UserId, Balance, Level))
        except Exception as e:
            print(e)
        a = f""":white_check_mark: | Votre profil a bien été créé, {ctx.author.mention}. Voici vos statistiques de départ :

> :heart_decoration: Rang : `{Level}`
> :credit_card: Crédits : `{Balance}`
> :id: ID d'enregistrement : {UserId}

Affichez à tout moment ces statistiques avec la commande `profil`.
Pour en savoir plus sur les différentes manières d'obtenir plus de crédits, utilisez la commande `work help`.

Amusez-vous bien ! :heart:"""
        await msg.edit(content=a)

def setup(bot):
    bot.add_cog(Datacom(bot))
