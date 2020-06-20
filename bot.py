import discord
from discord.ext import commands

import os
from dotenv import load_dotenv
load_dotenv("./secrets/.env")

client = commands.Bot(command_prefix="b!")
client.remove_command("help")

extensions = [
]

for exten in extensions:
    try:
        client.load_extension(exten)
    except Exception as e:
        print(f"Failed to load cog {exten}")
        print(e)
    else:
        print(f"Loaded extension {exten}")

client.run(os.environ["TOKEN"])