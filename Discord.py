import asyncio
from discord import Game
from discord.ext.commands import Bot
import Pics
import project_ids


BOT_PREFIX = ("?", "!")
TOKEN =  project_ids.discord_token() # Get at discordapp.com/developers/applications/me

client = Bot(command_prefix=BOT_PREFIX)


@client.command(name='pic')
              
async def pics(name):

    await client.say(Pics.pics(name))
   

@client.command(name='gif')
                
async def pics(name):

    await client.say(Pics.gifs(name))
   
  
@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with humans"))
    print("Logged in as " + client.user.name)


@client.command(name='clear',
                pass_context = True)
async def clear(ctx, number):
    mgs = [] #Empty list to put all the messages in the log
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)



async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(TOKEN)
