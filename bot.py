import discord
from discord.ext import commands
import asyncio

prefix = '$'
token = open('btoken.txt', "r").read() 

class Tragic(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.queue = asyncio.Queue()
        self.pNext = asyncio.Event()

    @staticmethod
    async def task(self):
        while True:
            self.pNext.clear()
            curr = await self.queue.get()
            curr.start()
            await pNext.wait()

    def toggle(self):
        self.bot.loop.call_soon_threadsafe(pNext.set)

    @commands.command()
    async def play(self, ctx, url):
        if not bot.is_voice_connected(ctx.message.server):
            v = await bot.join_voice_channel(ctx.message.author.voice_channel)
        else:
            v = bot.voice_client_in(ctx.message.server)
        
        p = await v.create_ytdl_player(url, after=toggle)
        await self.queue.put(p)

    @commands.command()
    async def hi(self, ctx, args):
        await ctx.send("Nice message you got there")
        await ctx.send("it was\t"+str(args))

bot = commands.Bot(command_prefix = commands.when_mentioned_or(prefix), description= "random test woo")
        
bot.add_cog(Tragic(bot))

@bot.event
async def on_ready():
    print("Connected! as\t" + str(bot.user.name) + str(bot.user.id))
    bot.loop.create_task(Tragic.task())

bot.run(token)