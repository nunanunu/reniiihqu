import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
from discord.ext.commands import Bot
import asyncio
import time

startup_extensions = ["Music"]
bot = commands.Bot(">")


@bot.event
async def on_ready():
    print("Bot is online")

class Main_Commands():
    def __init__(self, bot):
        self.bot = bot

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("pong")

@bot.command(pass_context=True)
async def hello(ctx):
    await bot.say("hi :wave:")

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{} :{}' .format(type(e).__name___, e)
            print('Failed to load extension {}\n{}'.format(extension,exc))


bot.run("NDg3MTY3NTk4ODI0MjU5NTg1.DnJuCQ.4K0nLZ8fPiCBOXNXLsDIbOQUWWA") #Insert your bots token here
