from nextcord.ext import commands
import nextcord as discord
import subprocess
import os

class SrvRestartCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def cmd(self, ctx):
		await ctx.send("こんにちは!!!")

def setup(bot):
	bot.add_cog(SrvRestartCog(bot))