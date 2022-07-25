from http import client
from tkinter.messagebox import QUESTION
import discord
from discord import HTTPException
from discord.ext import commands
from cariAnime.searchAnime import animeSearch
import pgr_coop
import importlib
import asyncio
import random
from discord import File
import textwrap
from PIL import Image, ImageFont, ImageDraw
from help import helpMessage
from cariAnime.searchUser import *

#change token
TOKEN = 'TOKEN'

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

def convert(time):
    pos = ['d','m','j','h']

    time_dict = {'d':1,'m':60,'j':3600,'h':3600*24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try: 
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]

@client.command(aliases=['b'])
async def bantuan(ctx):
    await ctx.send(embed=helpMessage())

@client.command()
async def coop(ctx):
    importlib.reload(pgr_coop)
    await ctx.send(f'__**Punishing: Gray Raven - SCAVENGER EVENT**__\nJam Saat Ini: {pgr_coop.timeNow} \nJadwal Pertama {pgr_coop.timeStart1} - {pgr_coop.timeEnd1}: {pgr_coop.result1} \nJadwal Kedua {pgr_coop.timeStart2} - {pgr_coop.timeEnd2}: {pgr_coop.result2}\nJadwal Ketiga {pgr_coop.timeStart3} - {pgr_coop.timeEnd3}: {pgr_coop.result3}')
    return

@client.command()
async def foto(ctx, member: discord.Member=None):
    if member == None:
        member = ctx.author

    icon_url = member.avatar_url
    avatarEmbed = discord.Embed(title = f'Foto profil milik {member.name}', color = 0xFFA500)
    avatarEmbed.set_image(url = f'{icon_url}')
    avatarEmbed.timestamp = ctx.message.created_at
    await ctx.send(embed = avatarEmbed)

@client.command()
async def acak(ctx):
    await ctx.send('Ayo mengacak pilihan pengguna melalui *reaction*, jawablah pertanyaan berikut dalam waktu 30 detik!')

    questions = ['Di mana channel tujuan?',
    'Berapa lama durasi? (d/m/j/h)\nKeterangan:\n`d`: **detik**\n`m`: **menit**\n`j`: **jam**\n`h`: **hari**\nContoh, `15d` berarti 15 detik',
    'Apa konteks pengacakan?']

    answers =[]

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    for i in questions:
        await ctx.send(i)

        try:
            msg = await client.wait_for('message', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('Waktu habis, silahkan jalankan ulang perintah bot!')
            return
        else:
            answers.append(msg.content)

    try:
        c_id = int(answers[0][2:-1])
    except:
        await ctx.send(f'Anda tidak menyebut *channel* dengan benar. Lakukan seperti ini lain kali: {ctx.channel.mention}')
        return

    channel = client.get_channel(c_id)

    time = convert(answers[1])
    if time == -1:
        await ctx.send(f'Anda tidak menjawab dengan unit waktu yang benar. Gunakan d/m/j/h untuk keterangan waktu, misal 1h untuk 1 hari')
        return
    elif time == -2:
        await ctx.send(f'Waktu harus dinyatakan dengan bilangan bulat!')
        return
    
    prize = answers[2]

    await ctx.send(f'Pemilihan akan diadakan pada {channel.mention} dan akan berlangsung selama {answers[1]}!')

    embed = discord.Embed(title = 'Acak-acak:', description = f'{prize}', color = ctx.author.color)

    embed.add_field(name = 'Diselenggarakan oleh:', value = ctx.author.mention)

    embed.set_footer(text = f'Klik tombol ✅ untuk ikut serta, berakhir {answers[1]} dari sekarang!')

    my_msg = await channel.send(embed = embed)


    await my_msg.add_reaction("✅")

    await asyncio.sleep(time)

    new_msg = await channel.fetch_message(my_msg.id)

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await channel.send(f'Hasil pemilihan acak adalah pengguna {winner.mention} untuk {prize}!')

@client.command()
async def cahyo(ctx, *args):
    msg = " ".join(args)
    font = ImageFont.truetype("PatrickHand-Regular.ttf", 50)
    img = Image.open("cahyo.png")
    cx, cy = (350, 230)

    lines = textwrap.wrap(msg, width=20)
    print(lines)
    w, h = font.getsize(msg)
    y_offset = (len(lines)*h)/2
    y_text = cy-(h/2) - y_offset

    for line in lines:
        draw = ImageDraw.Draw(img)
        w, h = font.getsize(line)
        draw.text((cx-(w/2), y_text), line, (0, 0, 0), font=font)
        img.save("cahyo-edited.png")
        y_text += h

    with open("cahyo-edited.png", "rb") as f:
        img = File(f)
        await ctx.channel.send(file=img)

@client.command()
async def alif(ctx, *args):
    msg = " ".join(args)
    font = ImageFont.truetype("PatrickHand-Regular.ttf", 50)
    img = Image.open("alif.png")
    cx, cy = (650, 205)

    lines = textwrap.wrap(msg, width=20)
    print(lines)
    w, h = font.getsize(msg)
    y_offset = (len(lines)*h)/2
    y_text = cy-(h/2) - y_offset

    for line in lines:
        draw = ImageDraw.Draw(img)
        w, h = font.getsize(line)
        draw.text((cx-(w/2), y_text), line, (0, 0, 0), font=font)
        img.save("alif-edited.png")
        y_text += h

    with open("alif-edited.png", "rb") as f:
        img = File(f)
        await ctx.channel.send(file=img)

@client.command(aliases=["ANIME", "a"])
async def anime(ctx, *, title):
    embed = animeSearch(title)
    await ctx.send(embed=embed)

@client.command(aliases=['PENGGUNA', 'p'])
async def pengguna(ctx, *, userName):
    result = generateUserInfo(userName)
    if result:
        try:
            userEmbed = userSearch(result)
            await ctx.send(embed=userEmbed)

            userAnimeEmbed = userAnime(result)
            await ctx.send(embed=userAnimeEmbed)

            userMangaEmbed = userManga(result)
            await ctx.send(embed=userMangaEmbed)

        except HTTPException:
            pass
    else:
        await ctx.send(embed=userError(userName))

client.run(TOKEN)