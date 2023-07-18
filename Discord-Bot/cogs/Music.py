import discord
from discord.ext import commands,tasks
import os
import yt_dlp
import asyncio

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #self.ydl_opts = {
    #    'format': 'bestaudio/best',
    #    'postprocessors': [{
    #        'key': 'FFmpegExtractAudio',
    #        'preferredcodec': 'mp3',
    #        'preferredquality': '192'
    #    }],
    #    }
        #with yt_dlp.YoutubeDL(ydl_opts) as ydl:

    @commands.command(
        name="join",
        help="Joins the voice channel of the user"
    )
    async def join(self, ctx, member: discord.Member = None):
        try:
            member = member or ctx.author
            channel = member.voice.channel
            
            if ctx.voice_client is None:
                await ctx.send(f'Joining {channel}!')
                await member.voice.channel.connect()

            else:
                await ctx.send(f'I can not do that, I am already in {ctx.voice_client.channel}~')
        except AttributeError:
            return await ctx.send('You are not in a voice channel silly~')

    @commands.command(
        name="leave",
        help="Leaves the current voice channel"
    )
    async def leave(self, ctx):
        try:
            await ctx.guild.voice_client.disconnect()
        
        except:
            await ctx.send('I am not in a voice channel. . .')
    
    @commands.command(
        name="play",
        help="plays a song and adds it to the queue"
    )
    async def play(self, ctx, *, member: discord.Member = None):
        try:
            if ctx.voice_client is None:
                member = member or ctx.author
                channel = member.voice.channel

                await member.voice.channel.connect()

            
        except:
            await ctx.send("Unknown error. . .")
        #if voice_channel != None:
        #    voice_client: discord.VoiceClient = discord.utils.get(
        #        self.bot.voice_clients,
        #        guild = ctx.guild
        #    )
        #    audio_source = discord.FFmpegPCMAudio('test.mp3')
        #    if not voice_client.is_playing():
        #        voice_client.play(audio_source, after = None)
        #else:
        #    await self.bot.say('User is not in a channel.')

async def setup(bot):
    await bot.add_cog(Music(bot))