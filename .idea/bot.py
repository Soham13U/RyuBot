import asyncio

import discord
from discord.ext import commands,tasks
import mal
from mal import AnimeSearch
from mal import Anime
from mal import MangaSearch
from bs4 import BeautifulSoup
import requests
from itertools import cycle




client=commands.Bot(command_prefix=">")
status=cycle(['oWo','uWu'])
client.remove_command('help')






@client.event
async def on_ready():
    change_status.start()
    print("Bot is ready")

@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandNotFound):
        await ctx.send("Invalid command used")
        embed=discord.Embed(
            colour=discord.Colour.green()
        )
        embed.set_image(url='https://media.tenor.com/images/59ae6e3415612f1429fb6bc5cec806da/tenor.gif')
        await ctx.send(embed=embed)



@tasks.loop(seconds=1)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))



@client.command()
async def hello(ctx):
    await ctx.send("Yoooo!!")
#----------------------------------------------ANIME SEARCH-------------------------------------------------------------------
@client.command()
async def ansearch(ctx):
    embed=discord.Embed(
        title='Which anime do you want to search?',
        description="Timeout in 10 seconds",
        colour=discord.Colour.green()

    )
    await ctx.send(embed=embed)
    def check(m):
        return m.author.id==ctx.author.id
    message=await client.wait_for('message',timeout=10,check=check)

    an=message.content
    search = AnimeSearch(an)

    for i in range(0,10):
        await ctx.send(str(i+1)+"."+search.results[i].title)





#----------------------------------------------MANGA SEARCH-------------------------------------------------------------------
@client.command()
async def masearch(ctx):
    embed=discord.Embed(
        title='Which manga do you want to search?',
        description="Timeout in 10 seconds",
        colour=discord.Colour.green()

    )
    await ctx.send(embed=embed)
    def check(m):
        return m.author.id==ctx.author.id
    message=await client.wait_for('message',timeout=10,check=check)

    ma=message.content
    search = MangaSearch(ma)

    for i in range(0,10):
        await ctx.send(str(i+1)+"."+search.results[i].title)

#----------------------------------------------USER SEARCH-------------------------------------------------------------------
@client.command()
async def usearch(ctx):
    embed=discord.Embed(
        title='Which user do you want to search?',
        description="Timeout in 10 seconds",
        colour=discord.Colour.green()

    )
    await ctx.send(embed=embed)
    def check(m):
        return m.author.id==ctx.author.id
    message=await client.wait_for('message',timeout=10,check=check)
    uname=message.content
    source=requests.get("https://myanimelist.net/profile/"+uname).text
    soup=BeautifulSoup(source,'lxml')

    images=soup.find_all("img")
    i=0
    for image in images:
         if i == 2:
            break
         else:
            href=image.get('data-src')

         i=i+1




    t1=soup.find('title').text
    t2=soup.find('div',class_='stat-score di-t w100 pt8').text
    embed=discord.Embed(
        title=t1,url="https://myanimelist.net/profile/"+uname,
        description=t2,
        colour=discord.Colour.green()

    )
    embed.set_thumbnail(url=href)



    await ctx.send(embed=embed)

    #await ctx.send(t1)


     #  await ctx.send(t2)

  #  await ctx.send("-------------------")

    p=0
    for t4 in soup.find_all('li',class_='clearfix mb12'):

        heading=t4.a.text+": "
        value=t4.span.text
        final=heading+value
        if p==0:
            watching1=heading
            watching2=value

        if p==1:
            completed1=heading
            completed2=value

        if p==2:
            hold1=heading
            hold2=value
        if p==3:
            drop1=heading
            drop2=value
        if p==4:
            ptw1=heading
            ptw2=value

        if p==4:
            embed1=discord.Embed(
                title='Anime Stats: ',
                colour=discord.Colour.green()
            )
            embed1.add_field(name=watching1,value=watching2,inline=False)
            embed1.add_field(name=completed1,value=completed2,inline=False)
            embed1.add_field(name=hold1,value=hold2,inline=False)
            embed1.add_field(name=drop1,value=drop2,inline=False)
            embed1.add_field(name=ptw1,value=ptw2,inline=False)
            await ctx.send(embed=embed1)
        p=p+1

#----------------------------------------------ACTIONS-------------------------------------------------------------------
@client.command()
async def smirk(ctx):
    embed=discord.Embed(
        colour=discord.Colour.green()
            )
    embed.set_image(url='https://media.tenor.com/images/0a2540a372f9320d454c20761fb13d6e/tenor.gif')
    await ctx.send(embed=embed)

@client.command()
async def smile(ctx):
    embed=discord.Embed(
        colour=discord.Colour.green()
    )
    embed.set_image(url='https://media4.giphy.com/media/ree8xCap5nHi/200.gif')
    await ctx.send(embed=embed)

@client.command()
async def pout(ctx):
    embed=discord.Embed(
        colour=discord.Colour.green()
    )
    embed.set_image(url='https://i.pinimg.com/originals/e5/6e/1a/e56e1ae197ea11668756e6e82407e5c5.gif')
    await ctx.send(embed=embed)

