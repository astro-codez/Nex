from core.apolex import apolex
import os
os.system("pip install -r requirements.txt")
os.system("pip install git+https://github.com/Pycord-Development/pycord")
import colorama
from colorama import Fore
print(Fore.CYAN + "=======================" + Fore.RESET)
#import emoji
from itertools import cycle
from qrcode import QRCode
import ast
import googletrans
from googletrans import Translator
import discord
#import csv
#from discord.ui import Button, View
import inspect
import akinator 
from akinator.async_aki import Akinator
#from cogs.antiraid import AntiRaid
from cogs.help import Help
from lib2to3.pgen2 import token
import re
import json
import requests
from click import command
#import dismusic
import discord, datetime
import pymongo
from main1 import add_server, all_servers, get_amount, get_server, delete_server, get_warns,add_warn,add_amount, get_greet,add_greet,remove_greet,get_users,add_user,add_money,share_money, get_info,give_money,remove_money,add_inventory,update_greet, remove_code, add_code, get_codes, get_premiumservers, add_premium, add_funcmd, get_funcmd, remove_funcmd, add_chatbot, get_chatbot, remove_chatbot, add_joinchannel, get_join_channels, remove_joinchannel
from discord.ext import commands
import os
os.system("pip install aiohttp")
import aiohttp
os.system("pip install httpx")
import httpx
import json
os.system("pip install wavelink")
import wavelink
import subprocess
import asyncio
import traceback
import sys
import ast
#from otherscipts.data import Data
#from cogs.serversettings import ServerSettings
from discord.utils import get
import os
import random
import asyncio
from discord.ext import commands, tasks
import webserver
from webserver import keep_alive
import colorama
from colorama import Fore
print(Fore.CYAN + "=======================" + Fore.RESET)
import ast
import inspect
#from cogs.antiraid import AntiRaid
from cogs.help import Help
from lib2to3.pgen2 import token
import re
import urllib.request
import json
import requests
from click import command
import discord 
#from discord.ui import Button, View
#import dismusic


import discord, datetime
import pymongo
from main1 import add_server, all_servers, get_server, delete_server, get_greet,add_greet,remove_greet,get_users,add_user,add_money,share_money, get_info,give_money,remove_money,add_inventory,update_greet, remove_code, add_code, get_codes, get_premiumservers, add_premium,add_joinchannel, get_join_channels, remove_joinchannel
from discord.ext import commands
import os
os.system("pip install aiohttp")
import aiohttp
os.system("pip install httpx")
import httpx
import json
os.system("pip install wavelink")
import wavelink
import subprocess
from cogs.utils import *
import asyncio
import traceback
import sys
import ast
#from otherscipts.data import Data
#from cogs.serversettings import ServerSettings
from discord.utils import get
import os
import random
import asyncio
import discord
import googletrans 
#from discord.ui import Button, View
from discord.ext import commands, tasks
import webserver
from webserver import keep_alive
from main1 import add_server, all_servers, get_server, delete_server, get_greet,add_greet,remove_greet,get_users,add_user,add_money,share_money, get_info,give_money,remove_money,add_inventory,update_greet, remove_code, add_code, get_codes, get_premiumservers, add_premium,add_joinchannel, get_join_channels, remove_joinchannel
bot = apolex()

proxies = open('proxies.txt').read().split('\n')
proxs = cycle(proxies)
proxies={"http": 'http://' + next(proxs)}




@bot.listen("on_ready")
async def readyevn():
 print(f'logged in {bot.user}')
 bot.add_view(verificationb())
 bot.add_view(selfrole2())
 #bot.add_view(rr2())

@bot.event
async def on_guild_update(before, after):
  if "VANITY_URL" in after.features:
           with open("vanity.json") as f:
                vanity = json.load(f)
                stored_vanity = vanity[str(after.id)]
           return await after.edit(vanity_code=stored_vanity)

@bot.command(aliases=['vanity'])
@commands.guild_only()
async def setvanity(ctx, vanity_code):
    if ctx.message.author.id != ctx.guild.owner_id:
      return
    with open('vanity.json', 'r') as f:
        vanity = json.load(f)
        vanity[str(ctx.guild.id)] = vanity_code
    with open('vanity.json', 'w') as f:
        json.dump(vanity, f, indent=4)
    await ctx.send("Successfully Set Vanity To {}".format(vanity_code))

cd = commands.CooldownMapping.from_cooldown(6, 7, commands.BucketType.user)

@bot.listen("on_message")
async def antispamm_event(message):
  with open("antispamconf.json", "r") as f:
    idk = json.load(f)
  bucket = cd.get_bucket(message)
  retry = bucket.update_rate_limit()
  if retry:
    if str(message.guild.id) not in idk or idk[str(message.guild.id)] == "disable":
      return
    elif str(message.guild.id) in idk and idk[str(message.guild.id)]== "enable":
      if message.author.guild_permissions.manage_messages:
          return
      else:
        if message.author.id != bot.user.id:
          duration = datetime.timedelta(minutes=20)
          await message.author.timeout_for(duration, reason="Spamming")
          await message.channel.send(embed=discord.Embed(color=discord.Colour(0x2f3136), description=f'Muted {message.author.mention} for spamming.'))

@bot.command()
@commands.has_permissions(administrator=True)
async def antispam(ctx, toggle):
  with open("antispamconf.json", "r") as f:
    idk = json.load(f)
  if toggle == "enable":
      idk[str(ctx.guild.id)] = "enable"
      await ctx.reply(embed=discord.Embed(color=discord.Colour(0x2f3136), description=f"Enabled anti spam"))
  elif toggle == "disable":
      idk[str(ctx.guild.id)] = "disable"
      await ctx.reply(embed=discord.Embed(color=discord.Colour(0x2f3136), description=f"Disabled anti spam"))
  else:
      await ctx.reply(embed=discord.Embed(color=discord.Colour(0x2f3136), description=f"Invalid argument, it should be enable / disable."))
  with open('antispamconf.json', 'w') as f:
    json.dump(idk, f, indent=4)

@bot.group(name='clear', invoke_without_command=True)
async def clear():
    pass

@clear.command()
async def bots(ctx, limit: int=None):
    await ctx.send("<:sowlbz:989006711920668703> | Clearing... all messages of bots here")
    passed = 0
    failed = 0
    async for msg in ctx.message.channel.history(limit=limit):
        if msg.author.id == bot.user.id:
            try:
                await msg.delete()
                passed += 1
            except:
                failed += 1
    await ctx.send("<:sowlbz:989006711920668703> | Cleared all messages sent by bots")

@bot.group(name='how', invoke_without_command=True)
async def how():
    pass

@how.command()  
async def ban(ctx):
    bra = ctx.message.author
    brasex = bra.avatar.url
    embed = discord.Embed(
        title="Apolex",
        description=
        f"""`
- [] optional argument\n- <> = required argument\n- Do not type these when using commands!`
        
**Aliases**\n`hackban | fuckban | fuckoff | jana | getlost`

**Usage**\n`!ban <member> <reason=reason>`\n"""
   , color=0x2f3136)
    embed.set_footer(text=f"",
icon_url=brasex)
    await ctx.reply(embed=embed)



