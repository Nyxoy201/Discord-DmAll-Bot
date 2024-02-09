import discord
from discord.ext import commands
import pystyle
from pystyle import Colors,Colorate
import asyncio 

intents = discord.Intents.all()  

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(Colorate.Horizontal(Colors.purple_to_blue,"""
 ██████╗ ███╗   ███╗ █████╗ ██╗     ██╗         ██████╗  ██████╗ ████████╗
 ██╔══██╗████╗ ████║██╔══██╗██║     ██║         ██╔══██╗██╔═══██╗╚══██╔══╝
 ██║  ██║██╔████╔██║███████║██║     ██║         ██████╔╝██║   ██║   ██║   
 ██║  ██║██║╚██╔╝██║██╔══██║██║     ██║         ██╔══██╗██║   ██║   ██║   
 ██████╔╝██║ ╚═╝ ██║██║  ██║███████╗███████╗    ██████╔╝╚██████╔╝   ██║   
 ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚═════╝  ╚═════╝    ╚═╝   
"""))
    print(Colorate.Horizontal(Colors.purple_to_blue,f'[+] Connected as {bot.user.name} ({bot.user.id})'))



bot_token = "" # Your bot token
whitelist_file = "wl.txt" # Whitelist file, don't touch
admin_user_id = 11111111111111 # Owner discord ID




@bot.command(name='wl')
async def whitelist(ctx, user_id: int):

    if ctx.author.id != admin_user_id:
        embed = discord.Embed(
            title="WL Manager",
            description=f"""`❌` **You are not authorized to use this command.**
Only the `bot owner` can use this command.""",
            color=discord.Color(0x17004e)
        )

        if isinstance(ctx.author, discord.User):
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        elif isinstance(ctx.author, discord.Member):
            user = ctx.author
            avatar_url = user.avatar.url if user.avatar else user.default_avatar.url
            embed.set_thumbnail(url=avatar_url)
            embed.set_footer(text=f"Requested by {user.name}")

        await ctx.send(embed=embed)
        return

    with open(whitelist_file, 'r') as file:
        whitelist = [line.strip() for line in file]

    if str(user_id) in whitelist:
        embed = discord.Embed(
            title="WL Manager",
            description=f"""`✅` **User with ID `{user_id}` is already in the bot whitelist.**""",
            color=discord.Color(0x17004e)
        )

        if isinstance(ctx.author, discord.User):
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        elif isinstance(ctx.author, discord.Member):
            user = ctx.author
            avatar_url = user.avatar.url if user.avatar else user.default_avatar.url
            embed.set_thumbnail(url=avatar_url)
            embed.set_footer(text=f"Requested by {user.name}")

        await ctx.send(embed=embed)
        return

    with open(whitelist_file, 'a') as file:
        file.write(str(user_id) + '\n')
        embed = discord.Embed(
            title="WL Manager",
            description=f"""`✅` **User with ID `{user_id}` has been successfuly added to the bot whitelist.**""",
            color=discord.Color(0x17004e)
        )

        if isinstance(ctx.author, discord.User):
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        elif isinstance(ctx.author, discord.Member):
            user = ctx.author
            avatar_url = user.avatar.url if user.avatar else user.default_avatar.url
            embed.set_thumbnail(url=avatar_url)
            embed.set_footer(text=f"Requested by {user.name}")

        await ctx.send(embed=embed)


