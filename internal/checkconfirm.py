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
        
        def check(r, u):
            return str(r.dcmoji) in (dcmoji.CONFIRM_REACTION_EMOJI, dcmoji.CANCEL_REACTION_EMOJI) and u.id == ctx.author.id and r.message.id == message.id

        await message.add_reaction(dcmoji.CONFIRM_REACTION_EMOJI)
        await message.add_reaction(dcmoji.CANCEL_REACTION_EMOJI)

        reaction, user = await ctx.bot.wait_for('reaction_add', timeout=10.0, check=check)

        dcmoji = str(reaction.dcmoji)

        if dcmoji == dcmoji.CONFIRM_REACTION_EMOJI:
            return True
        return False
    except asyncio.TimeoutError:
        return None
