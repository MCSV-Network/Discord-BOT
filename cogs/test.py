from nextcord.ext import commands


class MainCmdCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def test(self, ctx):
		await ctx.send("コマンドを受信しました。")

def setup(bot):
	bot.add_cog(MainCmdCog(bot))