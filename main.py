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
    if message_content.startswith('!edit'):
      edit=('I can update it for you')
      await msg.channel.send(edit)

    #EVENT : INFO USER
    if message_content.startswith('!info'):
      if msg.mentions:
        info = ""
        for user in msg.mentions:

          # Get User Info

          # Parse Firebase, match and output data based on user ID

          embed=discord.Embed(
          title="About Me",
              url="https://mlh-fellowship.trainualapp.com/users/294366",
              description= user.display_name + "'s MLH Fellowship Profile",
              color=discord.Color.blue())
          embed.set_author(name=user.name, url="https://twitter.com/nikhilxvytla", icon_url=user.avatar_url)
          embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")
          embed.add_field(name="Name", value="Nikhil Vytla", inline=False)
          embed.add_field(name="Pronouns", value="(he/him)", inline=False)
          embed.add_field(name="__Pod__", value="4.2.0", inline=False)
          embed.add_field(name="__Track__", value="GitHub Externship", inline=False)
          embed.add_field(name="Favorite Language(s)", value="`Python`, `Javascript`", inline=False)
          embed.add_field(name="GitHub", value="> https://github.com/nikhil-vytla", inline=False)
          embed.add_field(name="LinkedIn", value="> https://linkedin.com/in/nikhil-vytla", inline=False)
          embed.add_field(name="Favorite Joke", value="||Why did the chicken cross the road? To get to the other side!||", inline=False)
          embed.set_footer(text="Learn more about me: nikhilvytla.com")

          await msg.channel.send(embed=embed)
      
      else:
        info = "Looking for profile info? Make sure to specify a user/users (ex. `!info @mlhducky`)."
      # if USER does not have info, return message 
      # "@USER does not have any info available"
      await msg.channel.send(info)

    #EVENT : SCHEDULE
    if message_content.startswith('!schedule'):
      schedule=('I can schedule a meeting')
      await msg.channel.send(schedule)

client.run(DISCORD_API)