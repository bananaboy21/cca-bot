import discord
import os
import io
from discord.ext import commands
bot = commands.Bot(command_prefix="-",owner_id=277981712989028353)
bot.remove_command('help')


@bot.event
async def on_ready():
    print('Bot is online, and ready to ROLL!')
    await bot.change_presence(activity=discord.Game(name="-help for help!"))
    

@bot.command()
async def help(ctx):
    em = discord.Embed(color=discord.Color(value=0x00ff00), title="CCA Bot Help")
    em.add_field(name="invite", value="Gives CCA's server invite link.", inline=False)
    em.add_field(name="events", value="Gets CCA's upcoming events.", inline=False)
    em.add_field(name="winners", value="Gets winners of previous seasons.", inline=False)
    em.add_field(name="rules", value="Gets the rules for CCA.", inline=False)
    em.add_field(name="roster", value="Gets the link for the CCA roster.", inline=False)
    em.add_field(name="website", value="Gets the CCA website.", inline=False)
    em.add_field(name="media", value="Gets links to all of CCA's social media.", inline=False)
    em.set_thumbnail(url="https://scontent-atl3-1.cdninstagram.com/vp/5c554a60f786fd5298e3a01d3063940b/5B774960/t51.2885-15/s1080x1080/e15/fr/29093015_1791620990897131_3863801241461063680_n.jpg")
    await ctx.send(embed=em)
    

@bot.command()
async def invite(ctx):
    """Gives the server invite."""
    await ctx.send("Invite to the server: https://discord.gg/DXKpZwy")
    
    
@bot.command()
async def events(ctx):
    """Gives any upcoming events."""
    await ctx.send("**Upcoming Events**\n\nCHALLENGE WAR LEAGUE (S2)")
    
    
@bot.command()
async def winners(ctx):
    """Gives the winners for CCL."""
    await ctx.send("**Previous Winners:**\n\nTH9 - WhySoSerious?\nTH8 - Gangsteryashmin\nCCWL s1 - THE WAR KINGS")
    
    
@bot.command()
async def rules(ctx):
    """Gets the rules for CCL."""
    await ctx.send("Read the rules carefully! \nhttps://docs.google.com/document/d/1Ika-P9SmYFw-lQ-ZJz2z33VAXQVw9eTlZF4fClAuBpc/edit?usp=drivesdk")
    
    
@bot.command()
async def roster(ctx):
    """Gets the roster."""
    await ctx.send("**Master Roster** \nhttps://drive.google.com/file/d/134skIPyo9J7eReAhNtDngBGfG_jvid7E/view?usp=drivesdk")


@bot.command()
async def website(ctx):
    """Gets the CCL website."""
    await ctx.send("Website: https://besotted-dominion.000webhostapp.com/index.html")
    
    
@bot.command(aliases=['social', 'socialmedia', 'sm'])
async def media(ctx):
    await ctx.send("__**Social Media**__ \n\n**Facebook:** https://m.facebook.com/Clash-Challenge-Academy-CCA-309095529618524/\n**Instagram:**https://www.instagram.com/p/BgksMZGH-tq/")
    
bot.run(os.environ.get('TOKEN'))
    
