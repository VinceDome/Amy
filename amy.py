import os, discord, time, datetime, random, asyncio, math, sys

from discord.ext import commands, tasks
from discord.utils import get


path_to_tokenL = os.getcwd().split("\\")
if len path_to_tokenL = 1:
    path_to_tokenL = os.getcwsd().split("/")
del path_to_tokenL[len(path_to_tokenL)-1]

sys.path.append("/".join(path_to_tokenL))
from amy_token import *




client = commands.Bot(command_prefix=",", case_insensitive = True)
client.remove_command("help")
bugs = open(os.getcwd()+"/amy/bugs.txt", "r", encoding="utf-8")
bugL = bugs.read().split("%%%")
bugs.close()

suggestions = open(os.getcwd()+"/amy/suggestions.txt", "r", encoding="utf-8")
suggestL = suggestions.read().split("%%%")
suggestions.close()


for i in bugL:
    if i == "":
        bugL.remove(i)

for i in suggestL:
    if i == "":
        suggestL.remove(i)
theme = 000000

def tobool(boolean):
    if boolean == "True":
        return True
    elif boolean == "False":
        return False

testingF = open(os.getcwd()+"/amy/testing.txt", "r", encoding="utf-8")
testing_mode = tobool(testingF.read().rstrip("\n"))
testingF.close()


@client.event
async def on_ready():
    print(f'{client.user} activated!')
    global bot_commands, dev_role, amevend, admin_role, amy_color

    if not testing_mode:
        activity = discord.Activity(type=discord.ActivityType.watching, name=",help")
        #activity = discord.Game(name="Waxination", type=3)
        await client.change_presence(status=discord.Status.online, activity=activity)
    else:
        activity = discord.Game(name="Testing mode, use with caution!", type=3)
        await client.change_presence(status=discord.Status.dnd, activity=activity)

    bot_commands = client.get_channel(856535768821268550)
    amevend = client.get_guild(856529447980236841)
    dev_role = get(amevend.roles, id=856531147521261628)
    admin_role = get(amevend.roles, id=856530763667603467)
    amy_color = get(amevend.roles, id=860969111629725747)
    await bot_commands.purge(limit=1000)
    
    
    
    #await general.send("Felkeltem! :)")

#region help

