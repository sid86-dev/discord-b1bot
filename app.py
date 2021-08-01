import discord
from telegram import *
import telegram
from telegram.ext import *

tel_token = "1900485491:AAEx7Db7iV-3zW5nBEeGJR2yi-5rNZZXl5o"
bot = telegram.Bot(token=tel_token)

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


my_secret = 'ODcxNDE4NzY5NDIyMDMyOTU3.YQbB-A.f1xEDYKKBHSLBIChKBr2RI6kRks'

keep_alive()
client.run(my_secret)

