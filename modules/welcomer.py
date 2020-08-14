import discord
from discord.ext import commands
from discord.ext.commands import Cog

class Welcomer(Cog):

    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 466600971213209600:

            short_message = self.bot.get_channel(466600971213209602)
            join_message = self.bot.get_channel(466603496322498561)
            
            await short_message.send(f"Bienvenue, {member.mention} :D")
            await join_message.send(f":arrow_lower_right: {member.idname} a rejoint le serveur.")

            private_message = """Hey !

Je n'ai pu m'empêcher de remarquer que tu venais de rejoindre **aperture** ! Bienvenue à toi :)

Avant toute chose, je t'invite à te présenter dans le salon <#467021094793117707> — **c'est obligatoire pour accéder au reste du serveur**, et cela aidera les autres membres à mieux te connaître.

Utilise ce modèle. Si tu souhaites ne pas préciser certaines infos, mets un tiret à l'endroit voulu :
```**Nom :**
**Genre :**
**Année de naissance :**
**Localisation :**
**Centres d'intérêts :**
**Goûts musicaux :**```

Bisous et profite bien de notre serveur !"""

            await member.send(private_message)

    @Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.id == 466600971213209600:

            leave_message = self.bot.get_channel(466603496322498561)
            await leave_message.send(f":wheelchair: {member.idname} a quitté le serveur.")

def setup(bot):
    bot.add_cog(Welcomer(bot))