@bot.command(name='unwl')
async def unwhitelist(ctx, user_id: int):

    if ctx.author.id != admin_user_id:
        embed = discord.Embed(
            title="WL Manager",
            description=f"""`❌` **You are not authorized to use this command.**
Only the `bot owner` can use this command.""",
            color=discord.Color(0x17004e)
        )

        if isinstance(ctx.author, discord.User):
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        elif isinstance(ctx.author, discord.Member):
            user = ctx.author
            avatar_url = user.avatar.url if user.avatar else user.default_avatar.url
            embed.set_thumbnail(url=avatar_url)
            embed.set_footer(text=f"Requested by {user.name}")

        await ctx.send(embed=embed)
        return

    with open(whitelist_file, 'r') as file:
        whitelist = [line.strip() for line in file]

    if str(user_id) not in whitelist:
        embed = discord.Embed(
            title="WL Manager",
            description=f"""`❌` **User with ID `{user_id}` is not in the bot whitelist.**""",
            color=discord.Color(0x17004e)
        )

        if isinstance(ctx.author, discord.User):
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        elif isinstance(ctx.author, discord.Member):
            user = ctx.author
            avatar_url = user.avatar.url if user.avatar else user.default_avatar.url
            embed.set_thumbnail(url=avatar_url)
            embed.set_footer(text=f"Requested by {user.name}")

        await ctx.send(embed=embed)
        return

    whitelist.remove(str(user_id))
    with open(whitelist_file, 'w') as file:
        file.write('\n'.join(whitelist))

    embed = discord.Embed(
        title="WL Manager",
        description=f"""`✅` **User with ID `{user_id}` has been removed from the bot whitelist.**""",
        color=discord.Color(0x17004e)
    )

    if isinstance(ctx.author, discord.User):
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
    elif isinstance(ctx.author, discord.Member):
        user = ctx.author
        avatar_url = user.avatar.url if user.avatar else user.default_avatar.url
        embed.set_thumbnail(url=avatar_url)
        embed.set_footer(text=f"Requested by {user.name}")

    await ctx.send(embed=embed)

    
    

@bot.command(name='cmd')
async def command(ctx):
    with open('wl.txt', 'r') as file:
        whitelist = [line.strip() for line in file]

    if str(ctx.author.id) not in whitelist:
        embed = discord.Embed(
            title="Commands Panel",
            description=f"""`❌` **You are not authorized to use this command.**
            Contact a staff member to be `whitelist`.""",
            color=discord.Color(0x17004e)
        )

        if isinstance(ctx.author, discord.User):
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        elif isinstance(ctx.author, discord.Member):
            user = ctx.author
            avatar_url = user.avatar.url if user.avatar else user.default_avatar.url
            embed.set_thumbnail(url=avatar_url)
            embed.set_footer(text=f"Requested by {user.name}")

        await ctx.send(embed=embed)

        return

    embed = discord.Embed(
        title="Commands Panel",
        description=f"""
1. `ping` → **Displays bot latency.**
2. `dm <user_id> <message>` → **Send a private message to a member with the bot.**
3. `dmall <0/1/2/3> <all/on/off> <message>` → **Send a message to everyone on the server.**
4. `servers` → **Show the servers where the bot is.**
5. `get <server_id>` → **Get an invitation to a server where the bot is.**
6. `wl <user_id>` → **Whitelist an user.**
7. `unwl <user_id>` → **UnWhitelist an user.**""",
        color=discord.Color(0x17004e)
    )

    if isinstance(ctx.author, discord.User):
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
    elif isinstance(ctx.author, discord.Member):
        user = ctx.author
        avatar_url = user.avatar.url if user.avatar else user.default_avatar.url
        embed.set_thumbnail(url=avatar_url)
        embed.set_footer(text=f"Requested by {user.name}")

    await ctx.send(embed=embed)


    

