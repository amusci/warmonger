
# Discord Imports
from discord.ext import commands
import discord

# Python
import random

# Keys

import keys

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("Peace...")
    quit()

@bot.command()
async def hort(ctx):
    responses = [
        "Tails!",
        "Heads!",
        "Tails! I bet you wanted Heads huh.",
        "omg you're about to be pissed... IT'S HEADS!"
    ]
    await ctx.send(random.choice(responses))
    
    

bot.run(keys.DISCORD_TOKEN)
