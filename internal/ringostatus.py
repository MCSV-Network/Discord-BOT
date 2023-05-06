import asyncio
import nextcord as discord
from random import randrange as rr

def iamringostatus():
	print('Loaded ringostatus py!')



async def botstatus(bot):
	print("Login completed")
	print('------')
	while True:
		await bot.change_presence(activity = discord.Activity(name="実験中のbotだよ!", type=discord.ActivityType.playing))
		await asyncio.sleep(15)
		joinserver=len(bot.guilds)
		servers=str(joinserver)
		await bot.change_presence(activity = discord.Activity(name="サーバー数:"+servers, type=discord.ActivityType.playing))
		await asyncio.sleep(15)
		await bot.change_presence(activity = discord.Activity(name="乱数:"+str(rr(0,101)), type=discord.ActivityType.playing))
		await asyncio.sleep(15)