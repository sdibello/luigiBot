# Luigi-small.py
import os
import discord
import random
import json
import aiohttp 
import time
import sys
import asyncio
import logging
from dotenv import load_dotenv
from discord.ext import commands
from random import randint
from collections import namedtuple


#load env
load_dotenv()
#environment settings
luigi_version = "1.0.1"
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
DND_API_URL = os.getenv('DND_API_URL')

# attack processing section
att_dict = {}
Attacks = namedtuple('Attacks', ['att', 'crit'])
# setting up bot command key
bot = commands.Bot(command_prefix='!',case_insensitive='true')
#logging
root = logging.getLogger()
root.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

bot.run(TOKEN)