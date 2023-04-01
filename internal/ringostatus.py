import asyncio
import nextcord as discord
from random import randrange as rr

activity = discord.Activity(name="起動中…", type=discord.ActivityType.playing)
client = discord.Client(activity=activity)
@client.event

async def iamringostatus():
	print('Loaded ringostatus py!')

async def startrpc():
   print("Login completed")
   print('------')
   while True:
       await client.change_presence(activity = discord.Activity(name="実験中のbotだよ!", type=discord.ActivityType.playing))
       await asyncio.sleep(15)
       joinserver=len(client.guilds)
       servers=str(joinserver)
       await client.change_presence(activity = discord.Activity(name="サーバー数:"+servers, type=discord.ActivityType.playing))
       await asyncio.sleep(15)
       await client.change_presence(activity = discord.Activity(name="乱数:"+str(rr(0,101)), type=discord.ActivityType.playing))
       await asyncio.sleep(15)