@client.command()
async def help(ctx, *, command=None):
    embed = discord.Embed(title="Help", description = "Please enter a valid command!", color=theme)
    


    if command != None:
        commandL = command.split(" ")
        if commandL[0] == "bugreport" or commandL[0] == "bug" or commandL[0] == "report":
            embed = discord.Embed(title="***,bugreport***", color=theme)
            
            embed.add_field(name = "**Usage**", value = f"Report a bug for any Amevend game, or for {client.user.mention} itself!", inline = False)
            embed.add_field(name = "**Aliases**", value = f"[bugreport, bug, report]", inline = False)
            embed.add_field(name = "**Syntax ( [] = required, <> = optional )**", value=",bugreport [title] | [platform] | [bug description] | [bug reproduction] | <extra notes>", inline = False)
            

        elif commandL[0] == "ping":
            embed = discord.Embed(title="***,ping***", color=theme)
            
            embed.add_field(name = "**Usage**", value = f"See the client delay!", inline = False)
            embed.add_field(name = "**Aliases**", value = f"[ping]", inline = False)
            embed.add_field(name = "**Syntax ( [] = required, <> = optional )**", value=",ping", inline = False)
            

        elif commandL[0] == "suggestion" or commandL[0] == "sug" or commandL[0] == "suggest":
            embed = discord.Embed(title="***,bugreport***", color=theme)
            
            embed.add_field(name = "**Usage**", value = f"Send a suggestion for any Amevend game, the discord server or for {client.user.mention} itself!", inline = False)
            embed.add_field(name = "**Aliases**", value = f"[suggestion, suggest, sug]", inline = False)
            embed.add_field(name = "**Syntax ( [] = required, <> = optional )**", value=",suggestion [title] | [platform] | [suggestion] | <extra notes>", inline = False)
            

        elif commandL[0] == "links":
            embed = discord.Embed(title="***,links***", color=theme)
            
            embed.add_field(name = "**Usage**", value = f"See the important links and contact information of the Amevend team!", inline = False)
            embed.add_field(name = "**Aliases**", value = f"[links]", inline = False)
            embed.add_field(name = "**Syntax ( [] = required, <> = optional )**", value=",links", inline = False)
           

        elif commandL[0] == "me":
            await ctx.send("well")
            await asyncio.sleep(2)
            await ctx.send("no")
            

        
        if commandL[0] == "admin":
            if not dev_role in ctx.author.roles and not admin_role in ctx.author.roles:
                return None
            if len(commandL) == 1:
                embed = discord.Embed(title="***Admin Help***", description="Type ,help admin [command] to get more information on it!", color=theme)
        
                embed.add_field(name = ",approve", value = f"Approve a bugreport or suggestion", inline = False)
                embed.add_field(name = ",deny", value = f"Deny a bugreport or suggestion", inline = False)

                embed.add_field(name = ",bugreports", value = f"View the active bugreports", inline = False)
                embed.add_field(name = ",suggestions", value = f"View the active suggestions", inline = False)
                embed.add_field(name = ",archived", value = f"View the archived bugreports and suggestions", inline = False)

                embed.add_field(name = ",clear", value = f"Clear an amount of messages", inline = False)
                embed.add_field(name = ",crash", value = f"Crash Amy (only <@!810910872792596550> can use it)", inline = False)
                embed.add_field(name = ",speak", value = f"Get Amy to say whatever you want (only <@!810910872792596550> can use it)", inline = False)
            else:
                if commandL[1] == "approve":
                    embed = discord.Embed(title="***,approve***", color=theme)
            
                    embed.add_field(name = "**Usage**", value = f"Approve a bugreport or suggestion", inline = False)
                    embed.add_field(name = "**Aliases**", value = f"[approve]", inline = False)
                    embed.add_field(name = "**Syntax ( [] = required, <> = optional )**", value=",approve [bug/sug (every alias is accepted)] [index of bug or sug] [message to the subbmitter]", inline = False)
                
                elif commandL[1] == "deny":
                    embed = discord.Embed(title="***,deny***", color=theme)
            
                    embed.add_field(name = "**Usage**", value = f"Deny a bugreport or suggestion", inline = False)
                    embed.add_field(name = "**Aliases**", value = f"[deny]", inline = False)
                    embed.add_field(name = "**Syntax ( [] = required, <> = optional )**", value=",deny [bug/sug (every alias is accepted)] [index of bug or sug] [message to the subbmitter]", inline = False)
                
                elif commandL[1] == "bugreports" or commandL[1] == "bugs" or commandL[1] == "reports":
                    embed = discord.Embed(title="***,bugreports***", color=theme)
            
                    embed.add_field(name = "**Usage**", value = f"View the current bugreports", inline = False)
                    embed.add_field(name = "**Aliases**", value = f"[bugreports, bugs, reports]", inline = False)
                    embed.add_field(name = "**Syntax ( [] = required, <> = optional )**", value=",bugreports <index of bug>", inline = False)      

                elif commandL[1] == "suggestions" or commandL[1] == "sugs" or commandL[1] == "suggests":
                    embed = discord.Embed(title="***,suggestions***", color=theme)
            
                    embed.add_field(name = "**Usage**", value = f"View the current suggestions", inline = False)
                    embed.add_field(name = "**Aliases**", value = f"[suggestions, sugs, suggests]", inline = False)
                    embed.add_field(name = "**Syntax ( [] = required, <> = optional )**", value=",suggestions <index of sug>", inline = False) 

                elif commandL[1] == "archived":
                    embed = discord.Embed(title="***,archived***", color=theme)
            
                    embed.add_field(name = "**Usage**", value = f"View the archived bugreports and suggestions", inline = False)
                    embed.add_field(name = "**Aliases**", value = f"[archived]", inline = False)
                    embed.add_field(name = "**Syntax ( [] = required, <> = optional )**", value=",archived", inline = False)

                elif commandL[1] == "clear" or commandL[1] == "c":
                    embed = discord.Embed(title="***,clear***", color=theme)
            
                    embed.add_field(name = "**Usage**", value = f"Clear an amount of messages", inline = False)
                    embed.add_field(name = "**Aliases**", value = f"[clear, c]", inline = False)
                    embed.add_field(name = "**Syntax ( [] = required, <> = optional )**", value=",clear [amount of messages]", inline = False) 
    
                elif commandL[1] == "crash":
                    embed = discord.Embed(title="***,crash***", color=theme)
            
                    embed.add_field(name = "**Usage**", value = f"Crash Amy (only <@!810910872792596550> can use it)", inline = False)
                    embed.add_field(name = "**Aliases**", value = f"[crash]", inline = False)
                    embed.add_field(name = "**Syntax ( [] = required, <> = optional )**", value=",crash", inline = False) 

                elif commandL[1] == "speak" or commandL[1] == "s":
                    embed = discord.Embed(title="***,speak***", color=theme)
            
                    embed.add_field(name = "**Usage**", value = f"Get Amy to say whatever you want (only <@!810910872792596550> can use it)", inline = False)
                    embed.add_field(name = "**Aliases**", value = f"[speak, s]", inline = False)
                    embed.add_field(name = "**Syntax ( [] = required, <> = optional )**", value=",speak [message]", inline = False) 
    else:
        embed = discord.Embed(title="***Help***", description="Type ,help [command] to get more information on it!", color=theme)
        
        embed.add_field(name = ",ping", value = f"See the client delay!", inline = False)
        embed.add_field(name = ",bugreport", value = f"Report a bug for any Amevend game, or for {client.user.mention} itself!", inline = False)
        embed.add_field(name = ",suggestion", value = f"Send a suggestion for any Amevend game, the discord server or for {client.user.mention} itself!", inline = False)
        embed.add_field(name = ",links", value = f"See the important links and contact information of the Amevend team!", inline = False)

    await ctx.send(embed = embed)