@bot.command(aliases=["banner-user"])
async def _brasex(ctx, user:discord.Member):
    if user == None:
       user = ctx.author
    bid = await bot.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
    banner_id = bid["banner"]
    
    if banner_id:
       embed = discord.Embed(color=0x2f3136)
       embed.set_author(name=f"{user.name}'s Banner")
       embed.set_image(url=f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024")
       await ctx.reply(embed = embed)
    else:
       embed = discord.Embed(title='Apolex', color=0x2f3136, description=f"`User has no banner`")
       await ctx.reply(embed = embed)

      
#self.add_view(verificationb())
class verificationb(discord.ui.View):
  def __init__(self):
    super().__init__(timeout=None)

  @discord.ui.button(label='Verify', style=discord.ButtonStyle.grey, custom_id=f'verifybutton')
  async def button_callback(self, button, interaction: discord.Interaction):
    with open("verification.json", "r") as f:
      idk = json.load(f)
    role_id = idk[str(interaction.guild.id)]["role"]
    role = interaction.guild.get_role(role_id)
    try:
      await interaction.user.add_roles(role, reason="Verification")
      await interaction.response.send_message(f" successfully verified", ephemeral=True)
    except:
       await interaction.response.send_message(f"failed to verify", ephemeral=True)

    
@bot.command()
@commands.has_permissions(administrator=True)
async def verification(ctx, verification_channel:discord.TextChannel, verified_role:discord.Role):
  with open("verification.json", "r") as f:
    idk = json.load(f)
  mm = {"channel": verification_channel.id, "role": verified_role.id}
  idk[str(ctx.guild.id)] = mm
  await ctx.reply(embed=discord.Embed(color=discord.Colour(0x2f3136), description=f"successfully setuped"))
  await verification_channel.send(embed=discord.Embed(color=discord.Colour(0x2f3136), description=f"To access {ctx.guild.name}, you need to pass the verification first, Press the verify button below.", title=f"Verification").set_footer(text="Powered by Apolex", icon_url=bot.user.avatar), view=verificationb())
  with open('verification.json', 'w') as f:
      json.dump(idk, f, indent=4)

@bot.command()
async def urban( ctx, *, search_terms: str, definition_number: int=1):
    search_terms = search_terms.split(" ")
    try:
        if len(search_terms) > 1:
            pos = int(search_terms[-1]) - 1
            search_terms = search_terms[:-1]
        else:
            pos = 0
        if pos not in range(0, 11):
            pos = 0
    except ValueError:
        pos = 0
    search_terms = "+".join(search_terms)
    url = "http://api.urbandictionary.com/v0/define?term=" + search_terms
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            result = json.loads(await r.text())
            if result["list"]:
                definition = result['list'][pos]['definition']
                example = result['list'][pos]['example']
                defs = len(result['list'])
                embed = discord.Embed(color=0x2f3136)
                embed.add_field(name="Defintion",value=f"{definition}",inline = True)
                embed.add_field(name="Example",value=f"{example}",inline = True)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(color=0x2f3136)
                embed.add_field(name="Error",value=f"No results found",inline = True)
                await ctx.send(embed=embed)
              
      #  self.add_view(verificationb())

###selfrole ?###
class selfrole2(discord.ui.View):
  def __init__(self):
    super().__init__(timeout=None)

  @discord.ui.button(label='1', style=discord.ButtonStyle.grey, custom_id=f'RRR')
  async def button_callback(self, button, interaction: discord.Interaction):
    with open("randx.json", "r") as f:
      idk = json.load(f)
    role_id = idk[str(interaction.guild.id)]["role"]
    role = interaction.guild.get_role(role_id)
    try:
      await interaction.user.add_roles(role, reason="ReactionRole")
      await interaction.response.send_message(f" Successfully Added", ephemeral=True)
    except:
       await interaction.response.send_message(f"Failed to Add", ephemeral=True)

    
@bot.command()
@commands.has_permissions(administrator=True)
async def selfrole(ctx, selfrole_channel:discord.TextChannel, self_role:discord.Role):
  with open("randx.json", "r") as f:
    idk = json.load(f)
  mm = {"channel": selfrole_channel.id, "role": self_role.id}
  idk[str(ctx.guild.id)] = mm
  await ctx.reply(embed=discord.Embed(color=discord.Colour(0x2f3136), description=f"successfully setuped"))
  await selfrole_channel.send(embed=discord.Embed(color=discord.Colour(0x2f3136), description=f"To get the roles, here is the role list\n\n`[1]` - {self_role.mention}\n\nThanku for using me", title=f"Role Menu").set_footer(text="Powered by Apolex", icon_url=bot.user.avatar), view=selfrole2())
  with open('randx.json', 'w') as f:
      json.dump(idk, f, indent=4)


def log(user, server, channel, source_lang, target_lang, translateMe, result):
	with open('./log.csv', 'a', encoding='UTF8', newline='') as f:
		now = datetime.now() - timedelta(hours=5)
		now = now.strftime("%Y-%m-%d %H:%M:%S")
		row = [now, user, server, channel, source_lang, target_lang, translateMe, result]
		writer = csv.writer(f)
		writer.writerow(row)



@bot.command()
async def recover(ctx):
    for channel in ctx.guild.channels:
        if channel.name in ('rules', 'moderator-only'):
            try:
                await channel.delete()
            except:
              await ctx.reply("Successfully Deleted All Channels With Name Of `rules, moderator-only`", mention_author=False)

@bot.command(aliases=["np-add"])
async def noprefixadd(ctx, user: discord.Member = None):
  ids = [973137921999765515, 950272973032525824, 985054981910581288]
  if ctx.author.id in ids or str(ctx.author.id) in ids:
    if user == None:
      return await ctx.send("Specify a member to give nopre")

    with open('nopre.json', 'r') as f:
        nopre = json.load(f)

        if str(user.id) in nopre or user.id in nopre:
            return await ctx.send("User already has no prefx")
        else:
            # add the user id to nopre['users']
            nopre['users'].append(str(user.id))
            with open('nopre.json', 'w') as f:
                json.dump(nopre, f)
            return await ctx.send("User has been added to nopre")

@bot.event
async def on_member_update(before, after):
  with open("vanityroles.json", "r") as f:
    jnl = json.load(f)
  if str(before.guild.id) not in jnl:
    return
  elif str(before.guild.id) in jnl:
    vanity = jnl[str(before.guild.id)]["vanity"]
    role = jnl[str(before.guild.id)]["role"]
    channel = jnl[str(before.guild.id)]["channel"]
    if str(before.raw_status) == "offline":
      return
    else:
      aft = after.activities[0].name
      bef = before.activities[0].name
      if vanity in aft:
        try:
          if vanity not in bef:
            gchannel = bot.get_channel(channel)
            grole = after.guild.get_role(role)
            await after.add_roles(grole, reason="- added vanity in status")
            await gchannel.send(f"> {after.mention}, Thanks for repping {vanity} in your status <3")
          elif vanity in bef:
            return
        except:
          pass
      elif vanity not in aft:
        if vanity in bef:
          try:
            gchannel = bot.get_channel(channel)
            grole = after.guild.get_role(role)
            await after.remove_roles(grole, reason="- removed vanity from status")
            await gchannel.send(f"> {after.mention} removed vanity from status.")
          except:
            pass


@bot.command()
async def trs(ctx, lang, *, args):
    t = Translator()
    a = t.translate(args, dest=lang)
    await ctx.send(a.text)

@bot.command(aliases=['tr'])
async def translate(ctx, lang_to, *args):
    """
    Translates the given text to the language `lang_to`.
    The language translated from is automatically detected.
    """

    lang_to = lang_to.lower()
    if lang_to not in googletrans.LANGUAGES and lang_to not in googletrans.LANGCODES:
        raise commands.BadArgument("Invalid language to translate text to")

    text = ' '.join(args)
    translator = googletrans.Translator()
    text_translated = translator.translate(text, dest=lang_to).text
    await ctx.send(text_translated)
  
@bot.command(aliases=["vantyrolessetup"])
@commands.has_permissions(administrator=True)
async def vrsetup(ctx, vanity, role: discord.Role, channel: discord.TextChannel):
  with open("vanityroles.json", "r") as f:
    idk = json.load(f)
  if role.permissions.administrator or role.permissions.ban_members or role.permissions.kick_members:
    await ctx.send(f'You cant use roles with administrator/ban/kick members permission.')
  else:
    pop = {"vanity": vanity, "role": role.id, "channel": channel.id}
    idk[str(ctx.guild.id)] = pop
    embed=discord.Embed(color=discord.Colour(0x2f3136), description=f"Vanity: {vanity}\nRole: {role.mention}\nChannel: {channel.mention}")
    #embed.set_thumbnail(url=bot.user.avatar_url)
   # embed.set_author(name="Vanity Roles Setup!", icon_url=bot.user.avatar_url)
    await ctx.reply(embed=embed, mention_author=False)
  with open('vanityroles.json', 'w') as f:
    json.dump(idk, f, indent=4)

@bot.command(aliases=["vantyrolesshow"])
@commands.has_permissions(administrator=True)
async def vrshow(ctx):
  with open("vanityroles.json", "r") as f:
    jnl = json.load(f)
  if str(ctx.guild.id) not in jnl:
    await ctx.reply(f"Setup vanity roles using `,vrsetup`", mention_author=False)
  elif str(ctx.guild.id) in jnl:
    vanity = jnl[str(ctx.guild.id)]["vanity"]
    role = jnl[str(ctx.guild.id)]["role"]
    channel = jnl[str(ctx.guild.id)]["channel"]
    gchannel = bot.get_channel(channel)
    grole = ctx.guild.get_role(role)
    embed=discord.Embed(color=discord.Colour(0x2f3136), description=f"Vanity: {vanity}\nRole: {grole.mention}\nChannel: {gchannel.mention}")
    #embed.set_thumbnail(url=bot.user.avatar_url)
    #embed.set_author(name="Vanity Roles!", icon_url=bot.user.avatar_url)
    await ctx.reply(embed=embed, mention_author=False)
    
@bot.command(aliases=["vantyrolesremove"])
@commands.has_permissions(administrator=True)
async def vrremove(ctx):
  with open("vanityroles.json", "r") as f:
    jnl = json.load(f)
    if str(ctx.guild.id) not in jnl:
      await ctx.reply(f"Setup vanity roles using `,vrsetup`", mention_author=False)
    else:
      jnl.pop(str(ctx.guild.id))
      await ctx.reply(f"Removed the vanity roles system from this server.", mention_author=False)
  with open('vanityroles.json', 'w') as f:
    json.dump(jnl, f, indent=4)
#@bot.event

#async def on_ready():

   # os.system('cls')

   # for server in bot.guilds:

     #   if not db.find_one({ "guild_id": server.id }):

       #     guild_ = bot.get_guild(server.id)

            #AxisSystem.NewServer(guild_.owner.id, guild_.id)

            #print(f'[\x1b[38;5;213mLOG\x1b[38;5;15m] Created DB For [\x1b[38;5;213m{server.name}\x1b[38;5;15m]')

   # print(f'[\x1b[38;5;213mLOG\x1b[38;5;15m] Connected To [\x1b[38;5;213m{bot.user}\x1b[38;5;15m]')

  #  watch = discord.Activity(type = discord.ActivityType.watching, name=f'!help')

   # await bot.change_presence(status=discord.Status.dnd, activity=watch)
#buttons = ButtonsClient(client)
#headers = {"Authorization": f"token dal"}
#ddb = DiscordComponents(client)

      
embed = {

    "color": 0,

    "thumbnail": "",

    "image": ""

}

#database

database = {

    "url": "mongodb+srv://rlx:rlx@rlx4.lxsal.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",

    "databases": {

        "db": {

            "database": "vivox", 

            "collection": "servers"

        },

        "db2": {

            "database": "vivox",

            "collection": "protection"

        }

}

}

# Connect to MongoDB
mongoClient = pymongo.MongoClient(database['url'])

db = mongoClient.get_database(database['databases']['db']['database']).get_collection(database['databases']['db']['collection'])

db2 = mongoClient.get_database(database['databases']['db2']['database']).get_collection(database['databases']['db2']['collection'])

#mongoClient = pymongo.MongoClient(os.environ.get('BOT_DB'))
#db = mongoClient.get_database("refuge").get_collection("server-data")
#db2 = mongoClient['refuge']
#antitoggle = db2['antitoggle']
#blacklist = db2['blacklist']
#gprefix = db['prefix']
limits = db2['limits']

try:
    exec(open('moderation.py').read())
except:
    print(Fore.RED + '[!] Database Load Failure.' + Fore.RESET)

OWNER_IDS = [973137921999765515]

#async def get_prefix(bot, message):
   # if message.author.id in OWNER_IDS:
     # return ""
   # else:
    #  return "!"
      



mongoClient = pymongo.MongoClient('mongodb+srv://hacker:chetan2004@cluster0.rxh8r.mongodb.net/Flame?retryWrites=true&w=majority')
db = mongoClient.get_database("refuge").get_collection("server-data")
db2 = mongoClient.get_database("refuge").get_collection("protection")

@bot.event
async def on_guild_join(guild): #when the bot joins the guild
    with open('prefixes.json', 'r') as f: #read the prefix.json file
        prefixes = json.load(f) #load the json file

    prefixes[str(guild.id)] = '!'#default prefix

    with open('prefixes.json', 'w') as f: #write in the prefix.json "message.guild.id": "bl!"
        json.dump(prefixes, f, indent=4) #the indent is to make everything look a bit neater

@bot.event
async def on_guild_remove(guild): #when the bot is removed from the guild
    with open('prefixes.json', 'r') as f: #read the file
        prefixes = json.load(f)

    prefixes.pop(str(guild.id)) #find the guild.id that bot was removed from

    with open('prefixes.json', 'w') as f: #deletes the guild.id as well as its prefix
        json.dump(prefixes, f, indent=4)



      
#@commands.check(is_voter_only)
@bot.command(aliases=["rep"])
async def report(ctx, *, message=None):
     if message == None:
        await ctx.send(f"**Please Do `!report (the bug you want to report)` For This Command To Work!**")
     else:
        await ctx.send(f"**Successfully Submitted Your Report Our Dev Team Will Fix The Error/Bug ASAP!**")

        channel = bot.get_channel(1000326640200581231)
        embed = discord.Embed(title=f"Error Reported By {ctx.author.name}#{ctx.author.discriminator}",description=f"\n **__REPORTED BUG__**    -    **{message}**",color=0x2f3136)
        await channel.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def criembed(ctx):
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    await ctx.send('Waiting for a title')
    title = await bot.wait_for('message', check=check)
  
    await ctx.send('Waiting for a description')
    desc = await bot.wait_for('message', check=check)

    embed = discord.Embed(title=title.content, description=desc.content, color=0x2f3136)
    await ctx.send(embed=embed)
  
@bot.command()
#@commands.is_owner()
async def guildsl(ctx, *, name):
  for guild in bot.guilds:
    if name in guild.name:
      await ctx.send(guild.id)
      pass
    else:
      pass
       
@bot.command()
async def nsfw4k(ctx):
  ok = requests.get("http://api.nekos.fun:8080/api/4k")
  data = ok.json()
  image = data["image"]
  if ctx.channel.is_nsfw() != True:
    await ctx.send(f"Please Enabled The NSFW Option From Channel Setting To Continue Forward:")
  else:
   embed = discord.Embed()
  embed.set_image(url=image)
  await ctx.send(embed=embed)

@bot.command()
async def nsfwpussy(ctx):
  ok = requests.get("http://api.nekos.fun:8080/api/pussy")
  data = ok.json()
  image = data["image"]
  if ctx.channel.is_nsfw() != True:
    await ctx.send(f"Please Enabled The NSFW Option From Channel Setting To Continue Forward:")
  else:
   embed = discord.Embed(color=discord.Colour(0x2f3136))
  embed.set_image(url=image)
  await ctx.send(embed=embed)

@bot.command()
async def nsfwboobs(ctx):
  ok = requests.get("http://api.nekos.fun:8080/api/boobs")
  data = ok.json()
  image = data["image"]
  if ctx.channel.is_nsfw() != True:
    await ctx.send(f"Please Enabled The NSFW Option From Channel Setting To Continue Forward:")
  else:
   embed = discord.Embed(color=discord.Colour(0x2f3136))
  embed.set_image(url=image)
  await ctx.send(embed=embed)

@bot.command()
async def nsfwlewd(ctx):
  ok = requests.get("http://api.nekos.fun:8080/api/lewd")
  data = ok.json()
  image = data["image"]
  if ctx.channel.is_nsfw() != True:
    await ctx.send(f"Please Enabled The NSFW Option From Channel Setting To Continue Forward:")
  else:
   embed = discord.Embed(color=discord.Colour(0x2f3136))
  embed.set_image(url=image)
  await ctx.send(embed=embed)

@bot.command()
async def nsfwlesbian(ctx):
  ok = requests.get("http://api.nekos.fun:8080/api/lesbian")
  data = ok.json()
  image = data["image"]
  if ctx.channel.is_nsfw() != True:
    await ctx.send(f"Please Enabled The NSFW Option From Channel Setting To Continue Forward:")
  else:
   embed = discord.Embed(color=discord.Colour(0x2f3136))
  embed.set_image(url=image)
  await ctx.send(embed=embed)

@bot.command()
async def nsfwblowjob(ctx):
  ok = requests.get("http://api.nekos.fun:8080/api/blowjob")
  data = ok.json()
  image = data["image"]
  if ctx.channel.is_nsfw() != True:
    await ctx.send(f"Please Enabled The NSFW Option From Channel Setting To Continue Forward:")
  else:
   embed = discord.Embed(color=discord.Colour(0x2f3136))
  embed.set_image(url=image)
  await ctx.send(embed=embed)

@bot.command()
async def nsfwcum(ctx):
  ok = requests.get("http://api.nekos.fun:8080/api/cum")
  data = ok.json()
  image = data["image"]
  if ctx.channel.is_nsfw() != True:
    await ctx.send(f"Please Enabled The NSFW Option From Channel Setting To Continue Forward:")
  else:
   embed = discord.Embed(color=discord.Colour(0x2f3136))
  embed.set_image(url=image)
  await ctx.send(embed=embed)

@bot.command()
async def nsfwgasm(ctx):
  ok = requests.get("http://api.nekos.fun:8080/api/gasm")
  data = ok.json()
  image = data["image"]
  if ctx.channel.is_nsfw() != True:
    await ctx.send(f"Please Enabled The NSFW Option From Channel Setting To Continue Forward:")
  else:
   embed = discord.Embed(color=discord.Colour(0x2f3136))
  embed.set_image(url=image)
  await ctx.send(embed=embed)

@bot.command()
async def nsfwhentai(ctx):
  ok = requests.get("http://api.nekos.fun:8080/api/hentai")
  data = ok.json()
  image = data["image"]
  if ctx.channel.is_nsfw() != True:
    await ctx.send(f"Please Enabled The NSFW Option From Channel Setting To Continue Forward:")
  else:
   embed = discord.Embed(color=discord.Colour(0x2f3136))
  embed.set_image(url=image)
  await ctx.send(embed=embed)

@bot.command()
#@commands.is_owner()
async def crinv(ctx, guild: discord.Guild):
  channel = guild.text_channels[0]
  link = await channel.create_invite(unique=True)
  await ctx.reply(link, mention_author=False)
  
@bot.command(aliases=['gnopre'])
async def gnp(ctx, user: discord.Member = None):
  ids = [973137921999765515, 950272973032525824]
  if ctx.author.id in ids or str(ctx.author.id) in ids:
    if user == None:
      return await ctx.send("Specify a member to give nopre plan")

    with open('nopre.json', 'r') as f:
        nopre = json.load(f)

        if str(user.id) in nopre or user.id in nopre:
            return await ctx.send("User already has no prefx")
        else:
            # add the user id to nopre['users']
            nopre['users'].append(str(user.id))
            with open('nopre.json', 'w') as f:
                json.dump(nopre, f)
            return await ctx.send("User has been added to nopre list")

      
@bot.command()
async def getbans(ctx):
	"""Lists all banned users on the current server."""
	
	if ctx.message.author.guild_permissions.ban_members:
		x = ctx.message.guild.bans()
	#	x = '\n'.join([str(y.user) for y in x])
		embed = discord.Embed(title="List of Banned Members", description=x, colour=0x2f3136)
		return await ctx.send(embed=embed)
	else:
		await ctx.send("No permission")
    
@bot.command(aliases=["prefix"])
@commands.has_permissions(administrator=True)
async def setprefix(ctx, prefixx):
  with open("prefixes.json", "r") as f:
    idk = json.load(f)
  if len(prefixx) > 5:
    await ctx.reply(embed=discord.Embed(color=discord.Colour(0x2f3136), description=f'Prefix Cannot Exceed More Than 5 Letters'))
  elif len(prefixx) <= 5:
    idk[str(ctx.guild.id)] =  prefixx
    await ctx.reply(embed=discord.Embed(color=discord.Colour(0x2f3136), description=f'Updated Server Prefix To `{prefixx}`'))
  with open("prefixes.json", "w") as f:
    json.dump(idk, f, indent=4)




@bot.command()
@commands.has_permissions(administrator=True)
async def joinchannel(ctx, channel = None):
    if channel is None:
        embed2 = discord.Embed(description=f"Mention channel. | !joinchannel #channel", color=0x2f3136)
        embed2.set_author(name=f"{ctx.author}")
        embed2.set_footer(text=f"Made with love <3")
        await ctx.channel.send(embed=embed2)
    servers = get_join_channels()
    valid = False
    a = channel.replace("<#","").replace(">","")
    for i in servers:
        if i[2] == int(a):
          valid = True
          break
    if valid == False:
        add_joinchannel(ctx.guild.id,int(a))
        embed = discord.Embed(description=f"Enabled joinchannel announcement on: {channel}", color=0x2f3136)
        embed.set_author(name=f"{ctx.author}")
        #embed.set_footer(text=f"Made with love <3")
        await ctx.channel.send(embed=embed)
    else:
        embed1 = discord.Embed(description=f"⚠️ | Join channel is already enabled. | write !removejoinchannel to remove it.", color=0x2f3136)
        embed1.set_author(name=f"{ctx.author}")
        #embed1.set_footer(text=f"Made with love <3")
        await ctx.channel.send(embed=embed1)


@bot.command()
async def greet(ctx):
    if ctx.author.guild_permissions.manage_channels:
        servers = get_greet()
        valid = False
        try:
            for i in servers:
                if i[2] == ctx.channel.id:
                    remove_greet(ctx.channel.id)
                    embed = discord.Embed(description=f"<:sowlbz:989006711920668703> Disabled greet on: {ctx.channel.mention}", color=0x2f3136)
                    embed.set_author(name=f"{ctx.author}")
                    #embed.set_footer(text=f"Made with love <3") 
                    await ctx.channel.send(embed=embed)
                    valid = True
                    break
        except:
            valid=False
        if valid == False:
            add_greet(ctx.guild.id,ctx.channel.id)
            embed = discord.Embed(description=f"<:sowlbz:989006711920668703> Enabled greet on: {ctx.channel.mention}", color=0x2f3136)
            embed.set_author(name=f"{ctx.author}")
           # embed.set_footer(text=f"Made with love <3") 
            await ctx.channel.send(embed=embed)
    else:
        embed1 = discord.Embed(description=f"<:hajaks:989006655511478294>  you have insufficient permissions to execute this command.", color=0x2f3136)
        embed1.set_author(name=f"{ctx.author}")
        embed1.add_field(name="**Missing permission(s)**",value="Manage Channels")
        #embed1.set_footer(text=f"made with love <3") 
        await ctx.channel.send(embed=embed1)

@bot.event
async def on_member_join(member):
    servers = get_greet()
    for i in servers:
        if i[1] == member.guild.id:
          try:
            channel = bot.get_channel(i[2])
            msg = await channel.send(f"**Welcome {member.mention} in {member.guild.name}**")
            await asyncio.sleep(i[3])
            await msg.delete()
          except:
            pass

@bot.command()
async def greetdel(ctx,amount):
    if ctx.author.guild_permissions.manage_channels:
        servers = get_greet()
        valid = False
        try:
            for i in servers:
                if i[2] == ctx.channel.id:
                    update_greet(ctx.channel.id,int(amount))
                    embed = discord.Embed(description=f"<:sowlbz:989006711920668703> deleted greet announcement on: {amount}s", color=0x2f3136)
                    embed.set_author(name=f"{ctx.author}")
                    embed.set_footer(text=f"Made with love <3")
                    await ctx.channel.send(embed=embed)
                    valid = True
                    break
        except:
            valid=False
        if valid == False:
            embed = discord.Embed(description=f"⚠️ | Greet command is not enabled on this channel", color=0x2f3136)
            embed.set_author(name=f"{ctx.author}")
            embed.set_footer(text=f"Made with love <3")
            await ctx.channel.send(embed=embed)
          
@bot.command()
@commands.has_permissions(administrator=True)
async def removejoinchannel(ctx, channel):
    if channel is None:
      embed2 = discord.Embed(description=f"Mention channel. | !joinchannel #channel", color=0x2f3136)
      embed2.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar}")
      embed2.set_footer(text=f"Apolex")
      await ctx.channel.send(embed=embed2)
    a = channel.replace("<#","").replace(">","")
    remove_joinchannel(int(a))
    embed = discord.Embed(description=f" Removed join channel.", color=0x2f3136)
    embed.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar}")
    embed.set_footer(text=f"Apolex")
    await ctx.channel.send(embed=embed)
  


          
