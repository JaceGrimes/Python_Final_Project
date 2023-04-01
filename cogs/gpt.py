""""
Copyright © Solemn 2023 - 
Description:

Version: 0.1.0
"""
from helpers import checks
import aiohttp
from discord.ext.commands import Context
from discord.ext import commands
import discord

# Here we name the cog and create a new class for the cog.


class OpenAI(commands.Cog, name="openai"):
    def __init__(self, bot):
        self.bot = bot

    # These are the commands for the GPT-3 AI

    @commands.command(
        name="askgpt",
        description="This command asks a question to the chatGPT API.",
    )
# This will only allow non-blacklisted members to execute the command
    @checks.not_blacklisted()
    # This will only allow owners of the bot to execute the command -> config.json
    # @checks.is_owner()
    async def askGPT(self, context: Context, *args: str):
        """
        This is a testing command connects with ChatGPT.

        :param context: The application command context.
        """
        prompt = " ".join(args)

        if prompt == "":
            await context.send("Please provide a question.")
            return
        # Do your stuff here
        async with aiohttp.ClientSession() as session:
            payload = {
                "model": "text-davinci-003",
                "prompt": prompt,
                "temperature": 0.9,
                "max_tokens": 100,
                "presence_penalty": 0,
                "frequency_penalty": 0,
                "best_of": 1,
                "user": "1234",

            }
            headers = {
                "Authorization": f"Bearer {self.bot.config['API_KEY']}"
            }
            async with session.post(
                "https://api.openai.com/v1/completions",
                headers=headers,
                json=payload,
            ) as response:
                response = await response.json()
                embed = discord.Embed(
                    title="SHAT GPT",
                    description=f"```{response['choices'][0]['text']}```",
                    color=0x00ff00,
                )
                await context.reply(embed=embed)
# if user did not provide a prompt then dont run the command and send a message to the user


# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
async def setup(bot):
    await bot.add_cog(OpenAI(bot))

