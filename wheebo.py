import discord
import os
import time

from discord import app_commands
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By

# discord setup
client = discord.Client(intents=discord.Intents.default())
tree = app_commands.CommandTree(client)

# selenium setup
display = Display()
display.start()

driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')

# define commands
@tree.command(name = "aws-this-week", description = "What's new in AWS This Week?")
async def awsThisWeek(interaction):
    await interaction.response.defer(ephemeral=True, thinking=True)

    driver.get('https://learn.acloud.guru/series/aws-this-week')
    time.sleep(3)
    
    video_element = driver.find_element(By.CSS_SELECTOR, '.css-uwfm48 a')
    video_link = video_element.get_attribute('href')

    await interaction.followup.send(video_link)

# sync commands
@client.event
async def on_ready():
    await tree.sync()
    print("Ready!")

# start
client.run(os.environ['DISCORD_TOKEN'])
