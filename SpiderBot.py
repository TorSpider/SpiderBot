#!/usr/bin/env python3

''' SpiderBot.py
    A bot for Discord that interfaces with the TorSpider service.
'''

import discord
from discord.ext import commands
import logging
import asyncio
import sys


# Set up logger


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


# Grab token from arguments


if len(sys.argv) == 2:
    token = sys.argv[1]
elif len(sys.argv) > 2:
    print("Too many arguments passed")
    sys.exit(0)
else:
    print("Token not provided")
    sys.exit(0)


# Main code


bot = discord.Client()

@bot.event
async def on_connect():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_ready():
    print("Bot ready")
    print('------')

@bot.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await message.channel.send('Calculating messages...')
        async for log in message.channel.history(limit=100):
            if log.author == message.author:
                counter += 1

        await tmp.edit(content='You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await message.channel.send('Done sleeping')

if __name__ == "__main__":
    bot.run(token)
