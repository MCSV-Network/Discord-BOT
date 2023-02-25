import asyncio
import datetime
import time
from pathlib import Path
import discord
import traceback
from nextcord.ext import commands

DiscordBot_Cogs = [
	'cogs.cmd',
	'cogs.test'
#	'cogs.UwU'
]

class ringoBot(commands.Bot):
	def __init__(self, command_prefix):
		super().__init__(command_prefix)
		for cog in DiscordBot_Cogs:
			try:
				self.load_extension(cogs)
			except Exception:
				traceback.print_exc()