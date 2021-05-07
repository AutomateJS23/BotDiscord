import discord 
from discord.ext import commands 

bot = commands.Bot(command_prefix='mina>')

@bot.event 
async def on_ready():
    print('Bot Started!')

@bot.event
async def on_message(message):
    await bot.process_commands(message)

@bot.command()
async def echo(ctx,*,message):
    await ctx.send(message)

@bot.command()
async def clear(ctx,limit=5):
    await ctx.channel.purge(limit=limit)

@bot.command()
async def hi(ctx):
    await ctx.send('Hi ><')

bot.run('yourBotToken')
print('finis')
print('finis2')
print('test 3')