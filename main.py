from bot.client import create_bot
from config import TOKEN

def main():
    bot = create_bot()
    bot.run(TOKEN)

if __name__ == "__main__":
    main()