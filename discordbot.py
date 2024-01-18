import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='!')

# Event - wywołuje się po uruchomieniu bota
@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user.name}')

# Komenda - wywołuje się po wpisaniu !hello na serwerze
@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

# Uruchomienie bota z tokenem
bot.run('YOUR_BOT_TOKEN')