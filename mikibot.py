import discord
import asyncio
from discord.ext import commands
import random


client = commands.Bot(command_prefix=">")


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("test"))
    print("bot is ready")

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

client.run("NzA5MDkwNTcwNjQ3MjQwNzQ1.Xrg2FA.TgMgkpXYzTtIbS2H2PcMLyJL-2w")