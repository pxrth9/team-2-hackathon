# # MAIN FILE FOR THE DISCORD BOT 
import firebase_admin
from firebase_admin import db
import os
from dotenv import load_dotenv, main
import json
import discord

# #API KEYS
load_dotenv()
GCP_CRED = json.loads(os.getenv('GCP_CRED'))
DISCORD_API = os.getenv('DISCORD_API')

#GLOBAL VARIABLES

#Discord Client
client = discord.Client()

#Initialize Firebase
if not firebase_admin._apps:
        cred_obj = firebase_admin.credentials.Certificate(GCP_CRED)
        firebase_admin.initialize_app(cred_obj, {
            'databaseURL': 'https://discord-intro-bot-default-rtdb.firebaseio.com/'
        })
    
# Ready Bot
@client.event
async def on_ready():
  print("Bot Ready!")

#Other Events
@client.event
async def on_message(msg):
    user_ID = msg.author
    message_content = msg.content

    #EVENT : HELP
    if message_content.startswith('!help'):
        help=('I got your request')
        await msg.channel.send(help)

    #EVENT : UPDATE USER
    if message_content.startswith('!update'):
      help=('I can update it for you')
      await msg.channel.send(help)

client.run(DISCORD_API)