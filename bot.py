
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

team_points = {}
    
@bot.tree.command(name="start_game")
async def start_game(interaction: discord.Interaction, team_a: str, team_b: str):

    team_points[team_a] = 0
    team_points[team_b] = 0

    embed = discord.Embed(
        title="War Started!",
        description=f"The war between **{team_a}** and **{team_b}** has begun!",
        color=discord.Color.red()
    )
    await interaction.response.send_message(embed=embed)
    await interaction.channel.send(f"@everyone The war between **{team_a}** and **{team_b}** has begun!")



@bot.tree.command(name="add_points")
async def add_points(interaction: discord.Interaction, team: str):
    if team in team_points:
        
        team_points[team] += 1

        
        if team_points[team] >= 7:
            winner_embed = discord.Embed(
                title="Game Over!",
                description=f"**{team}** has won war.",
                color=discord.Color.gold()
            )
            
            
            team_names = list(team_points.keys())
            score_display = f"**{team_names[0]}** {team_points[team_names[0]]} - {team_points[team_names[1]]} **{team_names[1]}**"
            winner_embed.add_field(name="Final Score", value=score_display, inline=False)

            await interaction.response.send_message(embed=winner_embed)

            
            team_points.clear()
        else:
            
            team_names = list(team_points.keys())
            score_display = f"**{team_names[0]}** {team_points[team_names[0]]} - {team_points[team_names[1]]} **{team_names[1]}**"
            
            embed = discord.Embed(
                title="Points Updated!",
                description=f"**{team}** has won the last game!",
                color=discord.Color.green()
            )
            
            embed.add_field(name="Current Score", value=score_display, inline=True)
            await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message(f"Team **{team}** not found. Please start the game first using /start_game.")


@bot.tree.command(name="show_score")
async def show_score(interaction: discord.Interaction, team_a: str, team_b: str):
    if team_a in team_points and team_b in team_points:

        score_display = f"**{team_a}** {team_points[team_a]} - {team_points[team_b]} **{team_b}**"

        embed = discord.Embed(
            title="Current Score",
            description=f"Score for the game between **{team_a}** and **{team_b}**:",
            color=discord.Color.blue()
        )
        
        embed.add_field(name="Current Score", value=score_display, inline=True)
        
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message(f"War has not started or one of the teams was not found. Please start the war first using /start_game.")




bot.run(keys.DISCORD_TOKEN)
