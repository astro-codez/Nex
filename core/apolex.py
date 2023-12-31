import discord
#import aiohttp
from discord.ext import commands
#from aiohttp import ClientSession
import json
import os
#os.system("pip install dismusic")
#import dismusic
import pymongo
os.system("pip install git+https://github.com/Pycord-Development/pycord")
os.system("pip install pymongo[srv]")
from cogs.ticket import createTicket, closeTicket
# ------------------------------ PREFIX AND INTENTS  -----------------------------------------

#OWNERS_IDS2 = [979967089542569994, 973137921999765515, 950272973032525824, 9905445987701649460, 905396101274828821]
OWNER_IDS = [973137921999765515, 950272973032525824]
intents = discord.Intents.all()

# ------------------------------ DATABASE  -----------------------------------------
client = pymongo.MongoClient("mongodb+srv://hacker:chetan2004@cluster0.rxh8r.mongodb.net/Flame?retryWrites=true&w=majority")
db = client.get_database("Flame").get_collection("servers")

# ------------------------------ CODE  -----------------------------------------
class apolex(commands.AutoShardedBot):
  def __init__(self) -> None:
    super().__init__(command_prefix=get_prefix, intents=intents, owner_ids=OWNER_IDS)
    self.persistent_views_added = False

    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            self.load_extension(f'cogs.{filename[:-3]}')
    
  def run(self, version):
      self.VERSION = version
      with open('./ext/config.json') as f:
        self.config = json.load(f)
      super().run(self.config['token'], reconnect=True)

  async def on_ready(self) -> None:
    if not self.persistent_views_added:
        self.add_view(createTicket())
        self.add_view(closeTicket())
        self.persistent_views_added = True
    print(f'╭────˚♪°𝄞°♪˚─────╮\n{self.user.name} is online.\n╰────˚♪°𝄞°♪˚─────╯')
    await self.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=f"!help"))
    self.bot = bot
#client.lavalink_nodes = [
#
  #  {
    #    'host': 'lava.link',
     ##   'port': 80,
   #     'password': 'dismusic'
   # }

#]
##client.load_extension('dismusic')
# If you want to use spotify search
    #bot.spotify_credentials = {
    #'client_id': '6ad677e7f4344a9ebd7958e3d6fa3e56',
    #'client_secret': '6405a1b768e841ca8a6cf542b8f24f1d'
#}

    
  #async def add_owner(self, user: discord.Member):
    #OWNER_IDS.append(user)
    #await user.send('<a:Ag_heedmode:958710180495908884> | You have been approved as the Co-Owner of Apolex')

  
#async def get_prefix(bot, message):
   # with open('prefixes.json', 'r') as f:
       # prefixes = json.load(f)
   # return "!"
   # return prefixes[str(message.guild.id)]
#def get_prefix(bot, message):
   #   with open ('nopre.json', 'r') as f:
      #  data = json.load(f)
       # data = data['users']
      #  if str(message.author.id) in data or message.author.id in data:
        #    return ''
      #  else:
         #   return '!'


####async def get_prefix(bot, message):
   # if message.author.id in OWNER_IDS:
     # return ""
   # else:
     # return "!"
default_prefix = "!"

def get_prefix(client, message):
  with open("prefixes.json", "r") as f:
    idk = json.load(f)
  with open ('nopre.json', 'r') as f:
    data = json.load(f)
    data = data['users']
    if str(message.author.id) in data or message.author.id in data:
      return ''
    elif str(message.guild.id) not in idk:
       return f"{default_prefix}"
    elif str(message.guild.id) in idk:
       idkprefix = idk[str(message.guild.id)]
       return f"{idkprefix}"


bot = commands.Bot(
  command_prefix = get_prefix,
  intents=intents,
)      
bot = apolex()
