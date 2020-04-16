import discord
from discord import commands

class Errors(Cog):

    @Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f'{redcross} | Vérifiez la commande et réessayez.')
        elif isinstance(error, commands.CommandNotFound):
            await ctx.message.add_reaction('❓')
        elif isinstance(error, commands.CheckFailure):
            await ctx.send(f'{redcross} | Vous n\'êtes pas autorisé.e à utiliser cette commande.')
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'{redcross} | Un argument requis est manquant.')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{redcross} | Vous n\'êtes pas autorisé.e à utiliser cette commande.')
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(f'{redcross} | Je n\'ai pas les permissions suffisantes pour effectuer cette commande.')
        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.send(f'{redcross} | Cette commande n\'est pas utilisable par message privé.')
        else:
            embedbasic = discord.Embed(color=discord.Color.red(),
                                       description='⚠ | Une erreur inconnue s\'est produite. Les développeurs en ont été notifiés :)')
            errorembed = discord.Embed(color=discord.Color.red(),
                                       title=f'Erreur causée par `{ctx.author}` ({ctx.author.id})',
                                       description=f'```py\n{error}\n```')
            errorembed.add_field(name='Serveur', value=f'**`{ctx.guild.name}`** ({ctx.guild.id})', inline=True)
            errorembed.add_field(name='Commande', value=f'**{ctx.command.name}**')
            channel = ctx.bot.get_channel(700344314630373536)
            await ctx.send(embed=embedbasic)
            await channel.send(embed=errorembed)


def setup(bot):
    bot.add_cog(Errors(bot))