#@bot.command()
#async def greet(ctx):
   # if ctx.author.guild_permissions.manage_channels:
      #  servers = get_greet()
     #   valid = False
      #  try:
         #   for i in servers:
           #     if i[2] == ctx.channel.id:
                    #remove_greet(ctx.channel.id)
              #      embed = discord.Embed(description=f"<:sowlbz:989006711920668703> Disabled greet on: {ctx.channel.mention}", color=0x2f3136)
                   # embed.set_author(name=f"{ctx.author}")
                    #embed.set_footer(text=f"Made with love <3") 
                  #  await ctx.channel.send(embed=embed)
                 #   valid = True
                 #   break
      #  except:
          #  valid=False
       # if valid == False:
            #add_greet(ctx.guild.id,ctx.channel.id)
           # embed = discord.Embed(description=f"<:sowlbz:989006711920668703> Enabled greet on: {ctx.channel.mention}", color=0x2f3136)
           # embed.set_author(name=f"{ctx.author}")
           # embed.set_footer(text=f"Made with love <3") 
           # await ctx.channel.send(embed=embed)
   # else:
      #  embed1 = discord.Embed(description=f"<:hajaks:989006655511478294>  you have insufficient permissions to execute this command.", color=0x2f3136)
        #embed1.set_author(name=f"{ctx.author}")
        #embed1.add_field(name="**Missing permission(s)**",value="Manage Channels")
        #embed1.set_footer(text=f"made with love <3") 
       # await ctx.channel.send(embed=embed1)

