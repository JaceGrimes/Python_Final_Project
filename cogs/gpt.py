# """"
# Copyright © Solemn 2023 - 
# Description:

# Version: 0.1.0
# """
# import discord
# from discord.ext import commands
# from discord.ext.commands import Context
# import aiohttp

# from helpers import checks


# # Here we name the cog and create a new class for the cog.
# class OpenAI(commands.Cog, name="ChatGPT"):
#     def __init__(self, bot):
#         self.bot = bot

#     # These are the commands for the GPT-3 AI

#     @commands.hybrid_command(
#         name="askgpt",
#         description="This command asks a question to the GPT-3 AI.",
#     )
#     # This will only allow non-blacklisted members to execute the command
#     @checks.not_blacklisted()
#     # This will only allow owners of the bot to execute the command -> config.json
#     @checks.is_owner()
#     async def askGPT(self, context: Context, prompt: str):
#         """
#         This is a testing command connects with ChatGPT.

#         :param context: The application command context.
#         """
#         # Do your stuff here
#         async with aiohttp.ClientSession() as session:
#             payload = {
#                 "model": "text-davinci-003",
#                 "prompt": prompt,
#                 "temperature": 0.9,
#                 "max_tokens": 50,
#                 "presence_penalty": 0,
#                 "frequency_penalty": 0,
#                 "best_of": 1,
#             }
#             headers = {
#                 "Authorization": f"Bearer {self.bot.config['API_KEY']}"}
#             async with session.post(
#                 "https://api.openai.com/v1/engines/davinci/completions",
#                 headers=headers,
#                 json=payload,
#             ) as response:
#                 result = await response.json()
#                 await context.send(result["choices"][0]["text"])
#                 embed = discord.Embed(
#                     title="GPT-3 AI", description=f"```{response['choices'][0]['text']}```", color=0x00ff00)
#                 await context.reply(embed=embed)

#         # Don't forget to remove "pass", I added this just because there's no content in the method.


# # And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
# async def setup(bot):
#     await bot.add_cog(OpenAI(bot))
