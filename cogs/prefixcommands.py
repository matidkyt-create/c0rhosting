import discord
from discord.ext import commands
invitelink = "https://discord.com/oauth2/authorize?client_id=1430593169598189720&permissions=8&integration_type=0&scope=bot"

class prefixcommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online!")

    @commands.command()
    async def ping(self, ctx):
        await ctx.reply(f"# **Pong!** \n Bot's Response Time Is: {round(self.bot.latency * 1000)}ms")

    @commands.command()
    async def info(self, ctx):
        embedinfo = discord.Embed(title="Bot's Info", description=f"CorBot Is An Essential Discord Bot. \n CorBot Was Made By Mat And Supports Slash Commands \n ``Invite Corbot?`` [Click To Invite]({invitelink})", color=discord.Color.blue())
        await ctx.send(embed=embedinfo)

async def setup(bot):
    await bot.add_cog(prefixcommands(bot))