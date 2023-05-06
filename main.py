import os
import asyncio
import logging
from pathlib import Path
import nextcord as discord
from internal.classbot import ringoBot
from internal import ringostatus
from nextcord.ext import commands
import traceback
from os.path import join, dirname
from dotenv import load_dotenv

activity = discord.Activity(name="起動中…", type=discord.ActivityType.playing)
#def load_env():
#
#
#	# Create .env file path.
#	dotenv_path = join(dirname(__file__), '.env')
#
#	# Load file from the path.
#	load_dotenv(dotenv_path)

async def run():

	def get_config_var(env_name, config_path, config_name, **kwargs):
		"""
		Attempts to get a variable from the env file, then from the config key, and finally, if none found, returns the fallback value.
		"""
		v = os.getenv(env_name, config_path.get(config_name, kwargs.get('fallback')))

		if v is None and kwargs.get('error', False):
			raise KeyError(f'Failed to get configuration key. Env name: {env_name}, Config name: {config_name}')

		return v

	intents = discord.Intents.all()
	intents.typing = False

	bot = ringoBot(
		command_prefix='mc!',
		bot = discord.Client(activity=activity)
		)

	try:
		load_dotenv()
		token = os.getenv('BOT_TOKEN')
		print("Logined as:", token)
		await ringostatus.startrpc()
		print("Starting RPC")
		await bot.start(token)
	except KeyboardInterrupt:
		await bot.logout()
		exit()


if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO)

	loop = asyncio.get_event_loop()
	loop.run_until_complete(run())



async def startrpc():
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