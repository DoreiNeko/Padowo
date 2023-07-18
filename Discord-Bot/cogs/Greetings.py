import discord 
from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'{member.mention} has appeared from the cosmos!')
                
    @commands.command(
        name="hello",
        help="Writes the user a lovely hello message~"
    )
    async def hello(self, ctx, *, member: discord.Member = None):
        ### Writes a hello message to the user who greeted
        ### the bot
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f'Hello {member.name}!')
        else:
            await ctx.send(f'{member.name}, please do not greet me too often.')
        self._last_member = member

async def setup(bot):
    await bot.add_cog(Greetings(bot))