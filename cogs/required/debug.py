import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import sys

class Debug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # commands
    # debug - prints some useful debugging information
    @commands.command(name="debug", description="version and debug information", usage="debug")
    @commands.is_owner()
    async def debug(self, ctx):
        embed=discord.Embed(title='Debug', color=0xc1c100)
        embed.add_field(name='discord.py version', value=f'{discord.__version__}', inline=False)
        embed.add_field(name='python version', value=f'{sys.version}', inline=False)
        await ctx.send(embed=embed)

    # guildid - prints the guilds id
    @commands.command(name="guildid", description="gets guild ID", usage="guildid")
    @commands.is_owner()
    async def guildid(self, ctx):
        await ctx.send(f'Guild id: {ctx.guild.id}')

def setup(bot):
    bot.add_cog(Debug(bot))
