import subprocess as sp
from discord.ext import commands
import discord
import builtins

bot = commands.Bot(command_prefix="sq!")

process = sp.Popen(['python3', 'Squid_Bot.py'])
authorized_roles = [651783488034570240, 651779641572458502]

bot.help_command = None


@bot.command()
@commands.has_any_role(*authorized_roles)
async def help(ctx):
    await ctx.send(
        "> %sstart --- Starts the Bot\n%sstatus --- Displays Bot Status\n%sterminate --- Terminates the Bot" % bot.command_prefix)


@bot.command()
@commands.has_any_role(*authorized_roles)
async def status(ctx):
    """Displays Bot Status"""
    if process.poll() is None:
        await ctx.channel.send("Currently Running!")
    else:
        await ctx.send("Currently Paused!")


@bot.command()
@commands.has_any_role(*authorized_roles)
async def start(ctx):
    """Starts the Bot"""
    global process
    if process.poll() is None:
        await ctx.channel.send('It\'s already running!')
        return
    process = sp.Popen(['python3', 'Squid_Bot.py'])
    await ctx.channel.send("Start!")


@bot.command()
@commands.has_any_role(*authorized_roles)
async def terminate(ctx):
    """Terminates the Bot"""
    process.terminate()
    process.wait()
    await ctx.channel.send("Terminated!")
    await ctx.guild.get_channel(651785448431157268).send(
        "%s has terminated the bot(id: %d)" % (ctx.author.name, ctx.author.id))


bot.run(open("Squid-Token.txt").read())
