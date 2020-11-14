import discord
import random
import os
from discord.ext import commands

prefix = '/'
client = commands.Bot(command_prefix = prefix)
client.remove_command('help')

bad_words = ['негр', 'Негр', 'нЕгр', 'неГр', 'негР','НЕгр', 'НЕГр', 'НЕГР', 'н е г р', 'Н е г р', 'н Е г р', 'н е Г р',
            'н е г Р', 'Н Е г р', 'Н Е Г Р', 'negr', 'Negr','nEgr', 'neGr', 'negR', 'NEgr', 'NEGr', 'NEGR','n e g r',
            'N e g r', 'n g r', 'n e G r','n e g R', 'N E g r', 'N E G r', 'N E G R', 'neGR', 'nEGR', 'n e G R',
            'nigga', 'Nigga', 'nIgga','niGga', 'nigGa','niggA', 'NIgga', 'NIGga', 'NIGGa', 'NIGGA', 'niGGa', 'nigGA',
            'niGGA', 'nIGGA', 'NiggA','NIggA', 'NIGgA', 'NiGgA', 'nIgGa', 'N I G G A', 'N i g g a', 'n I g g a',
             'n i G g a','n i G g a','n i g G a', 'n i g g A', 'n i g g a', 'N I g g a', 'N I G g a', 'N I G G a',
             'N I G G A', 'n i g G A','n i G G A', 'n I G G A', 'n E G R', 'n E G r', 'пидор', 'Пидор', 'пИдор', 'пиДор',
             'пидОр', 'пидоР', 'ПИдор', 'ПИДор', 'ПИДОр', 'пидр', 'ПИДОР', 'п и д о р', 'П и д о р', 'п И д о р', 'п и Д о р',
             'п и д О р', 'п и д о Р', 'П И д о р','П И Д о р', 'П И Д О р', 'П И Д О Р', 'П и д о Р', 'П и Д о Р',
             'п И д О р', 'Пид0р', 'пидар', 'пыдор', 'пидер', 'пiдор','пидарюга', 'пидорюга', 'пид0рюга', 'пидорюгa',
             'п и д о р ю г а', 'пи д о р ю г а', 'пид о р ю г а', 'пидо р ю г а', 'пидор ю г а', ' пидорю г а',
             'пидорюг а', 'п и д 0 р ю г а', 'пи д 0 р ю г а', 'пид 0 р ю г а', 'пид0 р ю г а', 'пид0р ю г а',
             ' пид0рю г а', 'пид0рюг а', 'ПИДОРЮГА', 'ПИД0РЮГА','пидорасина', 'пидорасин а', 'пидораси н а', 'пидорас и н а',
             'пидора с и н а', 'пидор а с и н а', 'пидо р а с и н а', 'пид о р а с и н а', 'пи д о р а с и н а',
             'п и д о р а с и н а', 'пид0расина','даун', 'д ау н', 'д а у н', 'бондаренко', ]

hello_word = ['Привет', 'привет', 'ПРИВЕТ', 'Ку', 'КУ', 'ky', 'KY', 'Ky', 'здарова', 'Здарова']

# Events

@client.event
async def on_ready():
    activity = discord.Game(name = "/help", type = 3)
    await client.change_presence(status = discord.Status.idle, activity = activity)
    print('bot connected')


@client.event
async def on_message(message):
    msg = message.content.lower()
    await client.process_commands(message)
    for i in bad_words:
        if i in msg:
            await message.delete()
            await message.author.send(f'{message.author.name}, не говори так!!!')
    if msg in hello_word:
        await message.channel.send(f'Привет, {message.author.mention} чтобы увидеть команды пропиши /help.')

#Commands

@client.command()
async def help(ctx):
    emb = discord.Embed(title = 'Commands:')
    emb.add_field(name = '{}mehelp'.format(prefix), value = 'Хелп для участников')
    emb.add_field(name = '{}adhelp'.format(prefix), value = 'Хелп для админов')
    await ctx.send(embed = emb)

@client.command()
async def mehelp(ctx):
    emb = discord.Embed(title = 'Commands:')
    emb.add_field(name = '{}links'.format(prefix), value = 'Ссылки')
    await ctx.send(embed = emb)

@client.command()
@commands.has_permissions(administrator = True)
async def adhelp(ctx):
    emb = discord.Embed(title = 'Commands:')
    emb.add_field(name = '{}clear'.format(prefix), value = 'Удаление чата')
    emb.add_field(name = '{}mute'.format(prefix), value = 'мут пользователя через @')
    emb.add_field(name = '{}unmute'.format(prefix), value = 'анмут пользователя через @')
    await ctx.send(embed = emb)

@adhelp.error
async def adhelp_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed = discord.Embed(description = f':no_entry: Для тебя эта команда запрещенна!'))
	
@client.command()
async def links(ctx):
    emb = discord.Embed(title = 'Ссылки')
    emb.add_field(name = 'VK SH1RONE:', value = 'https://vk.com/sh1r0ne.squad')
    emb.add_field(name = 'VK BlackBird', value = 'https://vk.com/blackbirdservers')	
    emb.add_field(name = 'Twitch', value = 'https://www.twitch.tv/sh1r0ne')
    emb.add_field(name = 'Youtube', value = 'https://www.youtube.com/channel/UCx3eQPR-zzV0OaT6-bg_cTQ')
    await ctx.send(embed = emb)


@client.command()
@commands.has_permissions(administrator = True)
async def clear(ctx, amount: int):
    await ctx.channel.purge( limit = amount )
            
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.mention}, введи сколько удалить сообщений. ')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(embed = discord.Embed(description = f':no_entry: Для тебя эта команда запрещенна!'))

@client.command()
async def bibametr(ctx):
    author = ctx.message.author
    biba = random.randint(1, 30)
    if biba < 15:
        await ctx.send(f'Ну бывает! У {author.mention} биба {biba} см!! ')
    elif biba > 15:
        await ctx.send(f'Вот это я понимаю! У {author.mention} биба {biba} см!! ')

@client.command()
@commands.has_permissions(administrator = True) 
async def mute(ctx, member: discord.Member): 
    await ctx.channel.purge(limit= 1) 
    members_role = discord.utils.get(ctx.message.guild.roles, name= 'Участники') 
    mute_role = discord.utils.get(ctx.message.guild.roles, name = 'Muted') 
    await member.add_roles(mute_role) 
    await member.remove_roles(members_role) 
    await ctx.send(f'У {member.mention} мут за запретное слово!!')

@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed = discord.Embed(description = f':no_entry: Для тебя эта команда запрещенна!'))

@client.command()
@commands.has_permissions(administrator = True) 
async def unmute(ctx, member: discord.Member): 
    await ctx.channel.purge(limit= 1) 
    members_role = discord.utils.get(ctx.message.guild.roles, name= 'Участники') 
    mute_role = discord.utils.get(ctx.message.guild.roles, name = 'Muted') 
    await member.add_roles(members_role) 
    await member.remove_roles(mute_role) 
    await ctx.send(f'{member.mention} был размучен!')

@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed = discord.Embed(description = f':no_entry: Для тебя эта команда запрещенна!'))


token = os.environ.get('BOT_TOKEN')
client.run(token)
