# botInfo
#Importamos las librerias necesarias.
import discord
import os
from dotenv import load_dotenv


load_dotenv()
TOKEN = 'ODAwOTk1Mzc2ODAyODI0MjAy.YAaPEw.gE-QTSHrRxFgm1HppHiNC7rB2ds'

client = discord.Client()
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
