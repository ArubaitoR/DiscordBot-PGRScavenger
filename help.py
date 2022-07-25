import discord


def helpMessage():
    embed = discord.Embed(
        title='Daftar Perintah',
        colour=discord.Colour.orange()
    )
    embed.set_author(name='VoxB - Bot Utilitas Personal VoxP')
    embed.add_field(name='!coop', value="Menampilkan info event game PGR, menggunakan Asia/Jakarta sebagai basis zona waktu.", inline=False)
    embed.add_field(name='!foto <@pengguna>', value="Menampilkan foto profil pengguna", inline=False)
    embed.add_field(name='!acak', value="Membuat post undian secara interaktif untuk pemilihan/giveaway", inline=False)
    embed.add_field(name='!alif <teks>', value="Membuat teks *bubble speech* dengan foto alif.", inline=False)
    embed.add_field(name='!cahyo <teks>', value="Membuat teks *bubble speech* dengan foto cahyo.", inline=False)
    embed.add_field(name='!anime <judul>', value="Mencari laman informasi dari judul anime yang diketik.", inline=False)
    embed.add_field(name='!pengguna <nama>', value="Mencari laman informasi anilist pengguna.", inline=False)
    embed.add_field(name='!ingetin <waktu> <kegiatan>', value="Bot akan mengingatkan sesuai dengan waktu yang ditetapkan. (d/m/j/h)", inline=False)
    return embed
