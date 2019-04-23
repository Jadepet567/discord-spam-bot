import discord
import sys
import time
import asyncio

token = ("NTI5MzMwMzE2OTQ3NDg4NzY4.XL8Q1g.yBJYv42c8w1f72Er0-TdUkWvz5o")
client = discord.Client()
raidtxt = str(input("Enter in spam text:"))
spamamt = int(input("Enter the amt of spam u want:"))

@client.event
async def on_ready():
    print("Bot is ready.")
    print("Use +start to run the bot.")
    print("Use +stop to stop the bot.")

@client.event
async def on_message(message):
    if message.content.startswith("+start"):
        for x in range(0, spamamt):
            time.sleep(1)
            await client.send_message(message.channel, raidtxt)
    if message.content.startswith("+stop"):         
        sys.exit()   

client.run(token, bot=False)
