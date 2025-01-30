import discord
from discord.ext import commands
Channel_id = 1329250229022621738
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    channel = bot.get_channel(Channel_id)
    print(f'We have logged in as {bot.user}')
    await channel.send("🟢READY🟢")    

@bot.command()
async def Climatico(ctx):
    mbed = discord.Embed(color=discord.Color.green(), title="Cambio climatico", description="El cambio climático es: Cambios a largo plazo en las temperaturas y patrones climáticos de la Tierra.")
    await ctx.reply(embed=mbed)

@bot.command()
async def climatico(ctx):
    mbed = discord.Embed(color=discord.Color.green(), title="Cambio climatico", description="El cambio climático es: Cambios a largo plazo en las temperaturas y patrones climáticos de la Tierra.")
    await ctx.reply(embed=mbed)

@bot.command()
async def Causas(ctx):
    mbed = discord.Embed(color=discord.Color.green(), title="Causas del cambio climático", description="Las causas del cambio climatico son: La generación de energía a partir de combustibles fósiles, la industria y manufactura, la deforestación, entre otros.")
    await ctx.reply(embed=mbed)

@bot.command()
async def causas(ctx):
    mbed = discord.Embed(color=discord.Color.green(), title="Causas del cambio climático", description="Las causas del cambio climatico son: La generación de energía a partir de combustibles fósiles, la industria y manufactura, la deforestación, entre otros.")
    await ctx.reply(embed=mbed)

@bot.command()
async def Soluciones(ctx):
    mbed = discord.Embed(color=discord.Color.green(), title="Soluciones para el cambio climático", description="Aunque no se puede frenar totalmente, algunas maneras de reducir el cambio climático son: Mejorar nuestra eficiencia energética al ser mas concientes sobre nuestro uso de energía, plantar arboles en zonas verdes cercanas, usar fuentes de energía renovables, entre otros.")
    await ctx.reply(embed=mbed)

@bot.command()
async def soluciones(ctx):
    mbed = discord.Embed(color=discord.Color.green(), title="Soluciones para el cambio climático", description="Aunque no se puede frenar totalmente, algunas maneras de reducir el cambio climático son: Mejorar nuestra eficiencia energética al ser mas concientes sobre nuestro uso de energía, plantar arboles en zonas verdes cercanas, usar fuentes de energía renovables, entre otros.")
    await ctx.reply(embed=mbed)


@bot.command()
async def info(ctx):
    mbed = discord.Embed(color=discord.Color.green(), title="Visita esta página web para mas información sobre el cambio climático", description="http://127.0.0.1:5000")
    await ctx.reply(embed=mbed)

@bot.command()
async def Info(ctx):
    mbed = discord.Embed(color=discord.Color.green(), title="Visita esta página web para mas información sobre el cambio climático", description="http://127.0.0.1:5000")
    await ctx.reply(embed=mbed)

bot.run("token")
