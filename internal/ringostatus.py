import asyncio
import nextcord as discord
from random import randrange as rr

def iamringostatus():
	print('Loaded ringostatus py!')



async def botstatus(client):
   print("Login completed")
   print('------')
   while True:
       await client.change_presence(activity = discord.Game(name="実験中のbotだよ!", type=discord.ActivityType.playing))
       await asyncio.sleep(15)
       joinserver=len(client.guilds)
       servers=str(joinserver)
       await client.change_presence(activity = discord.Game(name="サーバー数:"+servers, type=discord.ActivityType.playing))
       await asyncio.sleep(15)
       await client.change_presence(activity = discord.Game(name="乱数:"+str(rr(0,101)), type=discord.ActivityType.playing))
       await asyncio.sleep(15)