#mention spammer bot
import discord
import pickle
import random
import asyncio
import os
import time

token = ("eneter ur token here")
client = discord.Client()
raidtxt = str(input("plz enter in spam text:"))
spamamt = int(input("plz eneter the amt of spam u want"))

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(message):
    if message.content.startswith("+raidhere"):
        for x in range(0, spamamt):
            time.sleep(1)
            await client.send_message(message.channel, raidtxt)

client.run(token, bot=False)
