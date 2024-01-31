import os
import datetime 
import requests # HTTP Library
from dotenv import load_dotenv # load for env
import discord
import asyncio

load_dotenv()

TOKEN = os.environ.get("TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")

intents = discord.Intents.default()
intents.message_content = True

# discord Client class 생성

client = discord.Client(intents=intents)

@client.event # 봇이 실행되는 동안 발생하는 유저 이벤트
async def on_ready() : # 봇이 실행되면 한 번 실행됨
    print("Run on_ready")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("저는 봇입니다."))  # 상태 메시지 변경

@client.event
async def on_message(message): # 봇이 작동하고 있는 채널에서 메시지가 감지, message.content와 동일한 경우에 봇 동작
    if message.content == "테스트":
        await message.channel.send(f"Hello {message.author} {message.author.mention} ") # 채널에 메시지 전송 message.author =  작성자
        await message.author.send(f"User Hello {message.author} {message.author.mention}") # 메시지 작성자에게 dm 전송


client.run(TOKEN)



