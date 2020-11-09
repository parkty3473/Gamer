import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("Gamer Company")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("반가워")

client.run("Nzc1MzE3OTUwMzc4ODAzMjEx.X6klHA.yQBZMiGhgZK3Qzpb8X5_wKcd_t4")























































