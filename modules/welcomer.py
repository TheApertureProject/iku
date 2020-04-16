import discord
from discord import commands

class Welcomer(Cog):

    @Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 466600971213209600:

            large_message = self.bot.get_channel(466603496322498561)
            await large_message.send(f""":arrow_right: Bienvenue sur Aperture, {member.mention} !
            Voici quelques salons à lire avant toute chose : <#539929961512042506> | <#697087325246849084>
            Des rôles sont aussi disponibles. <#699609186907979797>
            Profitez-bien et n'hésitez pas à contacter l'équipe en cas de question ou problème :)""")

            short_message = self.bot.get_channel(466600971213209602)
            await short_message.send(f"Bienvenue, {member.mention} :D")

    @Cog.listener()
    async def on_member_leave(self, member):
        if member.guild.id == 466600971213209600:
            
            leave_message = self.bot.get_channel(466603496322498561)
            await leave_message.send(f":wheelchair: {member.name} a quitté le serveur.")

def setup(bot):
    bot.add_cog(Welcomer(bot))
