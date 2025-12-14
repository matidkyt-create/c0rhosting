

import discord
from discord.ext import commands, tasks
import os
import asyncio
from itertools import cycle
token = "MTQzMDU5MzE2OTU5ODE4OTcyMA.GHQhM0.uMhYj6HhiFvj_E1YOpG6YRLEJCfoYPFyYU0AmA"
invitelink = "https://discord.com/oauth2/authorize?client_id=1430593169598189720&permissions=8&integration_type=0&scope=bot"
bot = commands.Bot(command_prefix="c.", intents=discord.Intents.all())
bot_statuses = cycle(["101% Accurate", "Supercharged!"])

@tasks.loop(seconds=30)
async def change_bot_status():
    await bot.change_presence(activity=discord.Game(next(bot_statuses)))

@bot.event
async def on_ready():
    print("CorBot Went Online")
    change_bot_status.start()

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load()
        await bot.start(token)

asyncio.run(main())

