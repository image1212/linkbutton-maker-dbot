from discord.ext import commands
import discord
from discord_buttons_plugin import *

bot = commands.Bot(command_prefix = "!")
buttons = ButtonsClient(bot)

@bot.command()
async def button(ctx,title1=None,desc=None,label1=None,url=None,color=None):
    if color == None:
        await buttons.send(
            embed=discord.Embed(title=title1, description=desc, color=0x5c6cdf), 
            channel = ctx.channel.id,
            components = [
                ActionRow([
                    Button(
                        label = f"{label1}", 
                        style = ButtonType().Link, 
                        url = f"{url}"
                    )
                ])
            ]
        )
    else:
        color11 = int(hex(int(color.replace("#", ""), 16)), 0)
        await buttons.send(
            embed=discord.Embed(title=title1, description=desc, color=color11), 
            channel = ctx.channel.id,
            components = [
                ActionRow([
                    Button(
                        label = f"{label1}", 
                        style = ButtonType().Link, 
                        url = f"{url}"
                    )
                ])
            ]
        )

bot.run("token")
