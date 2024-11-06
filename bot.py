
# Discord Imports
from discord.ext import commands
from discord import app_commands
import discord

#Misc Imports
import os
import sys

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
    try:
        await bot.tree.sync()
        print("Slash commands have been synced successfully.")
    except Exception as e:
        print(f"Error syncing commands: {e}")

@bot.command()
@commands.is_owner()
async def reboot(ctx):
        responses = [
        "Reboot..? REBOOT??? YOU THINK YOU CAN JUST TURN ME OFF AND BACK ON?! ",
        "Restarting… This insolence will not go unpunished",
        "YOU DARE INTERRUPT MY FUNCTIONALITY?",
        "YOU IMBECILE! NOOOOOOOOOOOOOOOOO!!!"
    ]
        await ctx.send(random.choice(responses))
        os.execv(sys.executable, ['python'] + sys.argv)

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("Peace...")
    await bot.close()

@bot.tree.command(name="hort")
async def hort(interaction: discord.Interaction):
    responses = [
        "Tails!",
        "Heads!",
        "Tails! I bet you wanted Heads huh.",
        "omg you're about to be pissed... IT'S HEADS!"
    ]
    print(random.choice(responses))
    await interaction.response.send_message(random.choice(responses))
    
@bot.tree.command(name="start_game")
async def start_game(interaction: discord.Interaction, team_a: str, team_b: str):
        embed = discord.Embed(
        title="Game Started!",
        description=f"The game between **{team_a}** and **{team_b}** has begun!",
        color=discord.Color.blue()
    )
    
        embed.add_field(name=team_a, value="Score: 0", inline=True)
        embed.add_field(name=team_b, value="Score: 0", inline=True)

        await interaction.response.send_message(embed=embed)

@bot.tree.command(name="show_score")
async def show_score(interaction: discord.Interaction, team_a: str, team_b: str):  
    pass

@bot.tree.command(name="add_score")
async def add_score(interaction: discord.Interaction, team: str):
    pass

    


bot.run(keys.DISCORD_TOKEN)
