import discord
import random
token = "OTIyOTIzMzY5MDk4MjY0NjY2.YcIhXg.hIREGTPxeaFgefgY6iPnpImR-p0"

client = discord.Client()
themes = ['Wet Wednesday', 'Thirsty Thursday',
          'Fuck me Friday', 'Taco Tuesday', 'Manhood Monday', 'Sexy Saturday', 'Sensuous Sunday']
todays_theme = ""
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!ping"):
        msg = "Pong"
        await message.channel.send(msg)
    if message.content.startswith("!help"):
        msg = "Fuck you and your help. Just kidding, here ya go"
        await message.channel.send(msg)
    if message.content.startswith("!theme"):
        msg = "Picking Random Theme"
        await message.channel.send(msg)
        msg = f'Todays Theme is {themes[random.randint(0, len(themes))]}'
        await message.channel.send(msg)
    if message.author.name == "OutcastGamer":
        msg = f'Hi @everyone, @Server Daddy has arrived'
        await message.channel.send(msg)
    if "bad bot" in str(message.content).lower():
        msg = f"Spank me please {message.author.name} 🥺"
        await message.channel.send(msg)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print('---------')

client.run(token)