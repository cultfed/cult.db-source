from re import A
import discord, json, time, requests, telnyx
from interactions import Permissions
from discord.ext import commands
import sqlite3, os
from tarfile import RECORDSIZE

connection = sqlite3.connect("DB/DiscordDB.db")
connection2 = sqlite3.connect("DB/8chan.db")
connection3 = sqlite3.connect("DB/Gettr.db")
connection4 = sqlite3.connect("DB/doxbin.db")
connection5 = sqlite3.connect("DB/weleakinfo.db")
connection6 = sqlite3.connect("DB/usemails.db")
cursor = connection.cursor()
cursor2 = connection2.cursor()
cursor3 = connection3.cursor()
cursor4 = connection4.cursor()
cursor5 = connection5.cursor()
cursor6 = connection6.cursor()


client = commands.Bot(',', self_bot = False)
with open('config/config.json') as z:
    config = json.load(z)
    apikey = config.get('apikey')
    token = config.get('token')


client.remove_command('help')


@client.command()
async def help(ctx, category=None):
    if category is None:

        await ctx.send('''```
 ╔═╗╦ ╦╦ ╔╦╗╔╦╗╔╗      
 ║  ║ ║║  ║  ║║╠╩╗
 ╚═╝╚═╝╩═╝╩o═╩╝╚═╝    180,291 Records         t.me/cultfed
 ──────────────────────────────────────────────────────────┐
    discord    (60)          eightchan   (15k)             │
    gettr      (90k)         doxbin  (4k)                  │
    weleakinfo  (23k)        usa (48k)                     │
    other                                                  │
                                                           │
───────────────────────────────────────────────────────────┘```''')
    elif str(category).lower() == "discord":
        await ctx.send('''```
 ╔═╗╦ ╦╦ ╔╦╗╔╦╗╔╗ 
 ║  ║ ║║  ║  ║║╠╩╗
 ╚═╝╚═╝╩═╝╩o═╩╝╚═╝          Discord           t.me/cultfed
──────────────────────────────────────────────────────────┐
 ,discordid                  ,discordemail                │
 ,discordnumber              ,discordip                   │
 ,discordtoken               ,discorduser                 │
                                                          │
                                                          │
──────────────────────────────────────────────────────────┘
```''')
    elif str(category).lower() == "gettr":
        
        await ctx.send('''```       
╔═╗╦ ╦╦ ╔╦╗╔╦╗╔╗ 
║  ║ ║║  ║  ║║╠╩╗
╚═╝╚═╝╩═╝╩o═╩╝╚═╝     Gettr                 t.me/cultfed
──────────────────────────────────────────────────────────┐
 ,gettruser            ,gettremail                        │
                                                          │
                                                          │
                                                          │
                                                          │
──────────────────────────────────────────────────────────┘ ```''')
    elif str(category).lower() == "weleakinfo":
        await ctx.send('''```
        
╔═╗╦ ╦╦ ╔╦╗╔╦╗╔╗ 
║  ║ ║║  ║  ║║╠╩╗
╚═╝╚═╝╩═╝╩o═╩╝╚═╝    Weleakinfo      t.me/cultfed
──────────────────────────────────────────────────────────┐
 ,weleakemail        ,weleakname                          │
                                                          │
                                                          │
                                                          │
                                                          │
──────────────────────────────────────────────────────────┘```''')
    elif str(category).lower() == "eightchan":
        await ctx.send('''```    
╔═╗╦ ╦╦ ╔╦╗╔╦╗╔╗ 
║  ║ ║║  ║  ║║╠╩╗
╚═╝╚═╝╩═╝╩o═╩╝╚═╝        8chan              t.me/cultfed
──────────────────────────────────────────────────────────┐
 ,eigthchanemail       ,eightchanuser                     │
                                                          │
                                                          │
                                                          │
                                                          │
──────────────────────────────────────────────────────────┘
        ```''')
    elif str(category).lower() == "doxbin":
        await ctx.send('''```
        
╔═╗╦ ╦╦ ╔╦╗╔╦╗╔╗ 
║  ║ ║║  ║  ║║╠╩╗
╚═╝╚═╝╩═╝╩o═╩╝╚═╝        Doxbin              t.me/cultfed
──────────────────────────────────────────────────────────┐
 ,doxbinuser           ,doxbinpw                          │
                                                          │
                                                          │
                                                          │
                                                          │
──────────────────────────────────────────────────────────```''')
    elif str(category).lower() == "usa":
        await ctx.send('''```
╔═╗╦ ╦╦ ╔╦╗╔╦╗╔╗ 
║  ║ ║║  ║  ║║╠╩╗
╚═╝╚═╝╩═╝╩o═╩╝╚═╝        USA             t.me/cultfed
──────────────────────────────────────────────────────────┐
 ,usaemail                                                │
                                                          │
                                                          │
                                                          │
                                                          │
──────────────────────────────────────────────────────────┘```''')
    elif str(category).lower() ==  "other":
        await ctx.send('''```
        
╔═╗╦ ╦╦ ╔╦╗╔╦╗╔╗ 
║  ║ ║║  ║  ║║╠╩╗
╚═╝╚═╝╩═╝╩o═╩╝╚═╝        Other              t.me/cultfed
──────────────────────────────────────────────────────────┐
 ,ip                     ,email                           │
 ,number                                                  │
                                                          │
 ,instgram                                                │
                                                          │
──────────────────────────────────────────────────────────┘```''')


