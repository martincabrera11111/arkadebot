import discord
import os

from dotenv
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='+')

@bot.command(name='suma')
async def sumar(ctx, num1, num2):
    response = int(num1)+int(num2)
    await ctx.send(response)

bot.run(TOKEN)