import discord
from discord.ext import commands
from discord.ext.commands import Cog

class Welcomer(Cog):

    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 466600971213209600:

            short_message = aperture_id.get_channel(466600971213209602)
            await short_message.send(f"Bienvenue, {member.mention} :D")

            private_message = """Hey !

Je n'ai pu m'empêcher de remarquer que tu venais de rejoindre **aperture** ! Bienvenue à toi :)

Avant toute chose, je te conseille de te présenter dans le salon <#467021094793117707> en respectant le modèle suivant :
```**Nom :**
**Genre :**
**Année de naissance :**
**Localisation :**
**Centres d'intérêts :**
**Goûts musicaux :**```
(cela aidera les autres membres à mieux te connaître !)

Bisous et profite bien de notre serveur !"""
            
            await member.send(private_message)

    @Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.id == 466600971213209600:
            
            aperture_id = self.bot.get_guild(466600971213209600)
            leave_message = aperture_id.get_channel(466603496322498561)
            await leave_message.send(f":wheelchair: {member.name} a quitté le serveur.")

def setup(bot):
    bot.add_cog(Welcomer(bot))
