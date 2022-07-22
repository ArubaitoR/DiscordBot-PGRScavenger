from http import client
import discord
import pgr_coop

TOKEN = 'id'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'pgr-coop-status' or 'radio-command':
        if user_message.lower() == '!coop':
            await message.channel.send(f'__**Punishing: Gray Raven - SCAVENGER EVENT**__\nJam Saat Ini: {pgr_coop.timeNow} \nJadwal Pertama {pgr_coop.timeStart1} - {pgr_coop.timeEnd1}: {pgr_coop.result1} \nJadwal Kedua {pgr_coop.timeStart2} - {pgr_coop.timeEnd2}: {pgr_coop.result2}\nJadwal Ketiga {pgr_coop.timeStart3} - {pgr_coop.timeEnd3}: {pgr_coop.result3}')
            return


client.run(TOKEN)