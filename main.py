import json
import logging
import os
import discord
from discord import Commands

# Configuration des pré-requis

logging.basicConfig(level='INFO')

with open('./config.json', 'r') as cjson:
    config = json.load(cjson)

TOKEN = os.environ["TOKEN"]
PREFIX = config["prefix"]
MODS = config["mods"]

# Configuration et connection au bot

bot = discord.Client(prefix='^')

@bot.event
async def on_ready():
    loaded = len(MODS)
    bot.remove_command('help')
    for module in modules:
        try:
            logging.info('Loading %s', module)
            bot.load_extension(f'modules.{module}')
        except Exception as e:
            logging.exception('Failed to load {} : {}'.format(module, e))
    print('Logged in.')
    print('{}/{} modules loaded'.format(loaded, len(modules)))
    print(f'discord.py lib version : {discord.__version__}')
    bot.loop.create_task(status())


bot.run(TOKEN)
