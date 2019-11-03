import discord
from discord.ext import commands
import asyncio

prefix = '$'
token = open('btoken.txt', "r").read() 

class Tragic(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hi(self, ctx, args):
        await ctx.send("Nice message you got there")
        await ctx.send("it was\t"+str(args))

bot = commands.Bot(command_prefix = commands.when_mentioned_or(prefix), description= "random test woo")
        
@bot.event
async def on_ready():
    print("Connected! as\t" + str(bot.user.name) + str(bot.user.id))

bot.add_cog(Tragic(bot))

bot.run(token)