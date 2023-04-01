import nextcord as discord
from nextcord.ext import commands
import asyncio
from internal import dcmoji

async def confirm(ctx: commands.Context, message: discord.Message):
    """
    Creates a confirm/cancel reaction menu that returns True or False depending on which reaction was clicked.

    If a timeout occurs, it will return None.
    """
    
    try:
        dcmoji.say() # この行が必要な場合は、tryブロックに移動する必要があります。

        confirm_emoji = dcmoji.CONFIRM_REACTION_EMOJI
        cancel_emoji = dcmoji.CANCEL_REACTION_EMOJI
        
        def check(r, u):
            return str(r.dcmoji) in (confirm_emoji, cancel_emoji) and u.id == ctx.author.id and r.message.id == message.id

        await message.add_reaction(confirm_emoji)
        await message.add_reaction(cancel_emoji)

        reaction, user = await ctx.bot.wait_for('reaction_add', timeout=10.0, check=check)

        selected_emoji = str(reaction.dcmoji)

        if selected_emoji == confirm_emoji:
            return True
        return False
    except asyncio.TimeoutError:
        return None
