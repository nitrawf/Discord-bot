import discord
import giphypop
import random
import json
from vocabulary.vocabulary import Vocabulary as vb


TOKEN = None # place your token here
g=giphypop.Giphy() #giphypop object
client = discord.Client()	#discord.py object

@client.event
async def on_message(message):
	# we do not want the bot to reply to itself
	if message.author == client.user:
		return
	
	#check if bot is working
	if message.content.startswith('!heck'):
		msg = 'Heck Off {0.author.mention}'.format(message)
		await client.send_message(message.channel, msg)
	
	#text response
	if message.content.startswith('!venom'):
		msg = 'is cute uwu'.format(message)
		await client.send_message(message.channel, msg)
	
	#text response
	if message.content[0:4] == "ayy":
		await client.send_message(message.channel,"lmao".format(message))
	
	#text response
	if message.content[0:5] == "lmao":
		await client.send_message(message.channel,"ayy".format(message))
	
	#using giphy api post a random happy birthday gif
	if message.content.startswith("!hbd"):
		msg="HAPPPY BARTHDAYYYYY "
		if len(message.mentions)>0:
			msg+=message.mentions[0].mention
		hbds=[x for x in g.search("happy birthday")]
		hbd=hbds[random.randint(0,len(hbds))]
		msg+=" "+hbd.media_url
		await client.send_message(message.channel, msg)
	#tag spam a user(not recommended)	
	if message.content.startswith("!tagspam"):
		msg=""
		if len(message.mentions)>0:
			for i in message.mentions:
				msg+=i.mention+"\t"
		else:
			msg="Mention someone."
			await client.send_message(message.channel, msg)
			return
		for x in range(5):
			await client.send_message(message.channel, msg)
	
	#synonym using vocabulary api
	if message.content[0:3]=="!s ": #match first 3 charachters
		query=message.content.split(" ")[1] #seperate the content from the identifier
		result=vb.synonym(query)
		msg=""
		if result == False:	#if no reply from api 
			msg="Not found"	
		else:
			result=json.loads(result) #parse json string
			for i in result:
				msg+=i["text"]+"\n"	#add all results
		await client.send_message(message.channel,msg)
	
	#antonym using vocabulary api
	if message.content[0:3]=="!a ":
		query=message.content.split(" ")[1]
		result=vb.antonym(query)
		msg=""
		if result == False:
			msg="Not found"
		else:
			result=json.loads(result)
			for i in result:
				msg+=i["text"]+"\n"
		await client.send_message(message.channel,msg)
	
	#usage	
	if message.content[0:3]=="!u ":
		query=message.content.split(" ")[1:]
		query=' '.join(query)
		result=vb.usage_example(query)
		msg=""
		if result == False:
			msg="Not found"
		else:
			result=json.loads(result)
			for i in result:
				msg+=i["text"]+"\n"
		await client.send_message(message.channel,msg)
	
	#meaning
	if message.content[0:3]=="!m ":
		query=message.content.split(" ")[1]
		result=vb.meaning(query)
		msg=""
		if result == False:
			msg="Not found"
		else:
			result=json.loads(result)
			for i in result:
				msg+=i["text"]+"\n"
		await client.send_message(message.channel,msg)
	
	

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.run(TOKEN)