@client.command()
async def laugh(ctx):
    embed=discord.Embed(
        colour=discord.Colour.green()
    )
    embed.set_image(url='https://i.pinimg.com/originals/1b/4a/4d/1b4a4d70324db4ebb5849dd67d1d6414.gif')
    await ctx.send(embed=embed)

@client.command()
async def cry(ctx):
    embed=discord.Embed(
        colour=discord.Colour.green()
    )
    embed.set_image(url='https://media1.tenor.com/images/ce52606293142a2bd11cda1d3f0dc12c/tenor.gif?itemid=5184314')
    await ctx.send(embed=embed)

@client.command()
async def bruh(ctx):
    embed=discord.Embed(
        colour=discord.Colour.green()
    )
    embed.set_image(url='https://i.kym-cdn.com/photos/images/original/002/031/703/b68.gif')
    await ctx.send(embed=embed)

@client.command()
async def confused(ctx):
    embed=discord.Embed(
        colour=discord.Colour.green()
    )
    embed.set_image(url='https://i.gifer.com/C4iE.gif')
    await ctx.send(embed=embed)
#----------------------------------------------ABOUT-------------------------------------------------------------------
@client.command()
async def about(ctx):
    embed=discord.Embed(
        title='Konnichiwa!!',
        description='I am RyuBot, you can call me Ryu-chan uWu.I am a user friendly bot who can do a lot of cool and fun stuff. To know what all things I can do, type >help. If you want me to learn new things, contact my creator - Xoham(aka Ryujin) uWu ',
        colour=discord.Colour.green()
    )
    message=await ctx.send(embed=embed)
    await message.add_reaction('🤝')

#----------------------------------------------HELP-------------------------------------------------------------------



@client.group(invoke_without_command=True)
async def help(ctx):
    embed=discord.Embed(
        title='Help',
        description='Use >help <command> for extended information on that command',
        colour=discord.Colour.green()
    )
    embed.add_field(name="Search",value="ansearch,masearch,usearch",inline=False)
    embed.add_field(name="About",value="about",inline=False)
    embed.add_field(name="Actions",value="smirk,smile,pout,laugh,cry,bruh,confused",inline=False)

    await ctx.send(embed=embed)


@help.command()
async def ansearch(ctx):
    embed=discord.Embed(
        title='Anime Search',
        description='Shows top 10 matching results',
        colour=discord.Colour.green()
    )
    embed.add_field(name='Syntax',value='>ansearch')
    await ctx.send(embed=embed)

@help.command()
async def masearch(ctx):
    embed=discord.Embed(
        title='Manga Search',
        description='Shows top 10 matching results',
        colour=discord.Colour.green()
    )
    embed.add_field(name='Syntax',value='>masearch')
    await ctx.send(embed=embed)

@help.command()
async def usearch(ctx):
    embed=discord.Embed(
        title='User Search',
        description='Shows stats of matching user',
        colour=discord.Colour.green()
    )
    embed.add_field(name='Syntax',value='>usearch')
    await ctx.send(embed=embed)

@help.command()
async def about(ctx):
    embed=discord.Embed(
        title='About',
        description='All you need to know about me',
        colour=discord.Colour.green()
    )
    embed.add_field(name='Syntax',value='>about')
    await ctx.send(embed=embed)

@help.command()
async def smirk(ctx):
    embed=discord.Embed(
        title='Smirk',

        colour=discord.Colour.green()
    )
    embed.add_field(name='Syntax',value='>smirk')
    await ctx.send(embed=embed)

@help.command()
async def laugh(ctx):
    embed=discord.Embed(
        title='Laugh',

        colour=discord.Colour.green()
    )
    embed.add_field(name='Syntax',value='>laugh')
    await ctx.send(embed=embed)

@help.command()
async def smile(ctx):
    embed=discord.Embed(
        title='Smile',

        colour=discord.Colour.green()
    )
    embed.add_field(name='Syntax',value='>smile')
    await ctx.send(embed=embed)

@help.command()
async def pout(ctx):
    embed=discord.Embed(
        title='Pout',

        colour=discord.Colour.green()
    )
    embed.add_field(name='Syntax',value='>pout')
    await ctx.send(embed=embed)

@help.command()
async def cry(ctx):
    embed=discord.Embed(
        title='Cry',

        colour=discord.Colour.green()
    )
    embed.add_field(name='Syntax',value='>cry')
    await ctx.send(embed=embed)

@help.command()
async def bruh(ctx):
    embed=discord.Embed(
        title='Bruh',

        colour=discord.Colour.green()
    )
    embed.add_field(name='Syntax',value='>bruh')
    await ctx.send(embed=embed)

@help.command()
async def confused(ctx):
    embed=discord.Embed(
        title='Confused',

        colour=discord.Colour.green()
    )
    embed.add_field(name='Syntax',value='>confused')
    await ctx.send(embed=embed)









client.run("ODQ4NDQ4OTIzMzk1OTQ4NTc1.YLMxog.HmG0igx3J4Ib5Sn0kBUDIfYR4xE")