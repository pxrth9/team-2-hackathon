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
            "track",
            "calendy",
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
            ''' \t\tfields: Name, Pronouns, Pod, Track, Location, Timezone\n'''
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
        help=('I got your request')
        await msg.channel.send(help)

    #EVENT : UPDATE USER
    if message_content.startswith('!edit'):
        await update(msg)

    #EVENT : INFO USER
    if message_content.startswith('!info'):
      help=('I can send you the info')
      await msg.channel.send(help)

    #EVENT : SCHEDULE
    if message_content.startswith('!schedule'):
      help=('I can schedule a meeting')
      await msg.channel.send(help)

client.run(DISCORD_API)