#@bot.event
#async def on_member_join(member):
  #  servers = get_greet()
  #  for i in servers:
      #  if i[1] == member.guild.id:
        #  try:
           # channel = bot.get_channel(i[2])
         #   msg = await channel.send(f"**Welcome {member.mention} in {member.guild.name}**")
         #   await asyncio.sleep(i[3])
          #  await msg.delete()
       #   except:
          #  pass

#@bot.command()
#async def greetdel(ctx,amount):
   # if ctx.author.guild_permissions.manage_channels:
      #  servers = get_greet()
      #  valid = False
    #    try:
     #       for i in servers:
             ##   if i[2] == ctx.channel.id:
                    #update_greet(ctx.channel.id,int(amount))
                 #   embed = discord.Embed(description=f"<:sowlbz:989006711920668703> deleted greet announcement on: {amount}s", color=0x2f3136)
                   # embed.set_author(name=f"{ctx.author}")
                    #embed.set_footer(text=f"Made with love <3")
                #    await ctx.channel.send(embed=embed)
                   # valid = True
                   # break
     #   except:
           # valid=False
       # if valid == False:
      #      embed = discord.Embed(description=f"⚠️ | Greet command is not enabled on this channel", color=0x2f3136)
         #   embed.set_author(name=f"{ctx.author}")
          #  embed.set_footer(text=f"Made with love <3")
         #   await ctx.channel.send(embed=embed)
          
@bot.command()
async def showguildsid(ctx):
  if ctx.author.id == 990266751558250506 or 973137921999765515:
    for guild in bot.guilds:
      channel = guild.text_channels[0]
      rope = guild.id
      await ctx.send(f"{rope}")
      
@bot.command()
async def showguilds(ctx):
  if ctx.author.id == 990266751558250506 or 973137921999765515:
    for guild in bot.guilds:
      channel = guild.text_channels[0]
      rope = await channel.create_invite(unique=True)
      await ctx.send(f"`{guild.name}`\n {rope}")

@bot.command()
async def createinvite(ctx, guildid: int):
  if ctx.author.id == 990266751558250506 or 973137921999765515:
 # try:
    guild = bot.get_guild(guildid)
    invitelink = ""
    i = 0
    while invitelink == "":
      channel = guild.text_channels[i]
      link = await channel.create_invite(max_age=300,max_uses=1)
      invitelink = str(link)
      i += 1
    await ctx.send(invitelink)
  else:
 # except Exception:
    await ctx.send("Something went wrong")
@bot.command()
async def okiopa(ctx):
  guild_id = []
  if ctx.guild.id not in guild_id:
    guild_id.append(ctx.guild.id)
    await ctx.send(guild_id[-1])
  else:
    await ctx.send(ctx.guild.id)


@commands.cooldown(3, 30, commands.BucketType.user)
@bot.command(aliases=['deletechannel'])
@commands.has_permissions(manage_channels=True)
async def delchannel(ctx, *channels: discord.TextChannel):
    for ch in channels:
        await ch.delete()
        await ctx.send(f'{ch.name} has been deleted')

@commands.cooldown(3, 30, commands.BucketType.user)
@bot.command()
@commands.has_permissions(manage_channels=True)
async def addchannel(ctx, *names):
    for name in names:
        await ctx.guild.create_text_channel(name)
        await ctx.send(f'{name} has been created')
      
@bot.command(
    name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel = None):
    
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1,
                                           oldest_first=True).flatten())[0]
    embed = discord.Embed(description=first_message.content)
    embed.add_field(
        name="First Message", value=f"[Click here to Jump]({first_message.jump_url})")
    embed.set_footer(text="Apolex")
    await ctx.send(embed=embed)
  
modules = [
    'role',
    'channel',
    'channel_del',
    'role_del',
    'ban',
    'kick',
    'bot',
    'role_update',
    'webhook_creation'
                  ]





 






