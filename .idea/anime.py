from bs4 import BeautifulSoup
import requests

uname=input("Enter username:")
source=requests.get("https://myanimelist.net/profile/"+uname).text
soup=BeautifulSoup(source,'lxml')
#print(soup.prettify())

t1=soup.find('title').text
print(t1)

t2=soup.find('div',class_='stat-score di-t w100 pt8').text
print(t2)

print("Anime stats: ")
for t4 in soup.find_all('li',class_='clearfix mb12'):

   heading=t4.a.text+" "
   value=t4.span.text
   final=heading+value
   print(final)
   print(type(t4))






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
