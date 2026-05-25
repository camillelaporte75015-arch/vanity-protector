import discord
from discord.ext import commands
import json
import asyncio
import os
from utils.vanity_manager import VanityManager
from utils.logger import Logger
from utils.commands import CommandHandler

# Charger la configuration
with open('config.json', 'r') as f:
    config = json.load(f)

# Initialiser les modules
vanity_manager = VanityManager(config)
logger = Logger(config)
command_handler = CommandHandler(config, vanity_manager, logger)

# Initialiser le bot
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='&', intents=intents)

@bot.event
async def on_ready():
    print(f"Bot connecté en tant que {bot.user}")
    await vanity_manager.load_current_vanity()  # Charger le vanity actuel au démarrage

@bot.event
async def on_member_update(before, after):
    if before.nick != after.nick:  # Détection des changements de vanity
        await vanity_manager.check_vanity_change(before, after)

# Charger les commandes
bot.load_extension('utils.commands')

# Démarrer le bot
bot.run(os.getenv('TOKEN'))
