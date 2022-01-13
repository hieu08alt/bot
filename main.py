import discord
import asyncio
from all_function import get_badword, config_bot


list_bad_word = get_badword()
config = config_bot()
mute_time = config["mute_time"]
client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(f'Bot is online!'))
    print('we have logged in as {0.user}'.format(client))
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content

    if message.content.startswith('!ping'):
      await message.channel.send(f'{message.author.mention} | in {round(client.latency * 1000)}ms')

    if any(word in msg.upper() for word in list_bad_word):
      guild = message.guild
      channel = client.get_channel(config["id_channel_send"])
      delete_message = message
      await delete_message.delete()
      for role in guild.roles:
        if role.name == "Muted":
            await message.author.add_roles(role)
            ping = await channel.send(f'{message.author.mention}')
            await ping.delete()
            embed_mute = discord.Embed(title=f"{message.author}", description="", color=0xff7373) 
            embed_mute.add_field(name=f"Mute {mute_time}s", value=f"Lí do: Nói bậy", inline=False)
            embed_mute.add_field(name=f"Nội dung tin nhắn:", value=f"{message.content}", inline=False)
            embed_mute.add_field(name=f"Tin nhắn được gửi tại kênh:", value=f"{message.channel}", inline=False)
            embed_mute.add_field(name=f"Lưu ý:", value=f"Nếu bạn không nói tục mà bot warn thì hãy nhắn tin tới {config['author']} để được gỡ mute.", inline=False)
            await channel.send(embed=embed_mute)
    
            await asyncio.sleep(mute_time)

            await message.author.remove_roles(role)
            await channel.send(f'{message.author.mention} Hết bị mute gòi nha')
            return


client.run(config["TOKEN"])
