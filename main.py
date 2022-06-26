#The Great Wizard Tuss Source Code (Written In Python) by: TheLinuxPirate
from email import message
from http import client
import importlib
from pydoc import cli
from bleach import clean
from cairo import Status
from click import command
from discord.ext import commands, tasks
import discord
import random
import os
from itertools import cycle
import asyncio
import nacl

client = commands.Bot(command_prefix = ';')
Status = cycle(['Try typing \";ayuda\"', 'Hello World!', 'SHAZAMN!', 'Fool me once, fool me twice, fool the fool!', 'Me when the', 'As a wize wizard once said: \"Stop using Windows\"', 'The \"ayuda\" command was orginally named \"halp\"', 'Did you know I was created in one day?', 'Which State In The US Is The Smallest?'])

#Original on_ready: await client.change_presence(status=discord.Status.idle, activity=discord.Game("Hello World!"))

#StartUp Command = Online
@client.event 
async def on_ready():
    await client.change_presence(status=discord.Status.idle)
    change_status.start()
    print("A Wild Great Wizard Tuss Has Appeared!")

#Discord Status Continous Change; Seconds = How Often Status Changes
@tasks.loop(seconds=40)
async def change_status():
    await client.change_presence(activity=discord.Game(next(Status)))

#Discord Bot Joins The Voice Channel
@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send(f'Connected to \"{channel}\"!')

#Discord Bot Leaves The Voice Channel
@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    await ctx.send(f'Disconnected from Voice Channel!')

#Latency Speed Test (Message)       
@client.command()
async def speedtest(ctx):
    await ctx.send(f'Ding! {round(client.latency * 1000)}ms')

#Funny Troll: Yayo Command
@client.command()
async def yayo(ctx):
    await ctx.send("fr fr")

#Ayuda Command Displaying "All" Commands
@client.command()
async def ayuda(ctx):
    await ctx.send("Welcome to FanelMachine's ayuda prefix!\n FanelMachine's command prefix is the: \";\"\n\nThe commands that are available as of now are:\n ayuda: Will show this message\nspeedtest: Displays latency speed of message\n8ball: Ask the 8ball a question!\nclear: The clear command will delete messages, type clear and the amount of numbers you'd like to delete (The default value is 5)\nkick: The kick command will kick a user, and you can add the reason to report to aduit log\nban: The ban command will ban a user, and you can add the reason to report to aduit log\n join: The join command will join the user's voice channel\n leave: The leave command will make Tuss leave the voice channel\n")

#Simple 8ball command: May Change Name To Fortune
@client.command(aliases=['8ball'])
async def eightball(ctx, *, question):
    client.responses = [ 'It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes definitely.', 'You may rely on it.', 'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', 'Don\'t count on it.', 'My reply is no.', 'My sources say no.', 'Outlook not so good. Very doubtful.']    
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(client.responses)}')

#DEFAULT RESPONSES: client.responses = [ 'It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes definitely.', 'You may rely on it.', 'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', 'Don\'t count on it.', 'My reply is no.', 'My sources say no.', 'Outlook not so good. Very doubtful.']

#Purge/Clear Command
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

#Moderation: Kick Command    
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send (f'Wiggly Doogly Poo {member} has been kicked from this server!')
#Moderation: Ban Command    
@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send (f'Wiggly Doogly Doo {member} has been banned from this server!')

#Cogs? Unused: LEAVE COMMENTED SECTION ALONE     
#@client.command
#async def unload(ctx, extension):
#    client.unload_extension(f'cogs.{extension}')
#            
#@client.command
#async def load(ctx, extension):
#    client.load_extension(f'cogs.{extension}')

#Terminal Message When A Member Joins A Server
@client.event
async def on_member_join(member):
    print(f'(member) has joined a server')

#Terminal Message When A Member Leaves A Server    
@client.event
async def on_member_remove(member):
    print(f'(member) has exited a server')

#Command That Runs The Bot/ IF YOU COPY AND PASTED THIS CODE INTO ANOTHER BOT DELETE THE ('') CONTENT AND REPLACE IT WITH YOUR BOT'S TOKEN!   
client.run('NzQ3MTEzNDEyNzIyNjg4MDgw.GXZM5O.4FpICAuLLJC9BcsVLySBBErclWr8ypySoGaTBc')