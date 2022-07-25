import discord


def helpMessage():
    embed = discord.Embed(
        title='Daftar Perintah',
        colour=discord.Colour.orange()
    )
    embed.set_author(name='VoxB - Bot Utilitas Personal VoxP')
    embed.add_field(name='!coop', value="Menampilkan info event game PGR.", inline=False)
    embed.add_field(name='!acak', value="Membuat post undian secara interaktif untuk pemilihan/giveaway", inline=False)
    embed.add_field(name='!alif <teks>', value="Membuat teks *bubble speech* dengan foto alif.", inline=False)
    embed.add_field(name='!cahyo <teks>', value="Membuat teks *bubble speech* dengan foto cahyo.", inline=False)
    embed.add_field(name='!anime <judul>', value="Mencari laman informasi dari judul anime yang diketik.", inline=False)
    return embed