import discord
import asyncio

TOKEN = 'put ur token here'

CHANNEL_ID = 10101010

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await delete_messages()

async def delete_messages():
    channel = client.get_channel(CHANNEL_ID)
    while True:
        async for message in channel.history(limit=None):
            if not message.pinned:
                await message.delete()
            await asyncio.sleep(1)

client.run(TOKEN)
# Bling is The God of awesomeness!
