import os
import discord 
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

token = os.environ['TOKEN']
client = discord.Client()

sad_words = ['sad', 'depressed', 'unhappy', 'angry', 'miserable', 'depressing']

starter_encouragements = [
  'Cheer up !',
  'Hang in there !',
  'You are a great person / bot !'
]

if 'responding' not in db.keys():
  db['responding'] = True

def get_quote():
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + "\r\n - " + json_data[0]['a']
  return quote

def update_encouragements(encouraging_message):
  if 'encouragements' in db.keys():
    encouragements = db['encouragements']
    encouragements.append(encouraging_message)
    db['encouragements'] = encouragements
  else:
    db['encouragements'] = [encouraging_message]

def delete_encouragement(index):
  encouragements = db['encouragements']
  if len(encouragements) > index:
    del encouragements[index]
    db['encouragements'] = encouragements

@client.event
async def on_ready():
  print('We have logged in as {0.user}'
  .format(client))

  # Set bot activity
  await client.change_presence(activity=discord.Game('$help'))

  @client.event
  async def on_message(message):
    if message.author == client.user:
      return

    msg = message.content

    # Help message

    if msg.startswith('$help'):
      await message.channel.send(
        'Here is a list of all the commands available : \n\n Create a new encouragement message : \n **`$new [encouragement]`** \n List all encouragement messages : \n **`$list`** \n Delete an encouragement : \n **`$del [index]`** \n Enable/Disable responding : \n **`$responding [true|false]`**'
      )

    if db['responding']:
      options = starter_encouragements

      # Generate random quote from command '$quote'

      if msg.startswith('$quote'):
        quote = get_quote()
        await message.channel.send(quote)

      # Update encouragements

      if 'encouragements' in db.keys():
        options = options + list(db['encouragements'])

      # Sends encouragement message if any sad words in message

      if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(options))

    # Add new encouragement

    if msg.startswith('$new'):
      encouraging_message = msg.split('$new ', 1)[1]
      update_encouragements(encouraging_message)
      await message.channel.send('New encouraging message added.')

    # Delete encouragement

    if msg.startswith('$del'):
      encouragements = []
      if 'encouragements' in db.keys():
        index = int(msg.split('$del', 1)[1])
        delete_encouragement(index)
        encouragements = db['encouragements']
      await message.channel.send(encouragements)

    # Debug - Prints db encouragements

    if msg.startswith('$list'):
      encouragements = []
      if 'encouragements' in db.keys():
        encouragements = db['encouragements']
      await message.channel.send(encouragements)

    # Enable/Disable responding

    if msg.startswith('$responding'):
      value = msg.split('$responding ', 1)[1]

      if value.lower() == 'true':
        db['responding'] = True
        await message.channel.send('Responding is on.')
      else:
        db['responding'] = False
        await message.channel.send('Responding is off.')

keep_alive()
client.run(token)