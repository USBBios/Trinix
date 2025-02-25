#Required Imports
import discord
import datetime, time
import requests 
from discord.ext import commands, tasks
from random import choice 

start_time = time.time()

footer = "https://cdn.discordapp.com/attachments/888282878973194271/891935435859820574/default.png"

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='userinfo', aliases=["whois"]) #this code was from stackoverflow
    async def userinfo(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author
        roles = [role for role in member.roles]
        embed = discord.Embed(color=discord.Color.blurple(), timestamp=ctx.message.created_at,
                              title=f"Trinix UserInfo - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}")
        embed.add_field(name="Display Name:", value=member.display_name)
        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Account Created On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Highest Role:", value=member.top_role.mention)
        await ctx.send(embed=embed)

    @commands.command(name='uptime', aliases=['upt'])
    async def uptime(self, ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = 'Tirnix Up time: ' + str(datetime.timedelta(seconds=difference)) + ''
        embed = discord.Embed(color=discord.Color.blurple())
        embed.add_field(name="Uptime", value=text)
        embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("Current uptime: " + text)

    @commands.command(name='ping', aliases=["ms"])
    async def ping(self, ctx):
        await ctx.send(f'My Server Ping ({round(self.bot.latency * 1000)}ms)')

    @commands.command(name='website')
    async def website(self, ctx):
        embed=discord.Embed(title="Trinix Bot", description= "Website: https://trinixbot.xyz/", color = discord.Color.blurple())
        embed.add_field(name="Thank you for using Trinix", value="If you need any support join the discord", inline=False)
        embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
        await ctx.send(embed=embed)

    @commands.command(name='oauth')
    async def oauth(self, ctx):
        responses = 'Heres my invite link https://discord.com/oauth2/authorize?client_id=695402766268366949&permissions=8&scope=bot <3'
        await ctx.send(responses)

    @commands.command(name='passgen', aliases=['pwg'])
    async def passgen(self, ctx):
        API = "https://www.passwordrandom.com/query?command=password"
        x = requests.get(API)
        await ctx.author.send(x.text)
    
    @commands.command(name='sinvite')
    async def sinvite(self, ctx):
        invite = await ctx.channel_invite()
        await ctx.relpy(f"Here's your invite: {invite}")

def setup(bot): #Must have a setup function
    bot.add_cog(Misc(bot)) # Add the class to the cog.
