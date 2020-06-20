import discord
from discord.ext import commands
import utils.genhelp as gh

class Insult(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="insult")
    async def insult(self, ctx):
        if ctx.invoked_subcommand == None:
            await ctx.channel.send(embed=gh.genHelp("insult"))

    @insult.command(name="fucc")
    async def fucc(self, ctx, *name):
        name = " ".join(name)
        await ctx.channel.send(f"{ctx.author.name} says \"fuck you\", {name}")

def setup(bot):
    bot.add_cog(Insult(bot))