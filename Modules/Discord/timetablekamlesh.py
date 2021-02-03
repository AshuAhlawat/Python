import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "def ")

@client.event
async def on_ready():
    print("KAMLEEESSHHHHH!!")

@client.event
async def on_member_join(member):
    print(f'{member} kese aaya? Bhakkeee!!')
    
@client.event
async def on_member_remove(member):
    print(f'{member} Nikal Bhosssdiikee')


#FUNCTIONS
@client.command(aliases=['net'])
async def ping(ctx):
    await ctx.send(f'{round(client.latency*1000)}ms')

@client.command(aliases=['today','aajkya'])
async def timetable(ctx):
    from datetime import datetime
    
    x = datetime.now()
    today = int(x.strftime("%w"))
    
    timetable = [
        "AAJ SUTTA!",
        "12 se 1  Maths\n1 se 2  CHE wali bakwas\n3 se 5  practical wala ECE\n4 se 5  HTML Programming",
        "3 se 4  Carpentry++\n4 se 5  Maths",
        "12 se 1  waho Ped podho wala vigyan\n1 se 2  electrician bno\n3 se 4  fake accents",
        "12 se 1  pirated software wala\n1 se 2  Gothic hi sahi tha jisse\n3 se 4  engliss\n4 se 5  Math",
        "1 se 2  EE hi lelete\n3 se 4  padho Vectors tum log\n4 se 5  Code language hi seekh lete",
        "Aaj to lagegi\n9 se 11  CSE practical\n12 se 1  Physics hi kehdo ise\n1 se 2  ECE\n3 se 4  Differen/Integra(tion)\n4 se 5  Ye teacher pedophile hai"
    ]
        
    await ctx.send(f'{timetable[today]}')  

@client.command()
async def toss(ctx, *,ques):
    import random
    choices=['tension na le','are pakka','bilkul','ha','kya pta shayad','na','no chance','are ho hi nahi sakta','nikal bsdk','abee chal']
    await ctx.send(f'{random.choice(choices)}')

@client.command(aliases=["jma","ghata"])
async def add(ctx, *,ques):
    
    if "+" in ques:
        x = ques.split("+")
        y = 0
        for _ in x:
            y = y + int(_)
    else:
        y = "itna padha likha nahi hu mai!"
    if y == 69:
        y = "Nice"
    await ctx.send(f'{y}')

@client.command(aliases=["guna"])
async def multiply(ctx, *,ques):
    
    if "*" in ques:
        x = ques.split("*")
        y = 1
        for _ in x:
            y = y * int(_)
    else:
        y = "itna padha likha nahi hu mai!"
    if y == 69:
        y = "Nice"
    await ctx.send(f'{y}')

@client.command(aliases=["bhag"])
async def divide(ctx, *,ques):
    
    if "/" in ques:
        x = ques.split("/")
        if len(x)>2:
            y = "itna padha likha nahi hu mai!"
        else:
           y = float(x[0])/float(x[1])
    else:
        y = "itna padha likha nahi hu mai!"
    await ctx.send(f'{y}')

@client.command()
async def msg(ctx, *,ques):
    print("Recieved : "+ ques)
    r = input("Send : ")
    
    await ctx.send(f'{r}')
client.run('ODA2MDQyMjUwNTQyMzE3NTg4.YBjrWA.x1dky4jYUvca4qCGHWcwAkvBQq0')