import asyncio
import datetime
import time
from pathlib import Path
import nextcord as discord
import traceback
from nextcord.ext import commands

DiscordBot_Cogs = [
	'cogs.cmd',
	'cogs.test'
	'cogs.servrestart'
]

class ringoBot(commands.Bot):
	async def __init__(self, command_prefix):
		super().__init__(command_prefix)
		await self.wait_until_ready()
		await asyncio.sleep(1)  # Ensure that on_ready has completed and finished printing
		cogs = [x.stem for x in Path('cogs').glob('*.py')]
		for extension in cogs:
			try:
				print(f'loaded {extension}')
				self.load_extension(f'cogs.{extension}')
			except Exception as e:
				error = f'{extension}\n {type(e).__name__} : {e}'
				print(f'failed to load extension {error}')
			print('-' * 10)