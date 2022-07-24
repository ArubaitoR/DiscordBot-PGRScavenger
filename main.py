from http import client
import discord
from discord.ext import commands
import pgr_coop
import importlib

TOKEN = 'id'

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# PGR COOP EVENT SCHEDULE INFO
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


client.run(TOKEN)
