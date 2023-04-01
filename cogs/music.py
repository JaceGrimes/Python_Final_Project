# """"
# Copyright © Solemn 2023 - 
# Description:

# Version: 0.1.0
# """

# from discord.ext import commands
# from discord.ext.commands import Context
# #add voice client
# from discord import FFmpegPCMAudio
# from discord.utils import get
# import os
# import asyncio
# import random


# from helpers import checks


# # Here we name the cog and create a new class for the cog.
# class Music(commands.Cog, name="music"):
#     def __init__(self, bot):
#         self.bot = bot

#     # Here you can just add your own commands, you'll always need to provide "self" as first parameter.

#     @commands.hybrid_command(
#         name="queue",
#         description="This is the command for checking the queue.",
#     )
#     # This will only allow non-blacklisted members to execute the command
#     @checks.not_blacklisted()
#     # This will only allow owners of the bot to execute the command -> config.json
#     @checks.is_owner()
#     async def queue(self, context: Context):
#         """
#         This is the command for playing music.

#         :param context: The application command context.
#         """
#         # Do your stuff here
#         try:
#             channel = context.author.voice.channel
#         except AttributeError:
#             await context.send("You are not connected to a voice channel.")
#             return

#         get = self.bot.get_voice_client

#         voice = get(self.bot.voice_clients, guild=context.guild)
#         if voice and voice.is_connected():
#             await voice.move_to(channel)
#         else:
#             voice = await channel.connect()
#         await context.send(f"Joined {channel}")

#     @commands.command(
#         name="play",
#         description="This is the command for playing music.",
#     )
#     # This will only allow non-blacklisted members to execute the command
#     @checks.not_blacklisted()
#     # This will only allow owners of the bot to execute the command -> config.json
#     @checks.is_owner()
#     async def play(self, context: Context, url: str):
#         """
#         This is the command for playing music.

#         :param context: The application command context.
#         """
#         # Do your stuff here
#         try:
#             channel = context.author.voice.channel
#         except AttributeError:
#             await context.send("You are not connected to a voice channel.")
#             return

#     #here we have the bot join the voice channel of the user who called the command
#         get = self.bot.get_voice_client

#         voice = get(self.bot.voice_clients, guild=context.guild)
#         if voice and voice.is_connected():
#             await voice.move_to(channel)
#         else:
#             voice = await channel.connect()
#         await context.send(f"Joined {channel}")

#     #here we create a player for the bot to play the music
#         player = await voice.create_ytdl_player(url)
#         player.start()




# # And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
# async def setup(bot):
#     await bot.add_cog(Music(bot))
