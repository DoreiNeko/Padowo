import discord, os ,sys
from discord.ext import commands
import asyncio
import datetime

class Administration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
            name="test",
            help="command for testing purposes"
    )
    async def test(self, channel):
        channel = self.bot.get_channel()
        await channel.send(channel)

    @commands.command(
        name="restart",
        help="Restarts the bot"
    )
    async def restart(self, ctx):
        try:
            if ctx.message.author.guild_permissions.administrator:
                #channel = self.bot.get_channel(member.message.channel)

                def restart_program():
                    python = sys.executable
                    os.execl(python, python, * sys.argv)

                restart_embed = discord.Embed(
                    title = 'Restarting the bot in 5 seconds...',
                    color = 0x4fff4d,
                )
                await ctx.send(embed=restart_embed, delete_after=4.0)

                channel = self.bot.get_channel(1129941518552150106)
                blame_embed = discord.Embed(
                    title = f'The bot has been restarted at {datetime.datetime.now()}',
                    description = f'You can blame {ctx.author}'
                )
                await channel.send(embed=blame_embed)

                await asyncio.sleep(5)
                restart_program()

            else:
                await ctx.send("You do not have the permissions to do that~")
        except:
            print("Weird. . . ")

    @commands.command(
        name="purge",
        alias="clear",
        help="Removes user defined number of messages"
    )
    async def purge(self, ctx, amount):
        if ctx.message.author.guild_permissions.manage_messages:
            await ctx.message.delete()
            amount = int(amount)
            deleted = await ctx.channel.purge(limit=amount)
            confirmdelete_embed = discord.Embed(title='Delete Successfull!', description=f'Deleted {len(deleted)} messages in #{ctx.channel}', color=0x4fff4d)
            await ctx.channel.send(embed=confirmdelete_embed, delete_after=4.0)

            channel = self.bot.get_channel(1129941518552150106)
            blame_embed = discord.Embed(
                title = f'The bot has ran a purge of {len(deleted)} messages in {ctx.message.channel}',
                description = f'You can blame {ctx.author}'
            )
            await channel.send(embed=blame_embed)
        else:
            await ctx.send("You do not have the permissions to do that.")

    @commands.command(
        name="ping",
        help="Check the bots latency"
    )
    async def ping(self, ctx):
        await ctx.send(f'bot ping is {round(self.bot.latency * 1000)}ms')

async def setup(bot):
    await bot.add_cog(Administration(bot))
