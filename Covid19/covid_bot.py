import discord
from covid_backend import displayAllCountries, globalStats, displayOneCountry
from configer import TOKEN

client = discord.Client()

@client.event
async def on_ready():
	game = discord.Game("with COVID19 | c!help")
	print('logged in as {0.user}'.format(client))
	await client.change_presence(status=discord.Status.idle, activity=game)

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('c!help'):
		embed = discord.Embed(title="COVID19 - Bot", description="New and reliable Stats", color=0xff0000)
		embed.add_field(name="***c!help***", value="This page", inline=False)
		embed.add_field(name="***c!global***", value="Shows global COVID-stats", inline=False)
		embed.add_field(name="***c!countries***", value="Shows available Countries", inline=False)
		embed.add_field(name="***c!country [CountryName/CountryCode]***", value="Shows stats for the specified Country\n`$country Germany` / `$country DE`", inline=False)
		embed.add_field(name="***c!leaderboards***", value="Shows Leaderboards", inline=False)
		embed.add_field(name="***c!github***", value="Shows the Github repo", inline=False)
		embed.add_field(name="***c!add | c!invite***", value="Shows the invite link", inline=False)
		embed.set_footer(text="{}#{} by xnacly".format(client.user.name, client.user.discriminator), icon_url=client.user.avatar_url)
		await message.channel.send(embed=embed)
	
	if message.content.startswith('c!github'):
		embed = discord.Embed(title="COVID19 - Bot", description="New and reliable Stats", color=0xff0000)
		embed.add_field(name="Github repo:", value="https://github.com/xNaCly/scripts/tree/master/Covid19")
		embed.set_footer(text="{}#{} by xnacly".format(client.user.name, client.user.discriminator), icon_url=client.user.avatar_url)
		await message.channel.send(embed=embed)

	if message.content.startswith("c!global"):
		stringer = globalStats()
		embed = discord.Embed(title="COVID19 - Bot", description="New and reliable Stats", color=0xff0000)
		embed.add_field(name="Global-Stats:", value=stringer)
		embed.set_footer(text="{}#{} by xnacly".format(client.user.name, client.user.discriminator), icon_url=client.user.avatar_url)
		await message.channel.send(embed=embed)
	
	if message.content.startswith("c!countries"):
		embed = discord.Embed(title="COVID19 - Bot", description="New and reliable Stats", color=0xff0000)
		embed.add_field(name="Available Countries:", value="https://raw.githubusercontent.com/xNaCly/scripts/master/Covid19/available_countries.txt")
		embed.set_footer(text="{}#{} by xnacly".format(client.user.name, client.user.discriminator), icon_url=client.user.avatar_url)
		await message.channel.send(embed=embed)


	if message.content.startswith("c!add") or message.content.startswith("c!invite"):
		embed = discord.Embed(title="COVID19 - Bot", description="New and reliable Stats", color=0xff0000)
		embed.add_field(name="Invite Link:", value="https://discord.com/api/oauth2/authorize?client_id=707277819788525599&permissions=11264&scope=bot")
		embed.set_footer(text="{}#{} by xnacly".format(client.user.name, client.user.discriminator), icon_url=client.user.avatar_url)
		await message.channel.send(embed=embed)

	# dev area: 
	notDoneYetEmbed = discord.Embed(title="COVID19 - Bot", description="New and reliable Stats", color=0xff0000)
	notDoneYetEmbed.add_field(name="Error: ", value="this command isnt finished yet")
	notDoneYetEmbed.set_footer(text="{}#{} by xnacly".format(client.user.name, client.user.discriminator), icon_url=client.user.avatar_url)
	# await message.channel.send(embed=notDoneYetEmbed)

	if message.content.startswith("c!leaderboards"):
		await message.channel.send(embed=notDoneYetEmbed)

	if message.content.startswith("c!country"):
		args = message.content.split(" ")
		stringer = displayOneCountry(args[1])
		embed = discord.Embed(title="COVID19 - Bot", description="New and reliable Stats", color=0xff0000)
		embed.add_field(name=f"{args[1]}-Stats:", value=stringer)
		embed.set_footer(text=f"{client.user.name}#{client.user.discriminator} by xnacly", icon_url=client.user.avatar_url)
		await message.channel.send(embed=embed)
	

client.run(TOKEN)