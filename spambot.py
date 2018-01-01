#mention spammer bot
import discord
import pickle
import random
import asyncio
import os
import time

token = ("enter ur token here")
client = discord.Client()
raidtxt = str(input("plz enter in spam text:"))
spamamt = int(input("plz enter the amt of spam u want:"))
invitelink = str(input("plz enter an invite link for server ud like to raid: "))

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(message):
    if message.content.startswith("+raidhere"):
        for x in range(0, spamamt):
            time.sleep(1)
            await client.send_message(message.channel, raidtxt)

@client.event
async def on_ready():
    await client.accept_invite(invitelink)

client.run(token, bot=False)
