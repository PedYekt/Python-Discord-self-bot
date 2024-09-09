import discord
import datetime
from discord.ext import commands
import asyncio
import os

# Discord bot token (insert your token here)
TOKEN = " "

# Owner's Discord user ID (insert your user ID here)
OWNER_ID = " "

# Command prefix for bot commands
PREFIX = "~"  # You can change the prefix to your liking

# Initialize the bot with specific options
bot = commands.Bot(command_prefix=PREFIX, self_bot=True,
                   chunk_guilds_at_startup=False, request_guilds=False,
                   owner_id=OWNER_ID)

# Dictionary to store the last deleted message
last_deleted_message = {}

# Event that triggers when the bot is ready and logged in
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} at {datetime.date.today()}")

# Event that triggers when a message is deleted, saving its details
@bot.event
async def on_message_delete(message):
    global last_deleted_message
    last_deleted_message = {
        'author': message.author,
        'content': message.content,
        'timestamp': message.created_at
    }

# Command that makes the bot repeat the message in the same channel
@bot.command(name='say')
@commands.is_owner()  # Only the bot owner can use this command
async def simple_message(ctx, *, arg):
    if ctx.author.id == OWNER_ID:
        await ctx.send(arg)  # Send the message provided as 'arg'

# Command to delete a specified number of the bot's own messages
@bot.command(name='purge')
async def purge(ctx, limit: int):
    if ctx.author.id == OWNER_ID:
        # Prevent deleting too many messages
        if limit >= 100:
            await ctx.send("Too many messages to delete")
            return

        deleted_count = 0
        # Fetch message history and delete the bot's messages
        async for message in ctx.channel.history(limit=1000):
            if deleted_count > limit:
                break
            if message.author == bot.user:
                await message.delete()
                deleted_count += 1

        # Notify how many messages were deleted
        await ctx.send(f"Deleted {deleted_count} messages.", delete_after=1)

# Command to display the message history in the channel
@bot.command(name='history')
async def his(ctx, arg):
    arg = int(arg)
    async for message in ctx.channel.history(limit=arg):
        await ctx.send(f"{message.author}: {message.content}")

# Command to fetch and display a specific user's message history
@bot.command(name='user_his')
async def his(ctx, idf: int, arg: int):
    # Ensure the number of messages requested is reasonable
    if arg > 100:
        await ctx.send("Please specify a number less than or equal to 100.")
        return

    collected_messages = []  # List to store found messages
    count = 0

    # Search through the channel's message history
    async for message in ctx.channel.history(limit=1000):
        if message.author.id == idf:
            collected_messages.append(f"{message.author}: {message.content}")
            count += 1
            if count >= arg:
                break

    # Send the collected messages
    if collected_messages:
        await ctx.send("\n".join(collected_messages))
    else:
        await ctx.send("No messages found from this user.")

# Command to search for a specific user's messages containing a keyword
@bot.command(name='user_search')
async def his(ctx, idf: int, key: str, arg: int):
    # Ensure the number of messages requested is reasonable
    if arg > 100:
        await ctx.send("Please specify a number less than or equal to 100.")
        return

    collected_messages = []  # List to store found messages
    count = 0

    # Search through the channel's message history
    async for message in ctx.channel.history(limit=1000):
        if message.author.id == idf and key in message.content:
            collected_messages.append(f"{message.author}: {message.content}")
            count += 1
            if count >= arg:
                break

    # Send the collected messages
    if collected_messages:
        await ctx.send("\n".join(collected_messages))
    else:
        await ctx.send("No messages found from this user.")

# Command to "snipe" the last deleted message and display it
@bot.command(name='snipe')
async def snipe(ctx):
    if last_deleted_message:
        msg = last_deleted_message
        await ctx.send(f"**{msg['author']}**: {msg['content']}")
    else:
        await ctx.send("No message has been deleted recently.")

# Command to spam a message a specified number of times
@bot.command(name="spam")
async def spam(ctx, message, arg):
    counter = 0
    while counter < int(arg):
        await ctx.send(message)
        counter += 1

# Command to shut down the bot
@bot.command(name='exit')
async def close_discord(ctx):
    await bot.close()

# Run the bot with the provided token
bot.run(TOKEN)