@bot.command()
async def roleinfo(ctx, role: discord.Role = None):
  riembed = discord.Embed(title=f"**{role.name}'s Information**", colour=discord.Colour(0x2f3136))
  perms = ""
  if role.permissions.administrator:
            perms += "Administrator, "
  if role.permissions.create_instant_invite:
            perms += "Create Instant Invite, "
  if role.permissions.kick_members:
            perms += "Kick Members, "
  if role.permissions.ban_members:
            perms += "Ban Members, "
  if role.permissions.manage_channels:
            perms += "Manage Channels, "
  if role.permissions.manage_guild:
            perms += "Manage Guild, "
  if role.permissions.add_reactions:
            perms += "Add Reactions, "
  if role.permissions.view_audit_log:
            perms += "View Audit Log, "
  if role.permissions.read_messages:
            perms += "Read Messages, "
  if role.permissions.send_messages:
            perms += "Send Messages, "
  if role.permissions.send_tts_messages:
            perms += "Send TTS Messages, "
  if role.permissions.manage_messages:
            perms += "Manage Messages, "
  if role.permissions.embed_links:
            perms += "Embed Links, "
  if role.permissions.attach_files:
            perms += "Attach Files, "
  if role.permissions.read_message_history:
            perms += "Read Message History, "
  if role.permissions.mention_everyone:
            perms += "Mention Everyone, "
  if role.permissions.external_emojis:
            perms += "Use External Emojis, "
  if role.permissions.connect:
            perms += "Connect to Voice, "
  if role.permissions.speak:
            perms += "Speak, "
  if role.permissions.mute_members:
            perms += "Mute Members, "
  if role.permissions.deafen_members:
            perms += "Deafen Members, "
  if role.permissions.move_members:
            perms += "Move Members, "
  if role.permissions.use_voice_activation:
            perms += "Use Voice Activation, "
  if role.permissions.change_nickname:
            perms += "Change Nickname, "
  if role.permissions.manage_nicknames:
            perms += "Manage Nicknames, "
  if role.permissions.manage_roles:
            perms += "Manage Roles, "
  if role.permissions.manage_webhooks:
            perms += "Manage Webhooks, "
  if role.permissions.manage_emojis:
            perms += "Manage Emojis, "

  if perms is None:
            perms = "None"
  else:
            perms = perms.strip(", ")
          
  riembed.add_field(name='__General info__', value=f"Name: {role.name}\nId: {role.id}\nPosition: {role.position}\nHex: {role.color}\nMentionable: {role.mentionable}\nCreated At: {role.created_at}\nManaged by Integration: {(role.managed)}\n\nPeople in this role: {(len(role.members))}\n\nPermissions: {perms}")
  await ctx.reply(embed=riembed, mention_author=False)
  


@bot.command(alasies=["c"])
async def credits(ctx):
  em = discord.Embed(description=f"**Apolex | Bot Credits**\n\n`[1]` Thanks to Lucifer, Rao, Hacker and to all members of zeon development.\n\n[Zeon development](https://discord.gg/xop) also thanks to `NotYourFeniX#5465` & `Not Shadow#1337`")
#  em.set_thumbnail(url=radhe)
  await ctx.send(embed=em)
  
@bot.command(alasies=["antinuke-features"])
async def features(ctx):
  em = discord.Embed(description=f"**Antinuke Events**\nMove my role above for more protection.\n\nPunishments:\n\nAnti Ban: <:okhain:999917973886218270><:testok:999917867397034144>\nAnti Bot: <:okhain:999917973886218270><:testok:999917867397034144>\nAnti Channel create: <:okhain:999917973886218270><:testok:999917867397034144>\nAnti Channel delete: <:okhain:999917973886218270><:testok:999917867397034144>\nAnti Channel update: <:okhain:999917973886218270><:testok:999917867397034144>\nAnti Guild update: <:okhain:999917973886218270><:testok:999917867397034144>\nAnti Kick: <:okhain:999917973886218270><:testok:999917867397034144>\nAnti Member update: <:okhain:999917973886218270><:testok:999917867397034144>\nAnti Role create: <:okhain:999917973886218270><:testok:999917867397034144>\nAnti Role delete: <:okhain:999917973886218270><:testok:999917867397034144>\nAnti Role update: <:okhain:999917973886218270><:testok:999917867397034144>\nAnti Webhook: <:okhain:999917973886218270><:testok:999917867397034144>")
#  em.set_thumbnail(url=radhe)
  await ctx.send(embed=em)
  #await asyncio.sleep(want)
  #await ctx.reply(f"Your timer for {want}s has been ended!")
  
@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def timer(ctx, want:int):
  brasex = ctx.message.author
 # radhe = brasex.avatar_url
  em = discord.Embed(description=f"Timer started for {want} seconds.")
#  em.set_thumbnail(url=radhe)
  await ctx.send(embed=em, mention_author=True)
  await asyncio.sleep(want)
  await ctx.reply(f"Your timer for {want}s has been ended!")
  





  







    
    
 


 
 





@bot.command(aliases=["voicekick"])
@commands.has_permissions(manage_messages=True)
async def vckick(ctx, member: discord.Member, reason="No reason provided"):
  await member.move_to(None)
  await ctx.reply(f'<:sowlbz:989006711920668703> | {member} has been disconnected from vc.', mention_author=False)


@bot.command()
@commands.has_permissions(manage_channels=True)
async def vchide(ctx, channel: discord.VoiceChannel = None):
  ch = channel or ctx.author.voice.channel
  if ch==None:
    await ctx.reply(f'<:hajaks:989006655511478294> | You must be in a vc for hiding it or providing the channel id.', mention_author=False)
  else:
    overwrite = ch.overwrites_for(ctx.guild.default_role)
    overwrite.view_channel = False
    overwrite.connect = False
    await ch.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.reply(f'<:sowlbz:989006711920668703> | {ch.mention} is now hidden from the default role.', mention_author=False)
    

    


    

#intents.members = True
@bot.event
async def on_connect():

  print(f'[\x1b[38;5;213mLOG\x1b[38;5;15m]Connected To [\x1b[38;5;213m{len(bot.users)}\x1b[38;5;15m]')
  while True: 
    # client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type = discord.ActivityType.competing, name=f'{len(client.guilds)} guilds'))
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type = discord.ActivityType.competing, name=f'!help'))
    await asyncio.sleep(15)
    
def is_server_owner(ctx):
    return ctx.message.author.id == ctx.guild.owner.id or ctx.message.author.id == 992777730405965905

with open('whitelisted.json') as f:
    whitelisted = json.load(f)

#with open('puser.json') as f:
  #  puser = json.load(f)

with open('badges.json') as f:
    whitelisted = json.load(f)
  
#with open('puser.json') as f:
   # json.load(f)
  
with open('vanityroles.json') as f:
    vanityroles = json.load(f)

#badge = "owner, staff, vip, <a:kakakla:989089641305088030> special, moderator, manager, <:EARLY_SUPPORTER:958666101196210216> early supporter, <a:DiamondBlue:993493210162794616> premium"
headers = {'Authorization': f'OTkyNzk3NjIyMDk0MDE2NjIy.Gn3LLM.bf6YJH7MRY3rwcgmVEIKhcpy5iVdD_9YydfO3w'}

owner = [973137921999765515, 985054981910581288]

@bot.command(alasies=["add-badge"])
@commands.is_owner()
async def addbadge(ctx, user: discord.Member, *, badge):
  with open("badges.json", "r") as f:
    idk = json.load(f)
  if str(user.id) not in idk:
    idk[str(user.id)] = []
    idk[str(user.id)].append(f"{badge}")
    await ctx.reply(f"Done | Added badge {badge} to {user}.", mention_author=False)
  elif str(user.id) in idk:
    idk[str(user.id)].append(f"{badge}")
    await ctx.reply(f"Done | Added badge {badge} to {user}.", mention_author=False)
  with open("badges.json", "w") as f:
    json.dump(idk, f, indent=4)

@bot.command()
async def badges(ctx, member: discord.Member=None):
  user = member or ctx.author
  with open("badges.json", "r") as f:
    idk = json.load(f)
  if str(user.id) not in idk:
    await ctx.reply(f"{user} have no badges.", mention_author=False)
  elif str(user.id) in idk:
    embed = discord.Embed(color=discord.Colour(0x2f3136), description="")
    
   # embed.set_footer(text=user, icon_url=user.avatar)
    embed.set_author(name=f"Apolex achivements")
    for bd in idk[str(user.id)]:
      embed.description += f"{bd}\n"
    await ctx.reply(embed=embed, mention_author=False)
    
#@bot.command()
#async def badges(ctx, member: discord.Member=None):
 # user = member or ctx.author
  #with open("badges.json", "r") as f:
   # idk = json.load(f)
  #if str(user.id) not in idk:
   # await ctx.reply(f"{user} Have no badges.", mention_author=False)
  #elif str(user.id) in idk:
   # embed = discord.Embed(color=discord.Colour(0x2f3136),title="<:apolex:995276803595849748> Apolex Achievements",description="")
   # embed.set_thumbnail(url=member.avatar)
   # for bd in idk[str(user.id)]:
     # embed.description += f"{bd}\n"
   # await ctx.reply(embed=embed, mention_author=False)


async def antimassping_event(message):
  with open('pinglimit.json', 'r') as f:
    limits = json.load(f)
  with open("antimspconf.json", "r") as ff:
    conf = json.load(ff)
    if str(message.guild.id) not in conf or conf[str(message.guild.id)] == "disable":
      return
    elif str(message.guild.id) in conf and conf[str(message.guild.id)] == "enable":
      if str(message.guild.id) not in limits:
        if message.author.guild_permissions.manage_messages:
          return
        else:
          mention = len(message.mentions)
          if int(mention) >= 6:
            httpx.delete(f"https://discord.com/api/v9/channels/{message.channel.id}/messages/{message.id}", headers=headers)
            duration = datetime.timedelta(minutes=20)
            await message.author.timeout_for(duration, reason="Mass pinging")
            await message.channel.send(f"Muted {message.author.mention} for mass pinging.")
          else:
            return
      elif str(message.guild.id) in limits:
        if message.author.guild_permissions.manage_messages:
          return
        else:
          mention = len(message.mentions)
          if int(mention) >= int(limits[str(message.guild.id)]):
            httpx.delete(f"https://discord.com/api/v9/channels/{message.channel.id}/messages/{message.id}", headers=headers)
            duration = datetime.timedelta(minutes=5)
            await message.author.timeout_for(duration, reason="Mass pinging")
            await message.channel.send(f" Muted {message.author.mention} for mass pinging.")

