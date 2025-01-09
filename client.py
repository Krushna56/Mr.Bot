import discord
from discord.ext import commands
from .events import setup_events
from .handlers import MessageHandler

def create_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True

    bot = commands.Bot(command_prefix='!', intents=intents)
    message_handler = MessageHandler()
    
    setup_events(bot, message_handler)
    
    return bot