import discord
import asyncio

TOKEN = 'ur bot token'
# add unlimited channel ids mate 
CHANNEL_IDS = [10101, 10101, 10101, 10101, 10101]

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await delete_messages()

async def delete_messages():
    while True:
        for channel_id in CHANNEL_IDS:
            channel = client.get_channel(channel_id)
            async for message in channel.history(limit=None):
                if not message.pinned:
                    await message.delete()
            await asyncio.sleep(1)

client.run(TOKEN)
