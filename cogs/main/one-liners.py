'''
Name: One Liners
Description: random "one liner" commands
Last Updated: January 12, 2020
Created: October 30, 2019
'''
import discord
from discord.ext import commands
from utils import commandchecks
import random

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # chance
    @commands.check(commandchecks.isAllowed)
    @commands.command(name="chance", description="Random integer between 0 and 100 (displayed as percent)", usage="chance")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def chance(self, ctx):
        await ctx.send(f'{random.randint(0, 100)}% chance')

    # coin
    @commands.check(commandchecks.isAllowed)
    @commands.command(name="coin", description="Flips a coin and returns heads or tails.", usage="coin")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def coin(self, ctx):
        await ctx.send(random.choice(['heads', 'tails']))
        
    # DDOS
    @commands.check(commandchecks.isAllowed)
    @commands.command(name="ddos", description="You ever wanted to DDoS something? Well today is your lucky day!", usage="ddos <what-to-DDOS>")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ddos(self, ctx, *, name):
        await ctx.send(f'{name} is being DDoSed')

    # hank
    @commands.check(commandchecks.isAllowed)
    @commands.command(name="hank", description="<:hank:651284638958092301>", usage="hank")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def hank(self, ctx):
        await ctx.send('<:hank:651284638958092301>')

    # mushroom
    @commands.check(commandchecks.isAllowed)
    @commands.command(name="mushroom", description="<a:mushroomDance:659932848035463198>", usage="mushroom", aliases=['shroom'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def mushroom(self, ctx):
        await ctx.send('<a:mushroomDance:659932848035463198>')

    # ping
    @commands.check(commandchecks.isAllowed)
    @commands.command(name="ping", description="pong", usage="ping")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ping(self, ctx):
        await ctx.send('pong!')

    # rate
    @commands.check(commandchecks.isAllowed)
    @commands.command(name="rate", description="Random integer rating out of 10.", usage="rate", aliases=['rating'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def rate(self, ctx):
        await ctx.send(f'{random.randint(0,10)}/10')

    # saber
    @commands.check(commandchecks.isAllowed)
    @commands.command(name="saber", description="<a:pepelightsaber:663496095065964585>", usage="saber")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def saber(self, ctx):
        await ctx.send('<a:pepelightsaber:663496095065964585>')

def setup(bot):
    bot.add_cog(Basic(bot))