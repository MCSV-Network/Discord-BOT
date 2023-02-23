import asyncio
import datetime
import time
from pathlib import Path

import discord
from nextcord.ext import commands

class ringoBot(commands.Bot):
	def __init__(self, command_prefix):
		super().__init__(command_prefix)
		for cog in DiscordBot_Cogs:
			try:
				self.load_extension(cogs)
			except Exception:
				traceback.print_exc()