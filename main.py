
import discord
from discord.ext import commands


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='-',intents=intents)

@bot.event
async def on_ready():
    print(">>Chem is online<<")
    

@bot.command()
async def ping(ctx):
    await ctx.send(F'{bot.latency*1000} ms')

@bot.command()
async def hel(ctx):
    await ctx.send(f'calc for calculate (with +, -, *, /)\nping for the bot latency')



bot.run('MTA1MTk5MTUzMTQzNjkwODY4NA.GIDfhB.OLgEFq6aX1GhdntajTiygVk_u_FEArQK41mU28')