@client.command()
async def usaemail(ctx, query):
    if "cultbase" not in ctx.message.channel.name:
         await ctx.send('`This only works in #cultbase, ",setup" to setup the bot`')
         return
    cursor6.execute(f"SELECT * FROM usemails WHERE trim(field1) LIKE '{query}';")
    results = cursor6.fetchall()
    for r in results:
      await ctx.send(f"""```  
Username: {r[0]}
Password: {r[1]}
```""")

@client.command()
async def number(ctx, query):
    if "cultbase" not in ctx.message.channel.name:
         await ctx.send('`This only works in #cultbase, ",setup" to setup the bot`')
         return
    api2 = f"https://api.telnyx.com/v2/number_lookup/{query}"
    telnyx.api_key = f"{apikey}"
    telnyx.NumberLookup.retrieve(f"{query}")
    headers = {f"Authorization": f"Bearer {apikey}"}
    numberreturn = requests.get(api2, headers=headers)
    await ctx.send(f"```{numberreturn.text}```")
    print(numberreturn.status_code)

@client.command()
async def ip(ctx, query):
    if "cultbase" not in ctx.message.channel.name:
         await ctx.send('`This only works in #cultbase, ",setup" to setup the bot`')
         return
    api3 = f"https://ipapi.co/{query}/json/"
    ipreturn = requests.get(api3)
    await ctx.send(f"```{ipreturn.text}```")

@client.command()
async def email(ctx, emailsearch):
    if "cultbase" not in ctx.message.channel.name:
         await ctx.send('`This only works in #cultbase, ",setup" to setup the bot`')
         return
    api = f"https://emailrep.io/{emailsearch}"
    headers = {"Accept": "application/json"}
    returnn = requests.get(api, headers=headers)
    await ctx.send(f"```{returnn.text}```")
    print(returnn.status_code)@client.command()

