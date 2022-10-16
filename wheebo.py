import discord
import os

from discord import app_commands


intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name = "ping", description = "ping command")
async def ping(interaction):
    await interaction.response.send_message("pong")

@client.event
async def on_ready():
    await tree.sync()
    print("Ready!")

client.run(os.environ['DISCORD_TOKEN'])
