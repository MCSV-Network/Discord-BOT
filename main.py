import os
import asyncio
import json
import logging
from pathlib import Path
from dotenv import load_dotenv
import discord
from discord.ext import commands
import traceback

DiscordBot_Cogs = [
	'cogs.cmd',
	'cogs.test'
#	'cogs.UwU'
]

#def load_config():
#    from os.path import join, dirname
#
#
#    # Create .env file path.
#    dotenv_path = join(dirname(__file__), '.env')
#
#    # Load file from the path.
#    load_dotenv(dotenv_path)
#
#    with open('data/config.json', 'r', encoding='utf-8') as doc:
#        #  Please make sure encoding is correct, especially after editing the config file
#        return json.load(doc)


async def run():

	def get_config_var(env_name, config_path, config_name, **kwargs):
		v = os.getenv(env_name, config_path.get(config_name, kwargs.get('fallback')))

		if v is None and kwargs.get('error', False):
			raise KeyError(f'Failed to get configuration key. Env name: {env_name}, Config name: {config_name}')

		return v

	config = load_config()
	intents = discord.Intents.all()
	intents.typing = False

class ringoBot(commands.Bot):
	def __init__(self, command_prefix):
		super().__init__(command_prefix)
		for cog in DiscordBot_Cogs:
			try:
				self.load_extension(cogs)
			except Exception:
				traceback.print_exc()

if "__main__" == __name__:
	bot = ringoBot(command_prefix='mcs.')
#	bot = MCSVBot(
#			config=config,
#			description=config['description'],
#			intents=intents
#        )
#	bot.config = config

	try:
		token = get_config_var('BOT_TOKEN', config, 'token', error=True)
		bot.start(token)
	except KeyboardInterrupt:
		bot.logout()
		exit()


if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO)

	loop = asyncio.get_event_loop()
	loop.run_until_complete(run())