#endregion


#region commands

@client.command()
async def ping(ctx):
    await ctx.send(f"pong ({round(client.latency*1000)}ms)")

@client.command()
async def links(ctx):
    embed = discord.Embed(title=f"***Important links and contact information***", description = f"""Our games, email adress, itch.io page ect.""", color=theme)
    embed.add_field(name = "Amy source code", value = "https://github.com/VinceDome/Amy")
    embed.add_field(name = f"Waxination", value="https://tesztalany370.itch.io/waxination", inline = False)
    embed.add_field(name = f"StoMech", value="https://tesztalany370.itch.io/stomech", inline = False)
    embed.add_field(name = f"itch.io page", value="https://tesztalany370.itch.io/", inline = False)
    embed.add_field(name = f"Email", value="amevend@gmail.com", inline = False)
    await ctx.send(embed = embed)

@client.command()
async def crash(ctx):
    if ctx.author.id == 810910872792596550:
        await ctx.send("crash")
        exit()

@client.command(aliases=["bug", "report"])
async def bugreport(ctx, *, args=None):
    global bugL
    if args == None:
        await ctx.send("enter all parameters <:kekw:856936897698856970>")
        return None
    try:
        argsL = args.split(" | ")
        title = argsL[0]
        platform = argsL[1]
        whatbug = argsL[2]
        howto = argsL[3]
    except IndexError:
        await ctx.send("enter all parameters <:kekw:856936897698856970>")
    try:
        extra_notes = argsL[4] 
    except IndexError:
        extra_notes = "[None]"
        pass
    bugs = open(os.getcwd()+"/amy/bugs.txt", "a+", encoding="utf-8")
    bugs.write(f"%%%\n{title}\n{platform}\n{whatbug}\n{howto}\n{extra_notes}\n{ctx.author.id}\n")
    bugs.close()

    bugs = open(os.getcwd()+"/amy/bugs.txt", "r", encoding="utf-8")
    bugL = bugs.read().split("%%%")
    for i in bugL:
        if i == "":
            bugL.remove(i)

    embed = discord.Embed(title="***Bug succesfully submitted***", description = "Your bug has been sent to the devs! It's only a matter of time now...", color=theme)
    embed.add_field(name = "**Title**", value=title)
    embed.add_field(name = "**Platform:**", value=platform, inline=False)
    embed.add_field(name = "**Describe the bug**", value=whatbug, inline=False)
    embed.add_field(name = "**How to reproduce the bug?**", value=howto, inline=False)
    embed.add_field(name = "**Extra notes:**", value=extra_notes, inline=False)
    await ctx.send(embed = embed)  

