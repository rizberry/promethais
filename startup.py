'''
Bot Name: Applesauce
Created By: Matthew
Version: v2.0
Last Updated: June 3, 2020
Created On: October 12, 2019

Please read license.txt for license information
'''
import os
import sys
import time
import discord
import datetime
from discord.ext import commands
from discord.ext.commands import has_permissions
from util.checks import startup
from util.log import startLog, log
from util.db.query import queryPrefix, queryCogList
from util.db.insert import insertCogList
from util import config, exceptions

startLog.info("Booting...\n", console=True)

def get_prefix(bot, message):
    """
    Gets prefix for specific guild
    :return: Prefix to use
    :rtype: str
    """
    return queryPrefix.prefix(message.guild.id)

conf = config.readINI('mainConfig.ini')  # loads config
botName = conf['main']['botname']  # gets bots name from config
bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True)


@bot.event
async def on_ready():
    # starts timer to keep track of startup time
    startTime = time.time()

    # makes sure logs folder is created
    if not os.path.exists("logs"):
        os.mkdir("logs")

    # wipes startup and running log
    log.wipe(conf['logs']['start'])
    log.wipe(conf['logs']['run'])
    startLog.info('Running Checks', console=True)

    # runs startup checks that are in startupchecks.py
    if startup.checks() is False:
        startLog.error("Something isn't configured correctly for startup", console=True)
        startLog.error("Startup aborted", console=True)
    else:
        # writes startup information to startup-log.txt
        startLog.custom(f'Starting {botName}', "[info]", "\n", console=True, tagcolor="cyan")
        startLog.debug(f'Python {sys.version[:6]}', console=True)
        startLog.debug(f'OS {sys.platform}', console=True)
        startLog.debug(f'discord.py {discord.__version__}', console=True)

        # Requires Cogs loading
        # Any file in /cogs/required is considered a required cog
        # These files must ALL be loaded in order for the bot to continue initializing
        startLog.custom('Initializing Required Cogs', "[info]", "\n", console=True, tagcolor="cyan")
        for required in os.listdir('./cogs/required'):
            if required.endswith('.py'):
                try:
                    bot.load_extension(f'cogs.required.{required[:-3]}')
                    startLog.proceed(f'{required}', console=True)
                except Exception as e:
                    startLog.error(f'{required}', console=True)
                    startLog.error(f'{e}', console=True)
                    startLog.error('Startup aborted', console=True)
                    return

        # Main loading
        # Any file in /cogs/main is considered a cog
        # These files are attempted to be loaded. If a file errors then it is skipped and initializing continues
        startLog.custom('Initializing Cogs', "[info]", "\n", console=True, tagcolor="cyan")
        countSuccess = 0
        countFail = 0
        countSkip = 0
        for cog in os.listdir(f'./cogs/main'):
            if cog.endswith('.py'):
                try:
                    value = queryCogList.enabled(cog[:-3])
                except exceptions.CogNotFound:
                    try:
                        insertCogList.cog(cog[:-3], False, False)
                        value = False
                    except exceptions.CogInsertFail:
                        startLog.error(f'{cog} CogInsertFail', console=True)
                        continue

                if value:
                    try:
                        bot.load_extension(f'cogs.main.{cog[:-3]}')
                        insertCogList.loaded(cog[:-3], True)
                        startLog.proceed(f'{cog}', console=True)
                        countSuccess += 1
                    except Exception as e:
                        insertCogList.loaded(cog[:-3], False)
                        startLog.error(f'{cog}', console=True)
                        startLog.error(f'{e}', console=True)
                        countFail += 1
                else:
                    insertCogList.cog(cog[:-3], False, False)
                    startLog.skip(f'{cog}', console=True)
                    countSkip += 1

        startLog.info(f'Success: {countSuccess}  Failed: {countFail}  Skipped: {countSkip}\n', console=True)
        startLog.info(f'{botName} is ready to rumble!', console=True)
        startLog.info(f'Initialized in {int((time.time() - startTime)*1000)}ms', console=True)

# Starts bot with Discord token from mainConfig.ini
bot.run(conf['main']['discordToken'])
