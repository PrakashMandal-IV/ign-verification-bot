import os
import re
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
IGN_CHANNEL_ID = int(os.getenv("IGN_CHANNEL_ID"))
UNVERIFIED_ROLE_ID = int(os.getenv("UNVERIFIED_ROLE_ID"))

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

def is_valid_ign(name: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-z0-9_]{3,16}", name))

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    if message.channel.id != IGN_CHANNEL_ID:
        return

    ign = message.content.strip()

    try:
        await message.delete()
    except:
        pass

    if not is_valid_ign(ign):
        await message.author.send(
            "❌ **Invalid IGN**\n"
            "Only letters, numbers, and underscores are allowed.\n"
            "Length: 3–16 characters."
        )
        return

    member = message.author

    try:
        await member.edit(nick=ign)

        unverified_role = member.guild.get_role(UNVERIFIED_ROLE_ID)
        if unverified_role and unverified_role in member.roles:
            await member.remove_roles(unverified_role)

        await member.send(
            f"✅ **IGN Set Successfully!**\n"
            f"Your nickname is now: `{ign}`\n"
            f"You are now verified 🎉"
        )

    except discord.Forbidden:
        await member.send(
            "❌ I don't have permission to change your nickname or roles.\n"
            "Please contact a server admin."
        )

    await bot.process_commands(message)

bot.run(TOKEN)
