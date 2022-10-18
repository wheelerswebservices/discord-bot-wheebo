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
async def scrape(interaction, name):
    await interaction.response.defer(ephemeral=True, thinking=True)

    driver.get(f'https://learn.acloud.guru/series/${name}')
    time.sleep(3)

    video_element = driver.find_element(By.CSS_SELECTOR, '.css-uwfm48 a')
    video_link = video_element.get_attribute('href')

    await interaction.followup.send(video_link, ephemeral=False)

@tree.command(name = "aws-this-week", description = "What's new in AWS this Week?")
async def aws_this_week(interaction):
    await scrape(interaction, 'aws-this-week')

@tree.command(name = "azure-this-week", description = "What's new in Azure this Week?")
async def azure_this_week(interaction):
    await scrape(interaction, 'azure-this-week')

@tree.command(name = "gcp-this-month", description = "What's new in GCP this Month?")
async def gcp_this_month(interaction):
    await scrape(interaction, 'gcp-this-month')

@tree.command(name = "kubernetes-this-month", description = "What's new in Kubernetes this Month?")
async def kubernetes_this_month(interaction):
    await scrape(interaction, 'kubernetes-this-month')

@tree.command(name = "linux-this-month", description = "What's new in Linux this Month?")
async def linux_this_month(interaction):
    await scrape(interaction, 'linux-this-month')

# sync commands
@client.event
async def on_ready():
    await tree.sync()
    print("Ready!")

# start
client.run(os.environ['DISCORD_TOKEN'])
