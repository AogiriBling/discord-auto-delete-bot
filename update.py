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
            try:
                async for message in channel.history(limit=None):
                    if not message.pinned:
                        await message.delete()
                    await asyncio.sleep(0.5)  # slight delay between message deletions
            except discord.errors.HTTPException as e:
                print(f"Encountered HTTPException: {e}")
                await asyncio.sleep(5)  # yay retry 5 seconds
            except discord.errors.Forbidden as e:
                print(f"Encountered Forbidden: {e}")
                await asyncio.sleep(5)  # dw guys this will auto fix retry

client.run(TOKEN)
