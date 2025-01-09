import random

welcome_templates = [
    "Welcome to our lovely server, {}! 🌟 We've been waiting for someone as special as you!",
    "Look who just walked in! {} is here to steal hearts! 💖",
    "Hey {}! You just made our server 10 times more awesome! ✨",
    "Welcome aboard, {}! Get ready for some fun times! 🎉",
    "Oh my, {}! You're looking absolutely fabulous today! 💫",
    "Roses are red, violets are blue, {} just joined, and we're happy it's you! 🌹"
]

def get_welcome_message(username):
    return random.choice(welcome_templates).format(username)