@client.command()
async def doxbinuser(ctx, query):
    if "cultbase" not in ctx.message.channel.name:
         await ctx.send('`This only works in #cultbase, ",setup" to setup the bot`')
         return
    cursor4.execute(f"SELECT * FROM doxbin WHERE trim(field1) LIKE '{query}';")
    results = cursor4.fetchall()
    for r in results:
      await ctx.send(f"""```    
Username: {r[0]}
Password: {r[1]}
```""")
@client.command()
async def doxbinpw(ctx, query):
    if "cultbase" not in ctx.message.channel.name:
         await ctx.send('`This only works in #cultbase, ",setup" to setup the bot`')
         return
    cursor2.execute(f"SELECT * FROM doxbin WHERE trim(field2) LIKE '{query}';")
    results = cursor2.fetchall()
    for r in results:
      await ctx.send(f"""```    
Username: {r[0]}
Password: {r[1]}
```""")
################
@client.command()
async def eightchanemail(ctx, query):
    if "cultbase" not in ctx.message.channel.name:
         await ctx.send('`This only works in #cultbase, ",setup" to setup the bot`')
         return
    cursor2.execute(f"SELECT * FROM eightchan WHERE trim(field7) LIKE '{query}';")
    results = cursor2.fetchall()
    for r in results:
      await ctx.send(f"""```    
ID: {r[0]}
Username: {r[1]}
Hash:  {r[2]}
Salt:  {r[3]}
Type:  {r[4]}
Boards:  {r[5]}
Email: {r[6]}
```""")
@client.command()
async def eightchanuser(ctx, query):
    if "cultbase" not in ctx.message.channel.name:
         await ctx.send('`This only works in #cultbase, ",setup" to setup the bot`')
         return
    cursor2.execute(f"SELECT * FROM eightchan WHERE trim(field2) LIKE '{query}';")
    results = cursor2.fetchall()
    for r in results:
      await ctx.send(f"""```    
ID: {r[0]}
Username: {r[1]}
Hash:  {r[2]}
Salt:  {r[3]}
Type:  {r[4]}
Boards:  {r[5]}
Email: {r[6]}
```""")
##########################
@client.command()
async def weleakemail(ctx, query):
    if "cultbase" not in ctx.message.channel.name:
         await ctx.send('`This only works in #cultbase, ",setup" to setup the bot`')
         return
    cursor5.execute(f"SELECT * FROM customers WHERE trim(field3) LIKE '{query}';")
    results = cursor5.fetchall()
    for r in results:
      await ctx.send(f"""```    
ID: {r[0]}
Email: {r[2]}
Name:  {r[3]}
Date Created:  {r[4]}
Card Brand:  {r[8]}
Card Exp Month:  {r[10]}
Card Exp Year: {r[11]}
Card Name: {r[12]}
Card Last 4: {r[7]}
User ID: {r[31]}
```""")
@client.command()
async def weleakname(ctx, query):
    if "cultbase" not in ctx.message.channel.name:
         await ctx.send('`This only works in #cultbase, ",setup" to setup the bot`')
         return
    cursor5.execute(f"SELECT * FROM customers WHERE trim(field4) LIKE '{query}';")
    results = cursor5.fetchall()
    for r in results:
      await ctx.send(f"""```    
ID: {r[0]}
Email: {r[2]}
Name:  {r[3]}
Date Created:  {r[4]}
Card Brand:  {r[8]}
Card Exp Month:  {r[10]}
Card Exp Year: {r[11]}
Card Name: {r[12]}
Card Last 4: {r[7]}
User ID: {r[31]}
```""")


################
@client.command()
async def gettruser(ctx, query):
    if "cultbase" not in ctx.message.channel.name:
         await ctx.send('`This only works in #cultbase, ",setup" to setup the bot`')
         return
    cursor3.execute(f"SELECT * FROM gettr WHERE trim(field4) LIKE '{query}';")
    results = cursor3.fetchall()
    for r in results:
     await ctx.send(f"""```
User ID: {r[0]}
Username: {r[5]}
Birth Year: {r[7]}
Location: {r[15]}
Language: {r[12]}
Email: {r[4]}
```""")
@client.command()
async def gettremail(ctx, query):
    if "cultbase" not in ctx.message.channel.name:
         await ctx.send('`This only works in #cultbase, ",setup" to setup the bot`')
         return
    cursor3.execute(f"SELECT * FROM gettr WHERE trim(field5) LIKE '{query}';")
    results = cursor3.fetchall()
    for r in results:
     await ctx.send(f"""```
User ID: {r[0]}
Username: {r[5]}
Birth Year: {r[7]}
Location: {r[15]}
Language: {r[12]}
Email: {r[4]}
```""")
######################

################
@client.command()
async def discordemail(ctx, query):
    if "cultbase" not in ctx.message.channel.name:
         await ctx.send('`This only works in #cultbase, ",setup" to setup the bot`')
         return
    cursor.execute(f"SELECT * FROM info WHERE trim(Email) LIKE '{query}';")
    results = cursor.fetchall()
    for r in results:
     await ctx.send(f"""```
User ID: {r[0]}
Email: {r[1]}
Number: {r[2]}
IP: {r[3]}
Token: {r[4]}
Username: {r[5]}
```""")

