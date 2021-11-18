import discord
from discord.ext import commands

app = commands.Bot(command_prefix="!")


@app.event
async def on_ready():
    print(f'{app.user.name}이 서버에 입장했습니다.')
    await app.change_presence(status=discord.Status.online, activity=None)
    print('ready')

bot_token = open('token.txt', 'r')
app.run(bot_token.readline())
