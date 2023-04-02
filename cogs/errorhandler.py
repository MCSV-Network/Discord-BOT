import nextcord as discord
from nextcord.ext import commands

class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandError):
            # エラーが発生した場合、その内容をctx.sendする
            await ctx.send(f":rotating_light: エラーが発生しました。: {error}")
