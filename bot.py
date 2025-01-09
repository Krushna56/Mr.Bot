import discord
from discord.ext import commands
import random
from message_handler import MessageHandler
from greetings import get_welcome_message
from config import TOKEN

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)
message_handler = MessageHandler()

@bot.event
async def on_ready():
    print(f'{bot.user} is ready and online!')

@bot.event
async def on_member_join(member):
    welcome_channel = discord.utils.get(member.guild.channels, name='welcome')
    if welcome_channel:
        welcome_msg = get_welcome_message(member.name)
        await welcome_channel.send(welcome_msg)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Store message in history
    message_handler.add_message(message.author.name, message.content)
    
    # 30% chance to respond to messages
    if random.random() < 0.3:
        response = message_handler.generate_response(message.content)
        await message.channel.send(response)

    await bot.process_commands(message)

# Run the bot
bot.run(TOKEN)