@bot.command(name='ping')
async def ping(ctx):
    with open('wl.txt', 'r') as file:
        whitelist = [line.strip() for line in file]

    if str(ctx.author.id) not in whitelist:
        embed = discord.Embed(
            title="Commands Panel",
            description=f"""`❌` **You are not authorized to use this command.**
            Contact a staff member to be `whitelist`.""",
            color=discord.Color(0x17004e)
        )

        if isinstance(ctx.author, discord.User):
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        elif isinstance(ctx.author, discord.Member):
            user = ctx.author
            avatar_url = user.avatar.url if user.avatar else user.default_avatar.url
            embed.set_thumbnail(url=avatar_url)
            embed.set_footer(text=f"Requested by {user.name}")

        await ctx.send(embed=embed)

        return
    latency = round(bot.latency * 1000)  
    embed = discord.Embed(
        title="Bot Latency",
        description=f"""
`🤖` The bot's latency is
`{latency}ms`.""",
        color=discord.Color(0x17004e)
    )

    if isinstance(ctx.author, discord.User):
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
    elif isinstance(ctx.author, discord.Member):
        user = ctx.author
        avatar_url = user.avatar.url if user.avatar else user.default_avatar.url
        embed.set_thumbnail(url=avatar_url)
        embed.set_footer(text=f"Requested by {user.name}")

    await ctx.send(embed=embed)




@bot.command(name='dm')
async def send_dm(ctx, user_id: int, *, message):
    with open('wl.txt', 'r') as file:
        whitelist = [line.strip() for line in file]

    if str(ctx.author.id) not in whitelist:
        embed = discord.Embed(
            title="Commands Panel",
            description=f"""`❌` **You are not authorized to use this command.**
            Contact a staff member to be `whitelist`.""",
            color=discord.Color(0x17004e)
        )

        if isinstance(ctx.author, discord.User):
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        elif isinstance(ctx.author, discord.Member):
            user = ctx.author
            avatar_url = user.avatar.url if user.avatar else user.default_avatar.url
            embed.set_thumbnail(url=avatar_url)
            embed.set_footer(text=f"Requested by {user.name}")

        await ctx.send(embed=embed)

        return
    try:
      
        user = bot.get_user(user_id)
        if user:
        
            await user.send(message)
            embed = discord.Embed(
                title="DM Command",
                description=f"""`✅` Message sent successfully to `{user.name}`!
**Message** : *{message}* """,
                color=discord.Color(0x17004e)
            )
            if isinstance(ctx.author, discord.User):
                embed.set_thumbnail(url=ctx.author.avatar_url)
                embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
            elif isinstance(ctx.author, discord.Member):
                user = ctx.author
                avatar_url = user.avatar.url if user.avatar else user.default_avatar.url
                embed.set_thumbnail(url=avatar_url)
                embed.set_footer(text=f"Requested by {user.name}")
            await ctx.send(embed=embed)
            print(Colorate.Horizontal(Colors.purple_to_blue, f"[+] Message sent to {user.name} | '{message}'"))
        else:     
            embed = discord.Embed(
                title="DM Command",
                description=f"""`❌` **Invalid user id...**
Try another id.""",
                color=discord.Color(0x17004e)
            )
            if isinstance(ctx.author, discord.User):
                embed.set_thumbnail(url=ctx.author.avatar_url)
                embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
            elif isinstance(ctx.author, discord.Member):
                user = ctx.author
                avatar_url = user.avatar.url if user.avatar else user.default_avatar.url
                embed.set_thumbnail(url=avatar_url)
                embed.set_footer(text=f"Requested by {user.name}")
            await ctx.send(embed=embed)
    except discord.Forbidden:
            embed = discord.Embed(
                title="DM Command",
                description=f"""`❌` **Permission denied...**
Make sure you have activated intents.""",
                color=discord.Color(0x17004e)
            )
            if isinstance(ctx.author, discord.User):
                embed.set_thumbnail(url=ctx.author.avatar_url)
                embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
            elif isinstance(ctx.author, discord.Member):
                user = ctx.author
                avatar_url = user.avatar.url if user.avatar else user.default_avatar.url
                embed.set_thumbnail(url=avatar_url)
                embed.set_footer(text=f"Requested by {user.name}")
            await ctx.send(embed=embed)
        

