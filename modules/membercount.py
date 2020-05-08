import discord
from discord.ext import commands
from discord.ext.commands import Cog

class Membercount(Cog):

    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 466600971213209600:
            aperture_id = self.bot.get_guild(466600971213209600)
            mc_channel = aperture_id.get_channel(466650918989856789)
            for member in guild.members:
                if member.bot:
                    bot_count = bot_count + 1
                user_count = member.guild.member_count - bot_count
            await mc_channel.edit(name = f"👥 {user_count} membres")

    @Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.id == 466600971213209600:
            aperture_id = self.bot.get_guild(466600971213209600)
            mc_channel = aperture_id.get_channel(466650918989856789)
            for member in guild.members:
                if member.bot:
                    bot_count = bot_count + 1
                user_count = member.guild.member_count - bot_count
            await mc_channel.edit(name = f"👥 {user_count} membres")

def setup(bot):
    bot.add_cog(Membercount(bot))
