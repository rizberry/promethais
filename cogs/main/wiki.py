'''
Name: Wikipedia
Description: Wikipedia command
Last Updated: January 11, 2020
Created: October 30, 2019
'''
import discord
from discord.ext import commands
from utils import commandchecks
import wikipedia

class Wiki(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # wikipedia command
    @commands.check(commandchecks.isAllowed)
    @commands.command(name="wikipedia", description="Queries Wikipedia and returns summary and link to the page.", usage="wikipedia <query>", aliases=['wiki'])
    @commands.cooldown(1, 10, commands.BucketType.default)
    async def wikipedia(self, ctx, *, lookup):
        loading = await ctx.send('Searching for article....') # loading message

        try:
            page = wikipedia.summary(lookup, sentences=1) # gets pages first sentence
            wikiPage = wikipedia.page(lookup)
            pageURL = wikiPage.url # gets pages URL
            pageTitle = wikiPage.title
        except:
            # if nothing is found
            page = 'No results found.'
            pageURL = ''
            pageTitle = ''

        # embed for results
        embed=discord.Embed(title='Wikipedia', description=f'{pageURL}', color=0xc1c100)
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Wikipedia-logo-v2.svg/1200px-Wikipedia-logo-v2.svg.png")
        # embed.add_field(name='Lookup', value=f'{lookup}', inline=False)
        embed.add_field(name=f'{pageTitle}', value=f'{page}', inline=False)
        await ctx.send(embed=embed)

        await loading.delete() # deletes loading message

def setup(bot):
    bot.add_cog(Wiki(bot))