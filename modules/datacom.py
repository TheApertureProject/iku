import discord
from discord.ext import commands
from discord.ext.commands import Cog
from databases import Database
import asyncio
import aiomysql
import os

class Datacom(Cog):

    def __init__(self, bot):
        self.bot = bot
        self.db = None
        bot.loop.create_task(self.load())

    async def cog_check(self, ctx):
        return self.db is not None

    async def load(self):
        self.db = await aiomysql.create_pool(
            host=os.environ["DB_HOST"],
            port=os.environ["DB_PORT"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"],
            db=os.environ["DB_NAME"],
            loop=asyncio.get_event_loop(),
            autocommit=True
            )

    @commands.command(aliases=["start"])
    async def register(self, ctx):

        UserId = ctx.author.id

        msg = await ctx.send("<a:loading:712211273743597618> | Création de votre profil utilisateur en cours.")

        async with bot.db.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute("SELECT user_id FROM maindata WHERE user_id = %s", (user.id))
                user_id = await cur.fetchone()

        if user_id == UserId:
            await msg.edit(content="<:white_cross_mark:713026754763030629> | Votre profil existe déjà.")
            return

        Balance = 0
        Level = 1

        await bot.db.execute("INSERT INTO maindata (user_id, balance, level) VALUES (%s, %s, %s)", (UserId, Balance, Level))

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
