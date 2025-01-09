import discord
from .utils.greetings import get_welcome_message

def setup_events(bot, message_handler):
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

        message_handler.handle_message(message)
        await bot.process_commands(message)