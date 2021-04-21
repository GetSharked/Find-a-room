import os
import discord
import youtube_dl
from discord.utils import get
from discord import FFmpegPCMAudio
from os import environ
from dotenv import load_dotenv
from discord.ext import commands
'''
Potrzeba zainstalowac:
ffmpeg: git clone https://git.ffmpeg.org/ffmpeg.git ffmpeg
PyNaCl: pip install PyNaCl

'''
load_dotenv()

client = commands.Bot(command_prefix='!')


@client.command()
async def graj(ctx, url: str):  # definiujemy funkcje odpowiadajaca wejscie bota na serwer glosowy
    song_there = os.path.isfile("muza.mp3")  # zapisujemy muzyke do pliku
    try:  # usuwamy biezacą piosenke jesli jest w srodku
        if song_there:
            os.remove("muza.mp3")
    except PermissionError:
        await ctx.send('Poczekaj az sie skonczy piosenka lub uzyj komendy stop')
        return

    voice_channel = discord.utils.get(ctx.guild.voice_channels, name='Glibar')  # Kierujemy bota na kanał głosowy
    await voice_channel.connect()
    voice = discord.utils.get(client.voice_clients,
                              guild=ctx.guild)  # przechodzi przez wszystkie channele w guild i wybiera jeden do uzycia

    ydl_opts = {  # Opcje ydl typu jakie rozszerzenie jakosc
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "muza.mp3")
    voice.play(discord.FFmpegPCMAudio("muza.mp3"))


@client.command()
async def wyjdz(ctx):
    voice = discord.utils.get(client.voice_clients,
                              guild=ctx.guild)  # przechodzi przez wszystkie channele w guild i wybiera jeden do uzycia
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send('Bot nie jest polaczony')


@client.command()
async def pauza(ctx):
    voice = discord.utils.get(client.voice_clients,
                              guild=ctx.guild)  # przechodzi przez wszystkie channele w guild i wybiera jeden do uzycia
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send('Muza nie gra')


@client.command()
async def wznow(ctx):
    voice = discord.utils.get(client.voice_clients,
                              guild=ctx.guild)  # przechodzi przez wszystkie channele w guild i wybiera jeden do uzycia
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send('Muza gra')


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients,
                              guild=ctx.guild)  # przechodzi przez wszystkie channele w guild i wybiera jeden do uzycia
    voice.stop()
client.run(environ.get('DISCORD_TOKEN'))