@bot.command(name='dmall')
async def send_dm_all(ctx, cooldown: int, target: str, *, message_content: str):
    with open('wl.txt', 'r') as file:
        whitelist = [line.strip() for line in file]

    if str(ctx.author.id) not in whitelist:
        embed = discord.Embed(
            title="Commands Panel",
            description=f"""`❌` **You are not authorized to use this command.**
            Contact a staff member to be `whitelist`.""",
            color=discord.Color(0x17004e)
        )

        if isinstance(ctx.author, discord.User):
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        elif isinstance(ctx.author, discord.Member):
            user = ctx.author
            avatar_url = user.avatar.url if user.avatar else user.default_avatar.url
            embed.set_thumbnail(url=avatar_url)
            embed.set_footer(text=f"Requested by {user.name}")

        await ctx.send(embed=embed)

        return
    if cooldown < 0 or cooldown > 3:
            embed = discord.Embed(
                title="DMall Command",
                description=f"""`❌` **The cooldown must be between `0` and `3`.**
Check the `cmd` commande for help.""",
                color=discord.Color(0x17004e)
            )
            if isinstance(ctx.author, discord.User):
                embed.set_thumbnail(url=ctx.author.avatar_url)
                embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
            elif isinstance(ctx.author, discord.Member):
                user = ctx.author
                avatar_url = user.avatar.url if user.avatar else user.default_avatar.url
                embed.set_thumbnail(url=avatar_url)
                embed.set_footer(text=f"Requested by {user.name}")
            await ctx.send(embed=embed)

            return

    valid_targets = ['all', 'off', 'on']
    if target not in valid_targets:
            embed = discord.Embed(
                title="DMall Command",
                description=f"""`❌` **The target must be `all`, `off` or `on`.**
Check the `cmd` commande for help.""",
                color=discord.Color(0x17004e)
            )
            if isinstance(ctx.author, discord.User):
                embed.set_thumbnail(url=ctx.author.avatar_url)
                embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
            elif isinstance(ctx.author, discord.Member):
                user = ctx.author
                avatar_url = user.avatar.url if user.avatar else user.default_avatar.url
                embed.set_thumbnail(url=avatar_url)
                embed.set_footer(text=f"Requested by {user.name}")
            await ctx.send(embed=embed)

            return

    success_count = 0
    failure_count = 0

    if target == 'all':
        members = ctx.guild.members
    elif target == 'off':
        members = [member for member in ctx.guild.members if member.status == discord.Status.offline and not member.bot]
    elif target == 'on':
        members = [member for member in ctx.guild.members if member.status in [discord.Status.online, discord.Status.dnd, discord.Status.idle] and not member.bot]

    for member in members:
        try:
            if not member.bot:
                await member.send(message_content)
                print(Colorate.Horizontal(Colors.purple_to_blue, f"[+] Message sent to {member.name} | '{message_content}'"))
                await asyncio.sleep(cooldown)
                success_count += 1
        except discord.Forbidden:
            print(Colorate.Horizontal(Colors.purple_to_blue, f"[-] Unable to send a message to {member.name}"))
            failure_count += 1

    embed = discord.Embed(
                title="DMall Command",
                description=f"""`✅` **DMall finished !**
I successfuly sended a message to `{success_count} users`.
I got `{failure_count} failure`.""",
                color=discord.Color(0x17004e)
            )
    if isinstance(ctx.author, discord.User):
                embed.set_thumbnail(url=ctx.author.avatar_url)
                embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
    elif isinstance(ctx.author, discord.Member):
                user = ctx.author
                avatar_url = user.avatar.url if user.avatar else user.default_avatar.url
                embed.set_thumbnail(url=avatar_url)
                embed.set_footer(text=f"Requested by {user.name}")
    await ctx.send(embed=embed)
    print(Colorate.Horizontal(Colors.purple_to_blue, f"[+] Successfuly sended {success_count} messages !"))
    print(Colorate.Horizontal(Colors.purple_to_blue, f"[-] Got {failure_count} failure"))