@client.command()
async def discordip(ctx, query):
    if "cultbase" not in ctx.message.channel.name:
         await ctx.send('`This only works in #cultbase, ",setup" to setup the bot`')
         return
    cursor.execute(f"SELECT * FROM info WHERE trim(IP) LIKE '{query}';")
    results = cursor.fetchall()
    for r in results:
     await ctx.send(f"""```
User ID: {r[0]}
Email: {r[1]}
Number: {r[2]}
IP: {r[3]}
Token: {r[4]}
Username: {r[5]}
```""")
@client.command()
async def discorduser(ctx, query):
    if "cultbase" not in ctx.message.channel.name:
         await ctx.send('`This only works in #cultbase, ",setup" to setup the bot`')
         return
    cursor.execute(f"SELECT * FROM info WHERE trim(Username) LIKE '{query}';")
    results = cursor.fetchall()
    for r in results:
     await ctx.send(f"""```
User ID: {r[0]}
Email: {r[1]}
Number: {r[2]}
IP: {r[3]}
Token: {r[4]}
Username: {r[5]}
```""")
@client.command()
async def discordtoken(ctx, query):
    if "cultbase" not in ctx.message.channel.name:
         await ctx.send('`This only works in #cultbase, ",setup" to setup the bot`')
         return
    cursor.execute(f"SELECT * FROM info WHERE trim(Token) LIKE '{query}';")
    results = cursor.fetchall()
    for r in results:
     await ctx.send(f"""```
User ID: {r[0]}
Email: {r[1]}
Number: {r[2]}
IP: {r[3]}
Token: {r[4]}
Username: {r[5]}
```""")
@client.command()
async def discordnumber(ctx, query):
    if "cultbase" not in ctx.message.channel.name:
         await ctx.send('`This only works in #cultbase, ",setup" to setup the bot`')
         return
    cursor.execute(f"SELECT * FROM info WHERE trim(Number) LIKE '{query}';")
    results = cursor.fetchall()
    for r in results:
     await ctx.send(f"""```
User ID: {r[0]}
Email: {r[1]}
Number: {r[2]}
IP: {r[3]}
Token: {r[4]}
Username: {r[5]}
```""")
@client.command()
async def discordid(ctx, query):
    if "cultbase" not in ctx.message.channel.name:
         await ctx.send('`This only works in #cultbase, ",setup" to setup the bot`')
         return
    cursor.execute(f"SELECT * FROM info WHERE trim(UserID) LIKE '{query}';")
    results = cursor.fetchall()
    for r in results:
     await ctx.send(f"""```
User ID: {r[0]}
Email: {r[1]}
Number: {r[2]}
IP: {r[3]}
Token: {r[4]}
Username: {r[5]}
```""")
#################################
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="cultbase lookups", url="https://www.twitch.tv/fazesway"))
    print(f"{client.user} Has Connected Succesfully, Enjoy Searching!")

@client.command()
@commands.has_permissions(administrator=True)
async def purge(ctx, amount : int):
    await ctx.channel.purge(limit=amount + 1)

@client.command()
@commands.has_permissions(ban_members=True)
async def channuke(ctx):
    await ctx.channel.send(f"Successfully nuked #{ctx.channel.name}")
    await ctx.channel.delete(reason="nuke")
    await ctx.channel.clone(reason="nuke")
@client.command()
async def ping(ctx):
     await ctx.send(f'`{round(client.latency * 1000)}ms`')

@client.command()
@commands.has_permissions(administrator=True)
async def setup(ctx):
    
    perms = discord.Permissions(send_messages=True, read_messages=True)
    guild = ctx.guild
    await ctx.send("`Setting up Cultbase`")
    await guild.create_role(name="cultbase access", permissions=perms)
    await guild.create_text_channel("cultbase")

@client.command()
@commands.has_permissions(administrator=True)
async def perms(ctx):
     if "cultbase" not in ctx.message.channel.name:
         await ctx.send('`This only works in #cultbase, ",setup" to setup the bot`')
         return

     await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
     await ctx.send("`Updated Perms`")

@client.command()
async def instagram(ctx, query):
    await ctx.send(f"https://www.instagram.com/{query}/")
    
client.run(token, bot=True)
