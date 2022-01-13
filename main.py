import discord
from discord.ext import commands, tasks
import os
import asyncio
import psutil
from all_function import get_badword, config_bot, change_time
from keep_alive import keep_alive


list_bad_word = get_badword()
config = config_bot()
mute_time = config["mute_time"]

client = commands.Bot(command_prefix = config["prefix_bot"])

def is_it_me(ctx):
  return ((ctx.author.id == 916641873437798410) or (ctx.author.id == 748444330536206336))

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(f'Love you BBao'))
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send(f'{ctx.author.mention} | Làm ơn hãy điền những tham số bị thiếu!.')
  if isinstance(error, commands.MissingPermissions):
    await ctx.send(f"{ctx.author.mention} | Bạn không có quyền để sử dụng câu lệnh!")
  if isinstance(error, commands.CommandOnCooldown):
    msg = '**Này này! Bạn phải chờ `{:.2f}s` để sử dụng lại lệnh đó**'.format(error.retry_after)
    delete_msg = await ctx.send(msg)
    await asyncio.sleep(int(error.retry_after))
    await delete_msg.delete()


@client.command()
async def ping(ctx):
  await ctx.send(f'{ctx.author.mention} | độ trễ: {round(client.latency * 1000)}ms')

@client.command()
@commands.check(is_it_me)
async def set_mutetime(ctx, time : int):
  mute_time = time
  change_time(time)
  await ctx.send(f"**đã sửa thời gian mute thành `{time}`**")

@client.command()
@commands.check(is_it_me)
async def show(ctx):
  em = discord.Embed(title=f"{ctx.author.name}", description="", color=0xff7373)
  for show in config:
    em.add_field(name=f"{show}", value=f"`{config[show]}`", inline=True)
  await ctx.send(embed=em)


@client.command()
@commands.check(is_it_me)
async def check_vps(ctx):
  cpu_used = psutil.cpu_percent()
  ram_used = psutil.virtual_memory()[2]
  embed_vps = discord.Embed(title=f"{ctx.author} - Check VPS", description="", color=0x36ff57) 
  embed_vps.add_field(name="CPU", value=f"{cpu_used}", inline=True)
  embed_vps.add_field(name="RAM", value=f"{ram_used}", inline=True)
  await ctx.send(embed = embed_vps)



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content

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
    await client.process_commands(message)

keep_alive()
client.run(os.getenv('TOKEN'))