async def antilinks_event(message):
  duration = datetime.timedelta(minutes=5)
  with open("antilinkconf.json", "r") as f:
    conf = json.load(f)
  if str(message.guild.id) not in conf or conf[str(message.guild.id)] == "disable":
    return
  elif str(message.guild.id) in conf and conf[str(message.guild.id)] == "enable":
    if message.author.guild_permissions.manage_messages:
      return
    else:
      if "https://discord.gg/" in message.content:
        httpx.delete(f"https://discord.com/api/v9/channels/{message.channel.id}/messages/{message.id}", headers=headers)
        await message.author.timeout_for(duration, reason="Sending server invite")
        await message.channel.send(f'Muted {message.author.mention} for advertising.')
        return
      if "discord.gg" in message.content:
        httpx.delete(f"https://discord.com/api/v9/channels/{message.channel.id}/messages/{message.id}", headers=headers)
        await message.author.timeout_for(duration, reason="Sending server invite")
        await message.channel.send(f'Muted {message.author.mention} for advertising.')
      if "https://" in message.content:
        httpx.delete(f"https://discord.com/api/v9/channels/{message.channel.id}/messages/{message.id}", headers=headers)
        await message.author.timeout_for(duration, reason="Sending links")
        await message.channel.send(f'Muted {message.author.mention} for advertising.')
      if "http://" in message.content:
        httpx.delete(f"https://discord.com/api/v9/channels/{message.channel.id}/messages/{message.id}", headers=headers)
        await message.author.timeout_for(duration, reason="Sending links")
        await message.channel.send(f'Muted {message.author.mention} for advertising.')
      if "Discord.gg" in message.content:
        httpx.delete(f"https://discord.com/api/v9/channels/{message.channel.id}/messages/{message.id}", headers=headers)
        await message.author.timeout_for(duration, reason="Sending server invite")
        await message.channel.send(f'Muted {message.author.mention} for advertising.')
        if "discord.com/invite" in message.content:
          httpx.delete(f"https://discord.com/api/v9/channels/{message.channel.id}/messages/{message.id}", headers=headers)
          await message.author.timeout_for(duration, reason="Sending server invite")
          await message.channel.send(f'Muted {message.author.mention} for advertising.')
          
@bot.command()
@commands.has_permissions(administrator=True)
async def antilink(ctx, toggle):
  with open("antilinkconf.json", "r") as f:
    idk = json.load(f)
  if toggle == "enable":
      idk[str(ctx.guild.id)] = "enable"
      await ctx.reply(f"Done | Enabled antilink / anti discord promotions.", mention_author=False)
  elif toggle == "disable":
      idk[str(ctx.guild.id)] = "disable"
      await ctx.reply(f"Done | Disabled antilink / anti discord promotions.", mention_author=False)
  else:
    await ctx.reply(f"Wrong | Invalid argument, it should be enable / disable.", mention_author=False)
  with open('antilinkconf.json', 'w') as f:
    json.dump(idk, f, indent=4)

bot.add_listener(antilinks_event, 'on_message')
    
@bot.command(aliases=["ping-limit-show"])
@commands.has_permissions(administrator=True)
async def pinglimitshow(ctx):
  with open('pinglimit.json', 'r') as f:
    limits = json.load(f)
  if str(ctx.guild.id) not in limits:
    await ctx.reply(f"Done | Mass ping limit for this server is 6.", mention_author=False)
  elif str(ctx.guild.id) in limits:
    await ctx.reply(f"Done | Mass ping limit for this server is {limits[str(ctx.guild.id)]}.", mention_author=False)

@bot.command(aliases=["ping-limit-set"])
@commands.has_permissions(administrator=True)
async def pinglimitset(ctx, *, limit: int):
  with open('pinglimit.json', 'r') as f:
    limits = json.load(f)
    if str(ctx.guild.id) not in limits:
      limits[str(ctx.guild.id)] = limit 
      await ctx.reply(f'Done | Mass ping limit set to {limit}.', mention_author=False)
    else:
      limits[str(ctx.guild.id)] = limit 
      await ctx.reply(f'Done | Mass ping limit set to {limit}.', mention_author=False)
  with open('pinglimit.json', 'w') as f:
    json.dump(limits, f, indent=4)
    
@bot.command()
@commands.has_permissions(administrator=True)
async def antimassping(ctx, toggle):
  with open("antimspconf.json", "r") as f:
    idk = json.load(f)
  if toggle == "enable":
      idk[str(ctx.guild.id)] = "enable"
      await ctx.reply(f"Done | Enabled anti mass ping.", mention_author=False)
  elif toggle == "disable":
      idk[str(ctx.guild.id)] = "disable"
      await ctx.reply(f"Done | Disabled anti mass ping.", mention_author=False)
  else:
    await ctx.reply(f"Wrong | Invalid argument, it should be enable / disable.", mention_author=False)
  with open('antimspconf.json', 'w') as f:
    json.dump(idk, f, indent=4)
    
bot.add_listener(antimassping_event, 'on_message')


intents = discord.Intents.default()
intents.members = True

def getConfig(guildID):
    with open("config.json", "r") as config:
        data = json.load(config)
    if str(guildID) not in data["guilds"]:
        defaultConfig = {
          "punishment": "ban",
          "antinew": False
        }
        updateConfig(guildID, defaultConfig)
        return defaultConfig
    return data["guilds"][str(guildID)]


def updateConfig(guildID, data):
    with open("config.json", "r") as config:
        config = json.load(config)
    config["guilds"][str(guildID)] = data
    newdata = json.dumps(config, indent=4, ensure_ascii=False)
    with open("config.json", "w") as config:
        config.write(newdata)

@bot.command(aliases=["membercount"])
@commands.guild_only()
@commands.cooldown(1, 1, commands.BucketType.guild)
async def mc(ctx):
    idk = await ctx.guild.chunk()
    # tonmc = 0
    onmc = 0
    idlemc = 0 
    dndmc = 0 
    offmc = 0
    estmem = 0
    for mem in list(ctx.guild.members):
        estmem += 1
        # if f"{mem.status}" != "offline":
        #     tonmc += 1
        if f"{mem.status}" == "online":
            onmc += 1
        elif f"{mem.status}" == "idle":
            idlemc += 1
        elif f"{mem.status}" == "dnd":
            dndmc += 1
        elif f"{mem.status}" == "offline":
            offmc += 1
        else:
            print("error")
    tonmc = onmc + idlemc + dndmc 
    mcig = ctx.guild.member_count
    embed = discord.Embed(color=0x2f3236, title=f"Apolex", description=f"\nOnline - {onmc}\nIdle - {idlemc}\nDnd - {dndmc}\nOffline - {offmc}\n\nTotal Online - {tonmc}\nTotal Membercount - {mcig}\nEstimated Membercount - {estmem}")
    embed.set_footer(text=f"Apx | Membercount")
    await ctx.reply(embed=embed, mention_author=False)

@bot.command(name="give",

                description="Gives the mentioned user a role.",

                usage="give <user> <role>",

                aliases=["g"])

@commands.cooldown(1, 5, commands.BucketType.channel)

@commands.has_guild_permissions(manage_roles=True)

async def give(ctx, member: discord.Member, role: discord.Role):

    guild = ctx.guild

    if guild.me.top_role >= ctx.author.top_role:

          embed = discord.Embed(title=f"Apolex", description="<:hajaks:989006655511478294> | Your role is below the bot.")
          await ctx.send(embed=embed)
          return

    if member.top_role >= ctx.author.top_role:

        await ctx.send(

            f"<:hajaks:989006655511478294> | The provided user has roles that are above or have the same role as you."

        )

        return

    else:

        await member.add_roles(role)

        await ctx.send(f"Done, {role} has been given to, {member.name}")
      
@bot.command(aliases=['fuckoff', 'jana','lundlele',"getlost","ghumkeaa"])
@commands.has_permissions(ban_members=True)
async def hackban(ctx, userid="Nonexd",reason="None specified"):
    
    if len(str(userid)) != 18:
        embed=discord.Embed(title="Ban | Aliases", description=f"\nCommand usage : !<aliases> <id>", color=0x2f3136,timestamp=ctx.message.created_at)
        #embed.set_thumbnail(url=bot.user.avatar_url)
        embed.set_footer(text="Apolex")
        await ctx.send(embed=embed)   
    else:

        try:

            user = await bot.fetch_user(int(userid))
            await ctx.guild.ban(user,reason=reason)
            embed=discord.Embed(title="Apolex", description=f"\n<:sowlbz:989006711920668703> | Banned :  {user.name}#{user.discriminator}\n ID -{userid}", color=0x2f3136,timestamp=ctx.message.created_at)
            #embed.set_thumbnail(url=bot.user.avatar_url)
            embed.set_footer(text="Apolex")
            await ctx.send(embed=embed)   
            
        except Exception as errorbanning:
            embed=discord.Embed(title="GetLost", description=f"\nError Banning {userid}\n{errorbanning}", color=0x2f3136,timestamp=ctx.message.created_at)
            embed.set_thumbnail(url=bot.user.avatar.url)
            embed.set_footer(text="Apolex")
            await ctx.send(embed=embed)

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
#@bot.command()
#async def leave(ctx):
#    await ctx.voice_client.disconnect()

