from nextcord.ext import commands


class MainCmdCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def cmd(self, ctx):
		await ctx.send("こんにちは!!!")

def setup(bot):
	bot.add_cog(MainCmdCog(bot))
