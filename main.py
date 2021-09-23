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
DB_FIELDS = (
            "name",
            "pronouns",
            "pod",
            "discord",
            "email",
            "role",
            "calendly",
            "github",
            "linkedin",
            "primary_OS",
            "timezone",
            "location",
            "favorite_language"
        )

#Discord Client
client = discord.Client()

#Initialize Firebase
if not firebase_admin._apps:
        cred_obj = firebase_admin.credentials.Certificate(GCP_CRED)
        firebase_admin.initialize_app(cred_obj, {
            'databaseURL': 'https://discord-intro-bot-default-rtdb.firebaseio.com/'
        })

async def usage(err_type, channel):
    '''Send an error message and usage help'''
    if (err_type == "edit"):
        edit_help=(
            '''>>> Usage : `!edit @user field value` \n'''
            ''' \t\tfields: Name, Pronouns, Pod, Location, Timezone\n'''
            ''' \t\t\tEmail, Calendly, GitHub, LinkedIn'''
        )
        await channel.send(edit_help)
        
async def update(msg):
    '''Parse edit command from message and execute it'''
    args = msg.content.strip(' ').split(' ', 3)
    if len(args) != 4:
        return await usage("edit",msg.channel)
    field = args[2].strip(' ').lower()
    if field not in DB_FIELDS:
        return await usage("edit",msg.channel)
    elif len(msg.raw_mentions) != 1:
        return await usage("edit",msg.channel)
    else: #update database
        ref = db.reference("/fellows")
        uid = str( msg.mentions[0] )
        print(uid)
        val = args[-1]
        data = ref.get()
        found = False
        for k, usr in data.items():
            if usr["discord"] == uid:
                ref.child(k).update( {field: val} )
                found = True
                break
        if found: 
            await msg.channel.send(f"Set {field} to {val} for {uid}")
        else:
            await msg.channel.send(f"No entry found for {uid}")
    
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
        help=('```!edit @user key value-> Edit your own profile'
            +'\n!info @mention -> Get Info about your fellow pod mate'
            +'\n!schedule @user -> Schedule a time slot with your fellow pod mate```'
        )
        await msg.channel.send(help)

    #EVENT : UPDATE USER
    if message_content.startswith('!edit'):
        await update(msg)

    #EVENT : INFO USER
    if message_content.startswith('!info'):
      if msg.mentions:

        info, name, pronouns, pod, calendly, github = "", "", "", "", "", ""
        linkedin, email, location, timezone, favorite_language = "", "", "", "", ""

        # Populate User Info
        # Parse Firebase, match and output data based on user ID
        ref = db.reference("/fellows")
        uid = str(msg.mentions[0])
        data = ref.get()
        found = False

        for mentioned in msg.mentions:
          for k, usr in data.items():
              if usr["discord"] == uid:
                  name = usr["name"]
                  first_name = name.split(' ')[0]
                  pronouns = usr["pronouns"]
                  pod = usr["pod"]
                  discord_tag = usr["discord"]
                  email = usr["email"]
                  role = usr["role"]
                  calendly = usr["calendly"]
                  github = usr["github"]
                  linkedin = usr["linkedin"]
                  primary_OS = usr["primary_OS"]
                  timezone = usr["timezone"]
                  location = usr["location"]
                  favorite_language = usr["favorite_language"]
                  found = True

                  # Embed color based on track
                  if "4.0" in pod:
                    color = discord.Color.red()
                  elif "4.2" in pod:
                    color = discord.Color.blue()
                  else:
                    color = discord.Color.green()

                  break
          if found: 

            embed=discord.Embed(
            title="About " + first_name + " (@" + discord_tag + ")",
                description= "MLH Fellowship Profile",
                color=color)
            embed.set_author(name=name, icon_url=mentioned.avatar_url)
            embed.set_thumbnail(url=mentioned.avatar_url)
            embed.add_field(name="**Name**", value=name, inline=False)
            embed.add_field(name="**Pronouns**", value=pronouns, inline=False)
            embed.add_field(name="__Pod__", value=pod, inline=False)
            embed.add_field(name="**Favorite Language(s)**", value=favorite_language, inline=False)
            embed.add_field(name="**GitHub**", value="> https://github.com/" + github, inline=False)
            embed.add_field(name="**LinkedIn**", value="> "+ linkedin, inline=False)
            embed.add_field(name="**Favorite Joke**", value="||Why did the chicken cross the road? To get to the other side!||", inline=False)
            embed.set_footer(text="Schedule a 1-on-1: " + calendly)

            await msg.channel.send(embed=embed)
          else:
            await msg.channel.send(f"No entry found for {uid}")
      
      else:
        # if USER does not have info, return message 
        info = "Looking for profile info? Make sure to specify a user/users (ex. `!info @mlhducky`)."
        await msg.channel.send(info)

    #EVENT : SCHEDULE
    if message_content.startswith('!schedule'):
      schedule=('I can schedule a meeting')
      await msg.channel.send(schedule)

client.run(DISCORD_API)