@client.command(aliases=["bugs", "reports"])
async def bugreports(ctx, selected=None):
    global bugL, dev_role
    if not dev_role in ctx.author.roles:
        return None
    embed = discord.Embed(title="***Current bugreports***", description = "All the unnaproved bugreports", color=theme)
    title = False
    if selected == None:
        for i in bugL:
            if i == "":
                bugL.remove(i)
                break
            details = i.split("\n")
            for a in details:
                if a == "":
                    details.remove(a)
            title = details[0]
            platform = details[1]
            embed.add_field(name = f"[{bugL.index(i)+1}] {title}", value=f"**In:** *{platform}*", inline = False)
        if title == False:
            embed.add_field(name = "No bugreports", value = "There are no current bugreports, you can rest dev! :)")
    else:
        try:
            bugDetails = bugL[int(selected)-1].split("\n")
            for i in bugDetails:
                if i == "":
                    bugDetails.remove(i)
        except (ValueError, IndexError):
            await ctx.send("You have to provide a valid report number!")

        title = bugDetails[0]
        platform = bugDetails[1]
        whatbug = bugDetails[2]
        howto = bugDetails[3]
        extra_notes = bugDetails[4]
        author_id = bugDetails[5]

        embed = discord.Embed(title=f"***Viewing bug [{selected}]***", description = f"You are currently viewing bugreport index ***[{selected}]***, submitted by <@!{author_id}>", color=theme)
        embed.add_field(name = "**Title**", value=title)
        embed.add_field(name = "**Platform:**", value=platform, inline=False)
        embed.add_field(name = "**Describe the bug**", value=whatbug, inline=False)
        embed.add_field(name = "**How to reproduce the bug?**", value=howto, inline=False)
        embed.add_field(name = "**Extra notes:**", value=extra_notes, inline=False)
    
    await ctx.send(embed = embed)


@client.command(aliases=["suggest", "sug"])
async def suggestion(ctx, *, args=None):
    global suggestL
    if args == None:
        await ctx.send("enter all parameters <:kekw:856936897698856970>")
        return None
    try:
        argsL = args.split(" | ")
        title = argsL[0]
        platform = argsL[1]
        whatsuggest = argsL[2]
    except IndexError:
        await ctx.send("enter all parameters <:kekw:856936897698856970>")
    try:
        extra_notes = argsL[3] 
    except IndexError:
        extra_notes = "[None]"
        pass
    suggestions = open(os.getcwd()+"/amy/suggestions.txt", "a+", encoding="utf-8")
    suggestions.write(f"%%%\n{title}\n{platform}\n{whatsuggest}\n{extra_notes}\n{ctx.author.id}\n")
    suggestions.close()

    suggestions = open(os.getcwd()+"/amy/suggestions.txt", "r", encoding="utf-8")
    suggestL = suggestions.read().split("%%%")
    for i in suggestL:
        if i == "":
            suggestL.remove(i)

    embed = discord.Embed(title="***Suggestion succesfully submitted***", description = "Your suggestion has been sent to the devs! It's only a matter of time now...", color=theme)
    embed.add_field(name = "**Title**", value=title)
    embed.add_field(name = "**Platform**", value=platform, inline=False)
    embed.add_field(name = "**What is your suggestion?**", value=whatsuggest, inline=False)
    embed.add_field(name = "**Extra notes:**", value=extra_notes, inline=False)
    await ctx.send(embed = embed)  

@client.command(aliases=["suggests", "sugs"])
async def suggestions(ctx, selected=None):
    global suggestL
    if not dev_role in ctx.author.roles:
        return None
    embed = discord.Embed(title="***Current suggestions***", description = "All the unnaproved suggestions", color=theme)
    title = False
    if selected == None:
        for i in suggestL:
            if i == "":
                suggestL.remove(i)
                break
            details = i.split("\n")
            for a in details:
                if a == "":
                    details.remove(a)
            title = details[0]
            platform = details[1]
            embed.add_field(name = f"[{suggestL.index(i)+1}] {title}", value=f"**For:** *{platform}*", inline = False)
        if title == False:
            embed.add_field(name = "No suggestions", value = "There are no current suggestions, you can rest dev! :)")
    else:
        try:
            suggestDetails = suggestL[int(selected)-1].split("\n")
            for i in suggestDetails:
                if i == "":
                    suggestDetails.remove(i)
        except (ValueError, IndexError):
            await ctx.send("You have to provide a valid report number!")

        title = suggestDetails[0]
        platform = suggestDetails[1]
        whatsuggest = suggestDetails[2]
        extra_notes = suggestDetails[3]
        author_id = suggestDetails[4]

        embed = discord.Embed(title=f"***Viewing suggestion [{selected}]***", description = f"You are currently viewing suggestion index ***[{selected}]***, submitted by <@!{author_id}>", color=theme)
        embed.add_field(name = "**Title**", value=title)
        embed.add_field(name = "**Platform:**", value=platform, inline=False)
        embed.add_field(name = "**What is your suggestion?**", value=whatsuggest, inline=False)
        embed.add_field(name = "**Extra notes:**", value=extra_notes, inline=False)
    
    await ctx.send(embed = embed)

