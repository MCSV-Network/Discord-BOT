from nextcord.ext import commands
import subprocess
import os
from dotenv import load_dotenv
from internal import checkconfirm
from internal import dcmoji
COMMAND = os.environ.get("COMMAND")

class SrvRestartCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def restart(self, ctx):
		dcmoji.say()
		msg = await ctx.send('本当に実行しますか?(この操作を取り消す事はできません!)')

		confirmed = await checkconfirm.confirm(ctx, msg)

		if confirmed == True:
			await msg.edit(content=f'{dcmoji.LOADING_EMOJI} 実行中です...(1分ほどお待ちください!)')
			print ("Loading SubProccess")
			ret = subprocess.run(COMMAND, capture_output=True, text=True)
			print ("Result:")
			print("run:", ret.args)
			print("return code:", ret.returncode)
			print("ログ:", ret.stdout)
			print("エラー:", ret.stderr)
			if ret.returncode == 0:
				print ("Success! ")
				await msg.edit(content=f'{dcmoji.CHECKMARK_EMOJI} 成功しました!')
				return
			else:
				print ("Failed!")
				await msg.edit(content=f'{dcmoji.FAILED_EMOJI} エラーが発生しました! Return Code {ret.returncode}')
				return
		elif confirmed == False:
			await msg.edit(content=f'{dcmoji.CANCEL_REACTION_EMOJI} キャンセルしました!')
			return
		elif confirmed == None:
			await msg.edit(content=f'{dcmoji.TIMEOUT_EMOJI}時間内に応答がありませんでした!')
			return

def setup(bot):
	bot.add_cog(SrvRestartCog(bot))