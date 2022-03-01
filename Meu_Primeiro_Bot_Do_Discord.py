bot = commands.Bot("!")

@bot.event
async def on_ready():
    print(f"Estou pronto! Estou conectado como {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "palavrao" in massage.content:
        await massage.channel.send(f"Por favor, {massage.author}, não ofenda os demais usuarios!")

        await message.delete()

    await bot.process_commands(massage)




@bot.command(name="oi")
async def sand_hello(ctx):
    name = ctx.author.name

    response = "Olá, " + name

    await ctx.send(response)

    