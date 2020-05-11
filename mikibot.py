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

@client.command(aliases=["8ball"])
async def _8ball(ctx):
    responses = ["yes",
                 "maybe",
                 "my sources say no",
                 "my sources say yes",
                 "no",
                 "bitch tf you crazy?"]
    await ctx.send( f" {random.choice(responses)}, "+ctx.message.author.mention)

@client.command(aliases=["roll"])
async def dice(ctx):
    responses = ["1",
                 "2",
                 "3",
                 "4",
                 "5",
                 "6"]
    await ctx.send(f"{random.choice(responses)}")

@client.command(aliases=["cf"])
async def coinflip(ctx):
    responses = ["heads",
                 "tails",]
    await ctx.send(f"{random.choice(responses)}")   

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

@client.command(pass_context=True, aliases=["propaganda"])
async def manifesto(ctx):

  embed = discord.Embed(
    colour = discord.Colour.red()
  )

  embed.set_author(name="Pravda Manifesto Preface")
  embed.add_field(name="uwu", value="The Pravda Union is a conglomeration of United Republics spanning from Eastern Europe and Northern Asia into Siberia. The works of the party have driven the parasites out of her borders and have continued to ensure safety within her beloved empire. The Central Committee and works have exceeded their mortal ambitions, and restored order and prosperity to the vast Union. Pravda stands as a turning point in history, about the enter into a state of hard work and productivity. To accomplish such a remarkable task, we must end the exploitation by the bourgeoisie, spread out socialist ideals and stand victorious over our foes. Workers of the world, unite! ☭")

  await ctx.send(embed=embed)
    
@client.command()
async def slap(ctx, member : discord.Member):
  responses=["https://media.tenor.com/images/bd092fb261df4588a51f9dd1f4815fea/tenor.gif",
  "https://media.tenor.com/images/ac09dd389d43f3bc0adad6432a942532/tenor.gif",
  "https://media.tenor.com/images/6dbd997e3e79f21b7841b244833325c0/tenor.gif",
  "https://media.tenor.com/images/604a56f1e6e594beb00c265ea7a40dca/tenor.gif",
  "https://media.tenor.com/images/56387025912c48b5af27c0711a2645b8/tenor.gif",
  "https://media.tenor.com/images/f8f050aa79f92f3e45669ef8db45ed1e/tenor.gif",
  "https://media.tenor.com/images/79c666d38d5494bad25c5c023c0bbc44/tenor.gif",
  "https://media.tenor.com/images/47698b115e4185036e95111f81baab45/tenor.gif",
  "https://media.tenor.com/images/53b846f3cc11c7c5fe358fc6d458901d/tenor.gif",
  "https://media.tenor.com/images/091e0502e5fda1201ee76f5f26eea195/tenor.gif"]
   embed=discord.Embed(color=0xf4c2c2)
  embed.set_image(url=f"{random.choice(responses)}")
  await ctx.send(f"{member.mention} got slapped by "+ctx.message.author.mention, embed=embed)
 

@client.command(aliases=["simpdetector"])
async def simprate(ctx,member : discord.Member):
  responses = ["1","2","3","4","5","6","7","8","9","10"]
  await ctx.send(f"{member.mention} is {random.choice(responses)} out of 10 a simp")


client.run("TOKEN")
