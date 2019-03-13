import discord
from discord.ext import commands
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random

gcreds = input('Google Creds:')

token = input('Bot Token:')

btoken = open(token, "r").read() 


sheeturl = 'https://docs.google.com/spreadsheets/d/1ASX8MIDK594LuW3hxNyVYa3NFSIQyJD3UMQ1jtGsHUo'

#initialize Sheets enviroment
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name(gcreds, scope)
client = gspread.authorize(creds)
sheet = client.open_by_url(sheeturl)
worksheet = sheet.get_worksheet(0)

#initialize Bot enviroment 
description = 'Tragicly organize Tragic'
prefix = '?'
token = btoken

bot = commands.Bot(command_prefix=prefix, description=description)

@bot.event
async def on_ready():
    print('Logged in as {0} {1}'.format(bot.user.id,bot.user.name))
    print('------')

@bot.command(case_insensitive = False, description='Updates your data in the sheet.\nFormat: {0}update Classname Level Nonawk Awk Dp')
async def update(ctx, cname:str, level:float, non: int, awk:int, dp:int):
    initGspread()

    printmessage(ctx.message)

    memid = str(ctx.author)
    member = ctx.message.author.nick

    try:
        x = worksheet.find(memid)
        worksheet.update_cell(x.row,2,member)
        worksheet.update_cell(x.row,3,cname)
        worksheet.update_cell(x.row,4,level)
        worksheet.update_cell(x.row,6,non)
        worksheet.update_cell(x.row,7,awk)
        worksheet.update_cell(x.row,8,dp)

    except:
        row = [memid,member,cname,level,' ',non,awk,dp,False]
        worksheet.append_row(row)
    
    updateGS(memid)
    await ctx.send('Info Updated')


@bot.command(case_insensitive = False, description='Updates your data in the sheet.\nFormat: {0}gear NonAwk Awk Dp')
async def gear(ctx, non: int, awk:int, dp:int):
    initGspread()

    printmessage(ctx.message)

    memid = str(ctx.author)
    member = ctx.message.author.nick

    try:
        x = worksheet.find(memid)
        worksheet.update_cell(x.row,6,non)
        worksheet.update_cell(x.row,7,awk)
        worksheet.update_cell(x.row,8,dp)

    except:
        row = [memid,member,' ', ' ', ' ',non,awk,dp,False]
        worksheet.append_row(row) 

    updateGS(memid)
    await ctx.send('Info Updated')

@bot.command(case_insensitive = False, description='Updates Class in sheet.\nFormat: {0}class Classname'.format(prefix), name='class')
async def c(ctx, name:str):
    initGspread()

    printmessage(ctx.message)

    memid = str(ctx.author)
    member = ctx.message.author.nick

    try:
        x = worksheet.find(memid)
        worksheet.update_cell(x.row,3,name)

    except:
        row = [memid,member,name,' ',' ',' ',' ',False]
        worksheet.append_row(row)

    updateGS(memid)
    await ctx.send('Info Updated')

@bot.command(case_insensitive = False, description='Updates Level in sheet.\nFormat: {0}level Level'.format(prefix), name='level')
async def l(ctx,level):
    initGspread()

    printmessage(ctx.message)

    memid = str(ctx.author)
    member = ctx.message.author.nick
    
    try:
        x = worksheet.find(memid)
        worksheet.update_cell(x.row,4,level)

    except:
        row = [memid,member,' ',level, ' ',' ',' ',' ',False]
        worksheet.append_row(row)

    updateGS(memid)
    await ctx.send('Info Updated')


#Extra Funcs

def updateGS(memid):

    x = worksheet.find(memid)
    a = int(worksheet.cell(x.row,6).value) + int(worksheet.cell(x.row,7).value)
    b = int(worksheet.cell(x.row,8).value)

    res = a/2 + b

    worksheet.update_cell(x.row,5,res)

def printmessage(message):
    print('{0.author}: {0.content}'.format(message))

def initGspread():
    client = gspread.authorize(creds)
    sheet = client.open_by_url(sheeturl)
    worksheet = sheet.get_worksheet(0)


#run bot.
bot.run(token)