import discord
from discord.ext import commands

class Demo(Cog):

    def __init__(self, bot):
        self.bot = bot

    @bot.command()
    async def ping(self, ctx):
        """Répond 'Ping!'"""
        await ctx.send("Pong!")
    
    @bot.command()
    async def pong(self, ctx):
        """Répond 'Pong!'"""
        await ctx.send("Ping!")

def setup(bot):
    bot.add_cog(Demo(bot))
