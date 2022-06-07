# Discord Bot - Update Channel Name To Current Date
# Author: DociTeam - https://github.com/DociTeam

from discord.ext import commands, tasks
import jdatetime

client = commands.Bot(command_prefix = '!')
TOKEN = ""

@client.event
async def on_ready():
    zaman.start()
    print('Ready To Use.')
        

@tasks.loop(minutes=10)
async def zaman():
    tarikh_channel = client.get_channel(962764016428671077)
    fa_date = jdatetime.date.today()
    t_banner = fa_date.strftime("%y %B %d")
    await tarikh_channel.edit(name=f"〢「 {t_banner} 」")

client.run(TOKEN)