@bot.command(name='servers')
async def show_servers(ctx):
    with open('wl.txt', 'r') as file:
        whitelist = [line.strip() for line in file]

    if str(ctx.author.id) not in whitelist:
        embed = discord.Embed(
            title="Commands Panel",
            description=f"""`❌` **You are not authorized to use this command.**
            Contact a staff member to be `whitelist`.""",
            color=discord.Color(0x17004e)
        )

        if isinstance(ctx.author, discord.User):
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        elif isinstance(ctx.author, discord.Member):
            user = ctx.author
            avatar_url = user.avatar.url if user.avatar else user.default_avatar.url
            embed.set_thumbnail(url=avatar_url)
            embed.set_footer(text=f"Requested by {user.name}")

        await ctx.send(embed=embed)

        return
    guilds_info = []

    for guild in bot.guilds:
        members_count = len(guild.members)
        guild_info = {
            'name': guild.name,
            'id': guild.id,
            'members_count': members_count
        }
        guilds_info.append(guild_info)

    guilds_info.sort(key=lambda x: x['members_count'], reverse=True)

    embed = discord.Embed(
        title="Servers List",
        description="Here is the list of servers where I am present:",
        color=discord.Color(0x17004e)
    )

    for info in guilds_info:
        embed.add_field(
            name=f"- {info['name']} (ID: {info['id']})",
            value=f" - Members: {info['members_count']}",
            inline=False
        )

    if isinstance(ctx.author, discord.User):
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
    elif isinstance(ctx.author, discord.Member):
        user = ctx.author
        avatar_url = user.avatar.url if user.avatar else user.default_avatar.url
        embed.set_thumbnail(url=avatar_url)
        embed.set_footer(text=f"Requested by {user.name}")

    await ctx.send(embed=embed)

@bot.command(name='get')
async def get_server_invite(ctx, server_id: int):
    with open('wl.txt', 'r') as file:
        whitelist = [line.strip() for line in file]

    if str(ctx.author.id) not in whitelist:
        embed = discord.Embed(
            title="Commands Panel",
            description=f"""`❌` **You are not authorized to use this command.**
            Contact a staff member to be `whitelist`.""",
            color=discord.Color(0x17004e)
        )

        if isinstance(ctx.author, discord.User):
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        elif isinstance(ctx.author, discord.Member):
            user = ctx.author
            avatar_url = user.avatar.url if user.avatar else user.default_avatar.url
            embed.set_thumbnail(url=avatar_url)
            embed.set_footer(text=f"Requested by {user.name}")

        await ctx.send(embed=embed)
        return

    server = bot.get_guild(server_id)

    if server is None:
        embed = discord.Embed(
            title="Server Invite Manager",
            description=f"""`❌` **Server with ID `{server_id}` not found.**""",
            color=discord.Color(0x17004e)
        )

        if isinstance(ctx.author, discord.User):
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        elif isinstance(ctx.author, discord.Member):
            user = ctx.author
            avatar_url = user.avatar.url if user.avatar else user.default_avatar.url
            embed.set_thumbnail(url=avatar_url)
            embed.set_footer(text=f"Requested by {user.name}")

        await ctx.send(embed=embed)
        return

    invite = await server.text_channels[0].create_invite(max_uses=1, unique=True)

    embed = discord.Embed(
        title="Server Invite Manager",
        description=f"""`✅` **Here is the invitation to the server with ID `{server_id}`:**
{invite.url}""",
        color=discord.Color(0x17004e)
    )

    if isinstance(ctx.author, discord.User):
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
    elif isinstance(ctx.author, discord.Member):
        user = ctx.author
        avatar_url = user.avatar.url if user.avatar else user.default_avatar.url
        embed.set_thumbnail(url=avatar_url)
        embed.set_footer(text=f"Requested by {user.name}")

    await ctx.send(embed=embed)


bot.run(bot_token) 
