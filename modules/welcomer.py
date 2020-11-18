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
            await join_message.send(f":arrow_lower_right: {member.name}#{member.discriminator} a rejoint le serveur.")

            private_message = """Hey, bienvenue à toi sur Aperture.

Avant toute chose, je t'invite à te présenter — ça  aidera les autres membres à mieux te connaître.

Pour ce faire, copie-colle et remplis le modèle ci-dessous dans le salon <#467021094793117707>.

Bisous et profite bien de notre serveur !"""

            presentation = """```Markdown
**Nom :**
**Genre :**
**Année de naissance :**
**Localisation :**
**Centres d'intérêts :**
**Maîtrises artistiques :**
**Goûts musicaux :**```"""

            await member.send(private_message)
            await member.send(presentation)

    @Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.id == 466600971213209600:

            leave_message = self.bot.get_channel(466603496322498561)
            await leave_message.send(f":wheelchair: {member.name}#{member.discriminator} a quitté le serveur.")

def setup(bot):
    bot.add_cog(Welcomer(bot))