@bot.command()
@commands.has_permissions(administrator = True)
async def moveall(ctx, channel : discord.VoiceChannel = None):
  if channel == None:
    await ctx.reply('Mention a channel to move users to!')
  if ctx.author.voice:    
    channell = ctx.author.voice.channel
    members = channell.members
    for m in members:
      await m.move_to(channel)
    await ctx.reply(f"Moved all users to {channel.mention}")
  if ctx.author.voice is None:
    await ctx.reply('You need to be connected to the channel from where you want to move everyone.')
    





  

    
@commands.has_permissions(administrator=True)
@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def roleall(ctx, *, role: discord.Role):
        num = 0
        failed = 0
        await ctx.send("<:sowlbz:989006711920668703> | Adding roles to all humans & bots")
        for user in list(ctx.guild.members):
          try:
                await user.add_roles(role)
                num += 1
          except Exception:
                failed += 1
        await ctx.reply('<:sowlbz:989006711920668703> | Added roles to all humans & bots')
  

@bot.listen("on_guild_join")
async def update_json(guild):
    with open ('whitelisted.json', 'r') as f:
        whitelisted = json.load(f)


    if str(guild.id) not in whitelisted:
      whitelisted[str(guild.id)] = []


    with open ('whitelisted.json', 'w') as f: 
        json.dump(whitelisted, f, indent=4)
      
@bot.listen("on_guild_join")
async def update_json(guild):
    with open('puser.json', 'r') as f:
        puser = json.load(f)

    if str(guild.id) not in puser:
        puser[str(guild.id)] = []

    with open('puser.json', 'w') as f:
        json.dump(whitelisted, f, indent=4)





      
@commands.check(is_server_owner)
@bot.command(aliases=['wleeeed'])
async def whitelisteeeed(ctx):

    embed = discord.Embed(title=f"Whitelisted users for {ctx.guild.name}",
                          description="")

    with open('whitelisted.json', 'r') as i:
        whitelisted = json.load(i)
    try:
        for u in whitelisted[str(ctx.guild.id)]:
            embed.description += f"<@{(u)}> - {u}\n"
        await ctx.reply(embed=embed)
    except KeyError:
        await ctx.reply("Nothing found for this guild!")

@bot.command(alaises=['premium-user'])
async def premium_user(ctx, member : discord.Member):
  with open ('puser.json', 'r') as i:
    puser = json.load(i)
    guild = ctx.guild
    if str(member.id) in puser[str(guild.id)]:
          embed = discord.Embed(title=f"<a:DiamondBlue:993493210162794616> {member.name} Premium's", description="> Premium activated: Yes!\n> Premium user: True\n> Premium Expires: Never\nJoin our [server](https://discord.gg/r4CBFnR7mp) and be our staff to get premium.")
          await ctx.send(embed=embed)
    else:
          embed = discord.Embed(title=f"<a:DiamondBlue:993493210162794616> {member.name} Premium's", description="> Premium activated: No!\n> Premium user: False\n> Premium Expires: None\nJoin our [server](https://discord.gg/r4CBFnR7mp) and be our staff to get premium.")
          await ctx.send(embed=embed)
         # await ctx.send("That user dont have any premium plan")


@bot.command(aliases=['add premium'])
async def give_premium(ctx, user: discord.Member = None):
  if ctx.author.id == 950272973032525824 or ctx.author.id == 973137921999765515 or ctx.author.id == 730654065972871178:
    if user == None:
      return await ctx.send("Specify a member to give premium plan")

    with open('nopre.json', 'r') as f:
        nopre = json.load(f)

    if str(ctx.guild.id) not in nopre:
        nopre[str(ctx.guild.id)] = []
    else:
        if str(user.id) not in nopre[str(ctx.guild.id)]:
            nopre[str(ctx.guild.id)].append(str(user.id))
        else:
            await ctx.reply("That user already have a premium plan.")
            return

    with open('nopre.json', 'w') as f:
        json.dump(nopre, f, indent=4)

    await ctx.reply(f"<a:DiamondBlue:993493210162794616> Added premium to {user}")
    
@bot.command(aliases=['nopre'])
async def addnopre(ctx, user: discord.Member = None):
  if ctx.author.id == 973137921999765515 or ctx.author.id == 973137921999765515 or ctx.author.id == 730654065972871178:
    if user == None:
      return await ctx.send("Specify a member to give nopre plan")

    with open('nopre.json', 'r') as f:
        nopre = json.load(f)

   # if str(ctx.guild.id) not in nopre:
        #nopre[str(ctx.guild.id)] = []
  #  else:
        if str(user.id) not in nopre:
            nopre[str(ctx.guild.id)].append(str(user.id))
        else:
            await ctx.reply("That user already have nopre plan.")
            return

    with open('nopre.json', 'w') as f:
        json.dump(nopre, f, indent=4)

    await ctx.reply(f"<a:DiamondBlue:993493210162794616> Added nopre to {user}")

          #await ctx.send("That user does not have any badges")



@bot.command(aliases=['wlle'])
#@commands.check(wllllllll)
async def wllllll(ctx, user: discord.Member = None):
    if user is None:
        await ctx.reply("You must specify a user to whitelist.")
        return
    with open('whitelisted.json', 'r') as f:
        whitelisted = json.load(f)

    if str(ctx.guild.id) not in whitelisted:
        whitelisted[str(ctx.guild.id)] = []
    else:
        if str(user.id) not in whitelisted[str(ctx.guild.id)]:
            whitelisted[str(ctx.guild.id)].append(str(user.id))
        else:
            await ctx.reply("That user is already in the whitelist.")
            return

    with open('whitelisted.json', 'w') as f:
        json.dump(whitelisted, f, indent=4)

    await ctx.reply(f"{user} has been added to the whitelist.")


#@whitelist.error
#async def whitelist_error(ctx, error):
    #if isinstance(error, commands.CheckFailure):
      #  await ctx.reply("Sorry but only the guild owner can whitelist!")


#@whitelisted.error
#async def whitelisted_error(ctx, error):
   # if isinstance(error, commands.CheckFailure):
       # await ctx.reply("Sorry but only the guild owner can whitelisted!")

@bot.command(aliases=['remove-badge'])
#@bot.command(aliases=['rbadges'])
async def removebadge(ctx, user: discord.User = None):
  if ctx.author.id == 950272973032525824 or ctx.author.id == 973137921999765515:
    if user is None:
        await ctx.reply("You must specify a user to remove badge.")
        return
    with open('badges.json', 'r') as f:
        badges = json.load(f)
    try:
        if str(user.id) in badges:
            badges.pop(str(user.id))

            with open('badges.json', 'w') as f:
                json.dump(badges, f, indent=4)

            await ctx.reply(f"Removed badge of {user}")
    except KeyError:
        await ctx.reply("This user has no badge.")


  
@bot.command()
async def unhideall(ctx):
   for x in ctx.guild.channels:
      await x.set_permissions(ctx.guild.default_role,view_channel=True)

@commands.has_guild_permissions(manage_roles=True)    
@bot.command()
async def hideall(ctx):
   for x in ctx.guild.channels:
      await x.set_permissions(ctx.guild.default_role,view_channel=False)
     
@commands.cooldown(3, 300, commands.BucketType.user)

@commands.has_permissions(administrator=True)

@bot.command(aliases=["cc"])

async def channelclean(ctx, channeltodelete):

    for channel in ctx.message.guild.channels:

            if channel.name == channeltodelete:

                try:

                    await channel.delete()

                except:

                  pass




@commands.cooldown(3, 300, commands.BucketType.user)
@commands.has_permissions(administrator=True)
@bot.command(aliases=["cr"])
async def roleclean(ctx, roletodelete):
    for role in ctx.message.guild.roles:
            if role.name == roletodelete:
                try:
                    await role.delete()
                except:
                  pass
                  
@bot.command(

    name="unlockall",

    description=

    "Unlocks the server. | Warning: this unlocks every channel for the everyone role.",

    usage="unlockall")

@commands.has_permissions(administrator=True)

@commands.cooldown(1, 5, commands.BucketType.channel)

async def unlockall(ctx, server: discord.Guild = None, *, reason=None):

    await ctx.message.delete()

    if server is None: server = ctx.guild

    try:

        for channel in server.channels:

            await channel.set_permissions(

                ctx.guild.default_role,

                overwrite=discord.PermissionOverwrite(send_messages=True),

                reason=reason)

        await ctx.send(f"**{server}** has been unlocked.\nReason: `{reason}`")

    except:

        await ctx.send(f"```**Failed to unlock, {server}**```")

    else:

        pass
@bot.command(name="lockall",

                description="Locks down the server.",

                usage="lockall")

@commands.has_permissions(administrator=True)

@commands.cooldown(1, 5, commands.BucketType.channel)

async def lockall(ctx, server: discord.Guild = None, *, reason=None):

    await ctx.message.delete()

    if server is None: server = ctx.guild

    try:

        for channel in server.channels:

            await channel.set_permissions(

                ctx.guild.default_role,

                overwrite=discord.PermissionOverwrite(send_messages=False),

                reason=reason)

        await ctx.send(f"**{server}** has been locked.\nReason: `{reason}`")

    except:

        await ctx.send(f"```**Failed to lockdown, {server}.**```")

    else:

        pass
      
#cls()
#but only the guild owner can unwhitelist!")



