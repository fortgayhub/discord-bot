import os
import random
import discord
import colorama
from colorama import Fore, Style
from discord.ext import commands

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
       print(Fore.WHITE + "Setting up Web Server! Ping it at https://uptimerobot.com to keep it running 24/7 without paying for a subscription! You could use Heroku or glitch to host this, I would recommend Heroku")
       print(Fore.GREEN + Style.BRIGHT + "Bot is Ready! ")
       print(Fore.YELLOW + Style.BRIGHT + "Custom Status Incoming Setting up")
       await client.change_presence(status=discord.Status.idle, activity=discord.Game("Hello World"))
       
# purge #

@client.command()
async def purge(ctx, amount=5):
        await ctx.channel.purge(limit=amount)

# kick command #

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"Kicked Out {member} for `{reason}`")
        print(Fore.CYAN + f"Kicked out {member} for the reason: {reason}")

@kick.error
async def kick_error(ctx, error):
   if isinstance(error, commands.MissingPermissions):
           await ctx.send("You do not have permissions to use the Kick Command!")
           print(Fore.LIGHTBLUE_EX + f"Someone tried to use Kick Command!")

# ban code #

@client.command()
@commands.has_permissions(kick_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member} for `{reason}`")
        print(Fore.RED + f"Your moderator/ or you, Banned {member} for the reason: {reason}")

@ban.error
async def ban_error(ctx, error):
   if isinstance(error, commands.MissingPermissions):
           await ctx.send("You do not have permissions to use the Ban command!")
           print(Fore.LIGHTRED_EX + f"Someone tried to use Ban Command!")

# unban code #

@client.command()
@commands.has_permissions(kick_members=True)
async def unban(ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
                user = ban_entry.user

                if(user.name, user.discriminator) == (member_name, member_discriminator):
                        await ctx.guild.unban(user)
                        await ctx.send(f'Unbanned {user.mention}')
                        return

@unban.error
async def unban_error(ctx, error):
   if isinstance(error, commands.MissingPermissions):
           await ctx.send("You do not have permissions to use the UnBan command!")
           print(Fore.BLUE + f"Someone tried to use UnBan Command!")

# fun commands #

@client.command()
async def coinflip(ctx):
        choices = ["Heads", "Tails"]
        rancoin = random.choice(choices)
        await ctx.send(rancoin)

@client.command()
async def dice(ctx):
        choices = ["Without a doubt", "No way", "As I see it, probably a no from me", "NO WAY THAT IS HAPPENING! `NO WAY`"]
        rancoin = random.choice(choices)
        await ctx.send(rancoin)
        

client.run('ODQ4OTIxODMzMDcwOTE5NzUx.YLTqEQ.Mw3wUcZK1r0EdmPOCpsSn09WerI')
