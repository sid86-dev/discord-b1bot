import discord
import os
import random 
import pytz 

from keep_alive import keep_alive
from prsaw import RandomStuffV2

client = discord.Client()

@client.event
async def on_ready():
  print("Bot is connected. Logged in as {0.user}".format(client))
@client.event
async def on_message(message):
  msg = message.content

  rs = RandomStuffV2() 

  lst = rs.get_ai_response(msg)

  response = lst['message']



  if message.author == client.user:
    return
  else:
    await message.channel.send(response)

  rs.close()


my_secret = os.environ['BABETOKEN']

keep_alive()
client.run(my_secret)