import discord
from discord.ext import commands
from discord.ext.commands import Cog
from databases import Database
import os

sql_connect_url = os.environ["JAWSDB_URL"]

database = Database(sql_connect_url)
await database.connect()

class Datacom(Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["start"])
    async def register(self, ctx):
        msg = await ctx.send("<a:loading:712211273743597618> | Création de votre profil utilisateur en cours.")
        try:
            database.execute("INSERT INTO data(UserId, Money, Level), VALUES({}, {}, {})".format(ctx.author.id, 1000, 1))
        except Exception as e:
            print(e)
        a = f""":white_check_mark: | Votre profil a bien été créé, {ctx.author.mention}. Voici vos statistiques de départ :

> :heart_decoration: Rang : `1`
> :credit_card: Crédits : `1000`

Affichez à tout moment ces statistiques avec la commande `profil`.
Pour en savoir plus sur les différentes manières d'obtenir plus de crédits, utilisez la commande `work help`.

Amusez-vous bien ! :heart:"""
        await msg.edit(content=a)

def setup(bot):
    bot.add_cog(Datacom(bot))
