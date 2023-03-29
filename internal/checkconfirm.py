import nextcord as discord
from nextcord.ext import commands
import asyncio
from internal import discordemoji as emoji

async def confirm(ctx: commands.Context, message: discord.Message):
    """
    Creates a confirm/cancel reaction menu that returns True or False depending on which reaction was clicked.

    If a timeout occurs, it will return None.
    """

    def check(r, u):
        return str(r.emoji) in (emoji.CONFIRM_REACTION_EMOJI, emoji.CANCEL_REACTION_EMOJI) and u.id == ctx.author.id and r.message.id == message.id

    await message.add_reaction(emoji.CONFIRM_REACTION_EMOJI)
    await message.add_reaction(emoji.CANCEL_REACTION_EMOJI)

    try:
        reaction, user = await ctx.bot.wait_for('reaction_add', timeout=10.0, check=check)

        emoji = str(reaction.emoji)

        if emoji == emoji.CONFIRM_REACTION_EMOJI:
            return True
        return False
    except asyncio.TimeoutError:
        return None
