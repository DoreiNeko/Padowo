#!/bin/python3
import discord, json, os
from discord.ext import commands
import asyncio

if __name__ == "__main__":

    # Read the configuration file and load it
    # as bot_info
    config_path = f'{os.path.dirname(__file__)}/config.json'
    cogs_path = f'{os.path.dirname(__file__)}/cogs'
    
    with open(config_path, "r") as x:
        bot_info = json.load(x)
    
    # Set the intents of the bot
    intents = discord.Intents.default()
    intents.message_content = True
    intents.voice_states = True
    
    bot = commands.Bot(command_prefix=f'{bot_info["prefix"]}', intents=intents)
    
    # Bot startup information
    @bot.event
    async def on_ready():
        print(f'\n\nBot created by {bot_info["creator"]}')
        print(f'Successfully connected as {bot.user}')
        print("----------------------------------------------")
        print(f'The bot ping is {round(bot.latency * 1000)}ms')
        print(f'The current prefix is {bot_info["prefix"]}')
        await bot.change_presence(activity=discord.Game(name="!help to see a list of commands"))

    async def load():
        for filename in os.listdir(cogs_path):
            if filename.endswith('.py'):
                await bot.load_extension(f'cogs.{filename[:-3]}')

    async def main():
        await load()
        await bot.start(bot_info["token"])
    
    asyncio.run(main())