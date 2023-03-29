from nextcord.ext import commands
import colorama

class PyreadyCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

@commands.Cog.listener()
async def on_ready(self):
	print(Fore.GREEN + "======MCSV-Bot======")
	print("")
	print(Fore.GREEN + "Created by ringoXD")


def setup(bot):
	bot.add_cog(PyreadyCog(bot))
