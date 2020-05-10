import discord
import asyncio
from discord.ext import commands
import random


client = commands.Bot(command_prefix=">")


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("test"))
    print("bot is ready")

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

@client.command(aliases=["p"])
async def ping(ctx):
    await ctx.send(f'finding your local egirl took {round(client.latency * 1000)}ms')    

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=3):
    await ctx.channel.purge(limit=amount + 1)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"kicked {member} for {reason}")

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"banned {member} for {reason}")

@client.command()
async def poke(ctx):
    await ctx.author.send('boop!')

client.run("TOKEN")
