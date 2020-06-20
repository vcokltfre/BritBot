import utils.cfl as cfl
import discord

def getCommandGroup(groupName):
    help_file = cfl.getConfigList("static_data/help.json")
    for i in help_file:
        if i["name"] == groupName:
            return i

#Auto generate help embed
def genHelp(groupName):
    item = getCommandGroup(groupName)
    subcommands = item["subcommands"]
    embed = discord.Embed(title="Command help", description=f"Commands for group {groupName}")
    for item in subcommands:
        embed.add_field(name=item["name"], value=f"Desc: {item['description']}\nUsage: {item['usage']}")
    return embed
