import os
import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv
import logging

# Load token from .env file
load_dotenv()
TOKEN = os.getenv("MTM2MDk5OTAzNjM5NTQ1NDc3Nw.GUgpdf.1tNkhURlRuU4VA1ol8dY_YTqzVtnxI3I13cJ8E")

# Set up logging
logging.basicConfig(level=logging.INFO)

# Enable intents
intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True

# Set up the bot
bot = commands.Bot(command_prefix="/", intents=intents)

# List of cogs to load
initial_extensions = ["cogs.moderation"]

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")
    try:
        synced = await bot.tree.sync()
        print(f"🔁 Synced {len(synced)} slash command(s).")
    except Exception as e:
        print(f"❌ Command sync failed: {e}")

if __name__ == "__main__":
    for ext in initial_extensions:
        try:
            bot.load_extension(ext)
            print(f"✅ Loaded extension: {ext}")
        except Exception as e:
            print(f"❌ Failed to load {ext}: {e}")

    bot.run(TOKEN)
