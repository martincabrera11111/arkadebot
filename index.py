import os
from discord.ext import commands
from dotenv import load_dotenv
import urllib.request


bot = commands.Bot(command_prefix='+')

@bot.command(name='suma')
async def sumar(ctx, num1, num2):
    response = int(num1)+int(num2)
    await ctx.send(response)

bot.run('ODQzMTk1NTk2NDI0NzQwODc0.YKAVGA.2njS0ops1GrNnuil5rh1Yd-IXac')