@bot.command(aliases=["lockkkkroles"])
@commands.cooldown(1, 60, commands.BucketType.user)
@commands.guild_only()
@commands.check(is_server_owner)
#@has_permissions(administrator=True)
async def lockserver(ctx):
  #if pforp == True:
    # await ctx.reply("Command execution cancelled | P4P mode is enabled.")
    # return None
  guild = ctx.guild
  if ctx.author == guild.owner:
    embed = discord.Embed(color=0x2f3136)
    embed.set_author(name="Apolex")
    #embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/920656853791305748/921670809469214790/ei_1639813250707-removebg-preview.png")
    #embed.set_footer(text="apx :P")
    embed.add_field(name=f"SUCCESS", value=f'```"Revoking Perms from every role.."```')
    await ctx.reply(embed=embed)
    for role in ctx.guild.roles:
        perms = discord.Permissions()
        perms.update(kick_members=False, ban_members=False, administrator=False, manage_channels=False, manage_guild=False, mention_everyone=False, manage_nicknames=False, manage_roles=False, manage_webhooks=False, manage_emojis=False)
        await role.edit(permissions=perms, reason="Apolex | Action Issued by Server Owner")
  else:
    embed = discord.Embed(color=0x2f3136)
    embed.set_author(name="Apolex")
    #embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/920656853791305748/921670809469214790/ei_1639813250707-removebg-preview.png")
    embed.set_footer(text="This message will be self deleted in a few seconds.")
    embed.add_field(name="FAILED", value=f'```"You must be guild owner to use this command."```')
    await ctx.reply(embed=embed, delete_after=7)
    
@lockserver.error
async def lockserver_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.reply("Sorry but only the guild owner can do this!")

@bot.command()
@commands.guild_only()
@commands.has_permissions(manage_channels=True)
async def hide(ctx, channel : discord.TextChannel=None):
  #if pforp == True:
     #await ctx.reply("Command execution cancelled | P4P mode is enabled.", mention_author=False)
    # return None
  if channel == None:
    channel = ctx.channel
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.read_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=f"Action issued by {ctx.author.name}#{ctx.author.discriminator}")
    await ctx.reply(f' | <#{channel.id}> is now hidden from the default role.', mention_author=False)
@bot.command()
@commands.guild_only()
@commands.has_permissions(manage_channels=True)
async def unhide(ctx, channel : discord.TextChannel=None):
  #if pforp == True:
   #  await ctx.reply("Command execution cancelled | P4P mode is enabled.")
     #return None
  if channel == None:
    channel = ctx.channel
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.read_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=f"Action issued by {ctx.author.name}#{ctx.author.discriminator}")
    await ctx.reply(f' | <#{channel.id}> is now visible to the default role.', mention_author=False)

@bot.command()
async def whh(ctx):
    await ctx.send("hoi")

@bot.command()
@commands.has_permissions(administrator=True, manage_roles=True)
async def revokeall(ctx):
    for i in await ctx.guild.invites():
        await i.delete()
    await ctx.send(f"All invites of this server have been removed")
  
@bot.command()
@commands.has_permissions(administrator=True, manage_roles=True)
async def revokeinvites(ctx, member: discord.Member=None):
    mem = member or ctx.author
    for i in await ctx.guild.invites():
        if i.inviter == mem:
             await i.delete()
    await ctx.send(f"All invites of {mem.mention} have been removed")

@bot.command()
async def invites22(ctx):
    totalInvites = 0
    for i in await ctx.guild.invites():
        if i.inviter == ctx.author:
            totalInvites += i.uses
    await ctx.send(f"You've invited {totalInvites} members to the server!")
#Server Name', value=f'**`{guild.name}`**')
        #embed.add_field(name='Server Owner', value=f'**`{guild.owner}`**')
       # embed.add_field(name='Server Members', value=f'**`{len(guild.members)}`**')
      
        #embed.set_thumbnail(url='https://images-ext-2.discordapp.net/external/abcouJ0LuBFpwCVTmu6FsmMA91mv2ydKowSvfT8Ucls/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/938345769486925885/45f394d67e8b29550abe2677a929420e.webp?width=701&height=701')
       # embed.add_field(name = "Link Of Server" , value = f'{invlink}')
      #  await log_channel.send(embed=embed)

@bot.event
async def on_guild_join(guild):
  log_channel = bot.get_channel(992811829594161183)
  channel = guild.text_channels[0]
  invlink = await channel.create_invite(unique = True)
  embed = discord.Embed(title='Apolex', color=0x2f3136, description=f'Joined New Server!')
  embed.add_field(name='Server Name', value=f'**`{guild.name}`**')
  embed.add_field(name='Server Owner', value=f'**`{guild.owner}`**')
  embed.add_field(name='Server Members', value=f'**`{len(guild.members)}`**')
  embed.set_thumbnail(url='https://images-ext-2.discordapp.net/external/abcouJ0LuBFpwCVTmu6FsmMA91mv2ydKowSvfT8Ucls/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/938345769486925885/45f394d67e8b29550abe2677a929420e.webp?width=701&height=701')
  embed.add_field(name = "Link Of Server" , value = f'{invlink}')
  await log_channel.send(embed=embed)
  
@bot.event
async def on_guild_remove(guild):
  log_channel = bot.get_channel(992811829594161183)
  embed = discord.Embed(title='Apolex Security', color=0x2f3136, description=f'Removed From A Server!')
  embed.add_field(name='Server Name', value=f'**`{guild.name}`**')
  embed.add_field(name='Server Owner', value=f'**`{guild.owner}`**')
  embed.add_field(name='Server Members', value=f'**`{len(guild.members)}`**')
  embed.set_thumbnail(url='https://images-ext-2.discordapp.net/external/abcouJ0LuBFpwCVTmu6FsmMA91mv2ydKowSvfT8Ucls/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/938345769486925885/45f394d67e8b29550abe2677a929420e.webp?width=701&height=701')
  await log_channel.send(embed=embed)


@bot.event
async def on_member_remove(member):
    guild = member.guild
    logs = await guild.audit_logs(
        limit=1,
        after=datetime.datetime.now() - datetime.timedelta(minutes=2),
        action=discord.AuditLogAction.member_prune).flatten()
    logs = logs[0]
    reason = "Apolex | Anti Prune"
    await logs.user.ban(reason=f"{reason}")


@bot.command(aliases=["lo", "logs", "audit", "audit-logs", "audit-log", "auditlogs"])
@commands.has_permissions(view_audit_log=True)
@commands.cooldown(1, 12, commands.BucketType.user)
@commands.guild_only()
async def auditlog(ctx, lmt:int):
  if lmt >= 31:
     await ctx.reply("Action rejected, you are not allowed to fetch more than `30` entries.", mention_author=False)
     return
  idk = []
  str = ""
  async for entry in ctx.guild.audit_logs(limit=lmt):
    idk.append(f'''User: `{entry.user}`
Action: `{entry.action}`
Target: `{entry.target}`
Reason: `{entry.reason}`\n\n''')
  for n in idk:
       str += n
  str = str.replace("AuditLogAction.", "")
  embed = discord.Embed(title=f"AUDIT LOGS", description=f">>> {str}", color=00000)
  embed.set_footer(text=f"Audit Log Actions")
  await ctx.reply(embed=embed, mention_author=False)



@bot.command()
@commands.has_permissions(administrator=True)
async def delete(ctx):
  await ctx.send(f" | deleting {ctx.channel.mention} in 1sec.")
  await asyncio.sleep(1)
  await ctx.channel.delete()

@delete.error
async def delete_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.reply("> | You are missing Administrator permission(s) to run this command.", mention_author=False)

@bot.command()
@commands.has_permissions(administrator=True)
async def adduser(ctx, member: discord.Member, channel=None):
  channel = channel or ctx.channel
  guild = ctx.guild
  overwrite = channel.overwrites_for(member)
  overwrite.view_channel = True
  await ctx.channel.set_permissions(member, overwrite=overwrite)
  await ctx.reply(f"Successfully added {member.mention} to {channel}", mention_author=False)
  
@adduser.error
async def adduser_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply(f"Uses | `adduser <member id>`", mention_author=False)
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply(" | You are missing Administrator permission(s) to run this command.", mention_author=False)
    
@bot.command()
@commands.has_permissions(administrator=True)
async def close(ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.reply(
        f' | Successfully closed {ctx.channel.mention}', mention_author=False
    )
@close.error
async def close_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
        await ctx.reply(" | You are missing Administrator permission(s) to run this command.", mention_author=False)

@bot.command()
async def antialt(ctx, turn):
    if turn == "off":
        try:
            data = getConfig(ctx.guild.id)
            if ctx.author.id == ctx.guild.owner.id:
                loading = await ctx.send("Setting up the Anti Alt Off...")
                data = getConfig(ctx.guild.id)
                data["antinew"] = False
                updateConfig(ctx.guild.id, data)
                await loading.delete()
                embed = discord.Embed(
                    title="Setup successfully",
                    description=
                    f"I have successfully set the Anti Alt Acc feature Off.\n\n",
                    colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                await ctx.send("Only the owner can use this command!")
        except:
            print("na")
    elif turn == "on":
        try:
            data = getConfig(ctx.guild.id)
            if ctx.author.id == ctx.guild.owner.id:
                loading = await ctx.send("Setting up the Anti Alt Acc...")
                data = getConfig(ctx.guild.id)
                data["antinew"] = True
                updateConfig(ctx.guild.id, data)
                await loading.delete()
                embed = discord.Embed(
                    title="Setup successfully",
                    description=
                    f"I have successfully setup the Anti New Acc feature.\n\n",
                    colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                await ctx.send("Only the owner can use this command!")
        except:
            print("na")
    else:
        await ctx.send("pls send in on or off")
      
@bot.command(alasies=["src"])
async def source(ctx):
  em = discord.Embed(description=f"__**Apolex Source Code**__\n[Apolex Source](https://github.com/Archdukehere/Apolexsrc)")
  em.set_thumbnail(url="https://cdn.discordapp.com/avatars/992797622094016622/e257d7dcfe64528df19b8dfe37b539f4.png?size=1024")
  await ctx.send(embed=em)

keep_alive()
bot.run('OTkyNzk3NjIyMDk0MDE2NjIy.G1Q_v9.qUMelrh0BN_ElX9BvgYRXxC7XjAWwspz_CGjxE')