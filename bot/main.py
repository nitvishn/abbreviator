import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix=".")
token = os.getenv("DISCORD_BOT_TOKEN")

def abbreviate(S):
    if S.strip() == "":
        return '\n'
    line = ""
    for word in S.strip().split(' '):
        word = word[0].upper() if len(word) == 1 else word[0].upper() + word[1:]
        line+=word[0].upper()
        # for char in word:
        #     if not char.isalpha():
        #         line += char
    return line

@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("Listening to .help"))
    print("I am online")

@client.command()
async def ping(ctx) :
    await ctx.send(f"🏓 Pong with {str(round(client.latency, 2))} also who tf cares, @nitvishn's ping is the best")

@client.command(name="whoami")
async def whoami(ctx) :
    await ctx.send(f"You are {ctx.message.author.name}")

@client.command()
async def clear(ctx, amount=3) :
    await ctx.channel.purge(limit=amount)

@client.command()
async def abb(ctx):
    for line in ctx.message.content[5:].split('\n'):
        await ctx.send(f"{abbreviate(line)}")


client.run(token)