@client.command(aliases=["szpík", "s"])
async def speak(ctx, *args):
    if ctx.author.id == 810910872792596550:
        await ctx.message.delete()
        await ctx.send(" ".join(args))

@client.command(aliases=["c"])
async def clear(ctx, msgs):
    try:
        await ctx.channel.purge(limit=int(msgs)+1)
    except ValueError:
        await ctx.send("Please enter a number! ")

@client.command()
async def approve(ctx, report_type=None, number=None, *, dm=None):
    if not dev_role in ctx.author.roles:
        return None

    if report_type == None or dm == None or number == None:
        await ctx.send("enter all parameters <:kekw:856936897698856970>")
        return None
    try:
        number = int(number)
    except ValueError:
        await ctx.send("enter all parameters <:kekw:856936897698856970>")
        return None 

    if report_type == "bugreport" or report_type == "bug":
        bugDetails = bugL[number-1].split("\n")
        for i in bugDetails:
            if i == "":
                bugDetails.remove(i)
        
    
        title = bugDetails[0]
        op_id = bugDetails[5]

        #elküldi dm-be:
        op_user = await client.fetch_user(int(op_id))
        msg_dm = await op_user.create_dm()
        
        embed = discord.Embed(title=f"***Bugreport approved***", description = f"""Your bugreport titled: "{title}" was approved by {ctx.author.mention}""", color=theme)
        embed.add_field(name = f"Here's the message from them:", value=dm)
        await msg_dm.send(embed = embed)
        #elküldi a channelbe
        
        
        embed = discord.Embed(title=f"***Approved bugreport [{number}]***", description = f"""You approved the bugreport titled: "{title}", submitted by {op_user.mention}""", color=theme)
        embed.add_field(name = f"Here's what I sent to the submitter:", value=dm)
        await ctx.send(embed = embed)

        #fájlt átírja
        del bugL[number-1]
        os.remove(os.getcwd()+"/amy/bugs.txt")

        bugs = open(os.getcwd()+"/amy/bugs.txt", "a+", encoding="utf-8")
        for i in bugL:
            bugs.write(f"%%%\n{i[0]}\n{i[1]}\n{i[2]}\n{i[3]}\n{i[4]}\n{i[5]}\n")
        bugs.close()

    elif report_type == "suggestion" or report_type == "sug":
        suggestDetails = suggestL[number-1].split("\n")
        for i in suggestDetails:
            if i == "":
                suggestDetails.remove(i)
        
    
        title = suggestDetails[0]
        op_id = suggestDetails[4]

        #elküldi dm-be:
        op_user = await client.fetch_user(int(op_id))
        msg_dm = await op_user.create_dm()
        embed = discord.Embed(title=f"***Suggestion approved***", description = f"""Your suggestion titled: "{title}" was approved by {ctx.author.mention}""", color=theme)
        embed.add_field(name = f"Here's the message from them:", value=dm)
        await msg_dm.send(embed = embed)


        #elküldi a channelbe        
        embed = discord.Embed(title=f"***Approved suggestion [{number}]***", description = f"""You approved the suggestion titled: "{title}", submitted by {op_user.mention}""", color=theme)
        embed.add_field(name = f"Here's what I sent to the submitter:", value=dm)
        await ctx.send(embed = embed)

        #fájlt átírja
        del suggestL[number-1]
        os.remove(os.getcwd()+"/amy/suggestions.txt")

        suggestions = open(os.getcwd()+"/amy/suggestions.txt", "a+", encoding="utf-8")
    
        for i in suggestL:
            suggestions.write(f"%%%\n{i[0]}\n{i[1]}\n{i[2]}\n{i[3]}\n{i[4]}\n")
        suggestions.close()

        #elmenti for later
        archived = open(os.getcwd()+"/amy/archived.txt", "a+", encoding="utf-8")
        archived.write(f"%%%\nsuggestion, approved\n{suggestDetails[0]}\n{suggestDetails[1]}\n{suggestDetails[2]}\n{suggestDetails[3]}\n{op_user}, id={op_user.id}\n")
        archived.close()

