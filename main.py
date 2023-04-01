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

#def load_env():
#
#
#	# Create .env file path.
#	dotenv_path = join(dirname(__file__), '.env')
#
#	# Load file from the path.
#	load_dotenv(dotenv_path)

async def run():

	ringostatus.iamringostatus	
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
		command_prefix='mc!'
		)

	try:
		load_dotenv()
		token = os.getenv('BOT_TOKEN')
		print("Logined as:", token)
		ringostatus.startrpc
		print("Starting RPC")
		await bot.start(token)
	except KeyboardInterrupt:
		await bot.logout()
		exit()


if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO)

	loop = asyncio.get_event_loop()
	loop.run_until_complete(run())