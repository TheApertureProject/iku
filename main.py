import json
import logging
import os
from os import environ
import discord
from discord.ext import commands

# Configuration des pré-requis

logging.basicConfig(level='INFO')

with open('./config.json', 'r') as cjson:
    config = json.load(cjson)

TOKEN = environ.get("TOKEN")
PREFIX = config["PREFIX"]
MODS = config["MODS"]

# Configuration et connection au bot

bot = commands.Bot(command_prefix='^')

@bot.event
async def on_ready():
    loaded = len(MODS)
    bot.remove_command('help')
    for module in MODS:
        try:
            logging.info('Loading %s', module)
            bot.load_extension(f'modules.{module}')
        except Exception as e:
            logging.exception('Failed to load {} : {}'.format(module, e))
    print('Logged in.')
    print('{}/{} modules loaded'.format(loaded, len(MODS)))
    print(f'discord.py lib version : {discord.__version__}')


bot.run(TOKEN)