@client.command()
async def deny(ctx, report_type=None, number=None, *, dm=None):
    if not dev_role in ctx.author.roles:
        return None

    if report_type == None or dm == None or number == None:
        await ctx.send("enter all parameters <:kekw:856936897698856970>")
        return None
    try:
        number = int(number)
    except ValueError:
        await ctx.send("enter all parameters <:kekw:856936897698856970>")
        return None 

    if report_type == "bugreport" or report_type == "bug":
        bugDetails = bugL[number-1].split("\n")
        for i in bugDetails:
            if i == "":
                bugDetails.remove(i)
        
    
        title = bugDetails[0]
        op_id = bugDetails[5]

        #elküldi dm-be:
        op_user = await client.fetch_user(int(op_id))
        msg_dm = await op_user.create_dm()
        embed = discord.Embed(title=f"***Bugreport denied***", description = f"""Your bugreport titled: "{title}" was denied by {ctx.author.mention}""", color=theme)
        embed.add_field(name = f"Here's the message from them:", value=dm)
        await msg_dm.send(embed = embed)


        #elküldi a channelbe
        embed = discord.Embed(title=f"***Denied bug [{number}]***", description = f"""You denied the bug titled: "{title}", submitted by {op_user.mention}""", color=theme)
        embed.add_field(name = f"Here's what I sent to the submitter:", value=dm)
    
        await ctx.send(embed = embed)
        #fájlt átírja
        del bugL[number-1]
        os.remove(os.getcwd()+"/amy/bugs.txt")

        bugs = open(os.getcwd()+"/amy/bugs.txt", "a+", encoding="utf-8")
        
        
        for i in bugL:
            bugs.write(f"%%%\n{i[0]}\n{i[1]}\n{i[2]}\n{i[3]}\n{i[4]}\n{i[5]}\n")
        bugs.close()

    elif report_type == "suggestion" or report_type == "sug":
        suggestDetails = suggestL[number-1].split("\n")
        for i in suggestDetails:
            if i == "":
                suggestDetails.remove(i)
        
    
        title = suggestDetails[0]
        op_id = suggestDetails[4]

        #elküldi dm-be:
        op_user = await client.fetch_user(int(op_id))
        msg_dm = await op_user.create_dm()
        embed = discord.Embed(title=f"***Suggestion denied***", description = f"""Your suggestion titled: "{title}" was denied by {ctx.author.mention}""", color=theme)
        embed.add_field(name = f"Here's the message from them:", value=dm)
        await msg_dm.send(embed = embed)
        #elküldi a channelbe
        
        embed = discord.Embed(title=f"***Denied suggestion [{number}]***", description = f"""You denied the suggestion titled: "{title}", submitted by {op_user.mention}""", color=theme)
        embed.add_field(name = f"Here's what I sent to the submitter:", value=dm)
        await ctx.send(embed = embed)
        #fájlt átírja
        del suggestL[number-1]
        os.remove(os.getcwd()+"/amy/suggestions.txt")

        suggestions = open(os.getcwd()+"/amy/suggestions.txt", "a+", encoding="utf-8")
    
        for i in suggestL:
            suggestions.write(f"%%%\n{i[0]}\n{i[1]}\n{i[2]}\n{i[3]}\n{i[4]}\n")
        suggestions.close()      

@client.command()
async def testing(ctx):
    global testing_mode
    if ctx.author.id == 810910872792596550:
        testing_mode = not testing_mode
        os.remove(os.getcwd()+"/amy/testing.txt")
        testingF = open(os.getcwd()+"/amy/testing.txt", "a+", encoding="utf-8")
        testingF.write(str(testing_mode))
        testingF.close()

        if not testing_mode:
            activity = discord.Game(name="Waxination", type=3)
            await client.change_presence(status=discord.Status.online, activity=activity)
        else:
            activity = discord.Game(name="Testing mode, use with caution!", type=3)
            await client.change_presence(status=discord.Status.dnd, activity=activity)

        await ctx.send(f"Changed testing mode to [{testing_mode}]")

@client.command(aliases = ["archived"])
async def _archived(ctx):
    if not dev_role in ctx.author.roles:
        return None
    await ctx.send(file=discord.File(os.getcwd()+"/amy/archived.txt"))

@client.command(aliases = ["color"])
async def _color(ctx, color):
    global theme
    if not dev_role in ctx.author.roles:
        return None

    
    if len(list(str(color))) == 6:
    
        try:
            color = int(color)
        except ValueError:
            await ctx.send("I need a number")
            return None
        theme = color
        await amy_color.edit(colour=theme)
#endregion


@client.event
async def on_message(message):
    
    await client.process_commands(message)
    
    if message.channel.id == 856535768821268550:
        print(f"""{message.author} in {message.guild} #{message.channel} sent "{message.content}" """)
        await asyncio.sleep(60)
        await message.delete()
        return None
    
    if message.author == client.user:
        return None

    print(f"""{message.author} in {message.guild} #{message.channel} sent "{message.content}" """)



    
    



client.run(amy_token)