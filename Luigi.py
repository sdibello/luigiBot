# Luigi-small.py
import os
import discord
import random
import json
import aiohttp 
import time
import logging
import sys
from dotenv import load_dotenv
from discord.ext import commands
from random import seed
from random import randint
from collections import namedtuple

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
DND_API_URL = os.getenv('DND_API_URL')
att_dict = {}
luigi_version = "1.0.1"

#client = discord.Client()
bot = commands.Bot(command_prefix='!')
#logging
root = logging.getLogger()
root.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

@bot.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, bot.guilds)
    root.info(f'{bot.user} is connected to the following guild:\n')
    root.info(f'{guild.name}(id: {guild.id})\n')
    root.info(f'discord version: {discord.__version__}')
    root.info("starting luigibot")
    root.info(f"version:{luigi_version}")

@bot.command(name='attack')
async def attack(ctx, *args):
    ## calculate attacks
    Attacks = namedtuple('Attacks', ['att', 'crit'])
    singleAttack = "" 
    millis = int(round(time.time() * 1000))
    id = ctx.author.id
    seed(millis+id)
    isCritical = ""
    a = Attacks(att=1, crit="20")
    if (len(args) == 0):
        a = att_dict[id]
    else:
        if (len(args) >= 1):
            a = Attacks(att=args[0], crit="20")
        if (len(args) >= 2):
            a = Attacks(att=args[0], crit=args[1])
        att_dict.update({id:a})

    user = ctx.author.name
    for attack in a.att.split(','):
        roll = randint(1, 20)
        critical = a.crit
        attack_bonus = int(attack) 
        total_val = roll + attack_bonus
        if (int(roll) >= int(critical)):
            millis = int(round(time.time() * 1000))
            seed(millis+id)
            criticalroll = randint(1, 20)
            isCritical = f" - CRITICAL - Confirm Roll ({criticalroll})"
        singleAttack = singleAttack + f"""({roll})+{attack_bonus} = {total_val} {isCritical}
        """
        isCritical = ""

    attackmessage = f"""
        >>>  attack for {user}
        {singleAttack} 
        """
    
    if (len(attackmessage)>2000):
        for chunk in chunks(attackmessage, 1975):
            if (chunk.find(">>>")>0):
                await ctx.send(chunk)
            else:
                await ctx.send(">>> " + chunk)
    else:
        await ctx.send(attackmessage)


@bot.command(name='xp')
async def xp(ctx, level):
        currentlevel = int(level)
        xpnewlevel = (currentlevel * (currentlevel+1)) * 1000 / 2
        await ctx.send(" level " + str(currentlevel+1) + " needs " + str(xpnewlevel))

@bot.command(name='list')
async def spells_by_class_and_level(ctx, *id):
    ## initialization variables
    url = 'http://localhost:5241/api/v1/Spells/{0}/{1}'.format(id[0], id[1])
    print (url)
    class_name = id[0]
    class_level = id[1]
    spell_name = ""
    spell_list = ""
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        for r in response:
            spell_name = r['spellName']
            spell_list = spell_list + f"{spell_name} - "

    search_spell = f"""
        >>> **{class_name}** spells for level {class_level}
        {spell_list}
        """
    if (len(search_spell)>2000):
        for chunk in chunks(search_spell, 1975):
            if (chunk.find(">>>")>0):
                await ctx.send(chunk)
            else:
                await ctx.send(">>> " + chunk)
        else:
            await ctx.send(search_spell)


@bot.command(name='feat')
async def feat(ctx, *id):
    ## initialization variables.
    fid = ""
    description = ""
    title = ""
    benefit = ""
    slug = ""
    s = " "
    if (len(id)>1):
        s = s.join(id)
    else:
        s = id[0]
    url = 'http://localhost:5241/api/v1/Feat/{0}'.format(s)
    print (url)
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        fid = response['id']
        description = response['description']
        title = response['name']
        benefit = response['benefit']
        slug = response['slug']


    url = 'http://localhost:5241/api/v1/Feat/{0}/requirement'.format(fid)
    print (url)
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        required_feats = "**Required Feats:** "
        required_feats_by = f"**Feats that require {title}:** "

        for r in response['requiredFeats']:
            featName = r['name']
            required_feats = required_feats + f"- {featName} "
        for r in response['featsRequiredBy']:
            featName = r['name']
            required_feats_by = required_feats_by + f"- {featName} "
        feat = f"""
            >>> __**{title}**__  ({slug})
            {description}
            **Benefit:** {benefit}
            {required_feats}
            {required_feats_by}
            """
        if (len(feat)>2000):
            for chunk in chunks(feat, 1975):
                if (chunk.find(">>>")>0):
                    await ctx.send(chunk)
                else:
                    await ctx.send(">>> " + chunk)
        else:
            await ctx.send(feat)

@bot.command(name='spell')
async def spell(ctx, *id):
    ## initialization variables.
    fid = ""
    description = ""
    title = ""
    castingTime = ""
    range = ""
    savingThrow = ""
    spellResistance = ""
    duration = ""
    target = ""
    slug = ""
    school = ""
    subschool = ""
    schoolOutput = ""
    s = " "
    if (len(id)>1):
        s = s.join(id)
    else:
        s = id[0]
    url = 'http://localhost:5241/api/v1/Spells/{0}'.format(s)
    print (url)
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        fid = response['id']

        if (fid==0):
            snarky_response = [
            'Yeah, I had an apprentice try that once.',
            'Cloud tried to pull that once with a Carne Pyre...',
            'Next time I see Russel.. i\'ll ask him what you mean.... ',
            'Spellcasting is like cooking, it\'s not just ingrediants mixed together..',
            ' I\'m too old for this shit..',
            ' Yeah, And i\'ve met Dedestroyt too .. ',
            ]
            randomrespone = random.choice(snarky_response)
            response['search']
            spelllist = ""
            for s in response['search']:
                spell = s['name']
                spelllist = spelllist + f"{spell}, "
            message = f"""
            >>> {randomrespone}
            Did you really mean one of these? - {spelllist}
            """
            if (len(message)>2000):
                for chunk in chunks(message, 1975):
                    if (chunk.find(">>>")>0):
                        await ctx.send(chunk)
                    else:
                        await ctx.send(">>> " + chunk)
                return
            else:
                await ctx.send(message)
                return
        
        description = response['description']
        title = response['name']
        castingTime = response['castingTime']
        range = response['range']
        savingThrow = response['savingThrow']
        spellResistance = response['spellResistance']
        duration = response['duration']
        target = response['target']
        slug = response['slug']

    ### add " school " to the spell response
    url = 'http://localhost:5241/api/v1/Spells/{0}/school'.format(fid)
    print (url)
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        for r in response:
            school = r['schoolName']
            ##subschool = r['subSchoolName']
        if (school != None):
            if (len(school)>0):
                schoolOutput = f"[{school}]"
                if (subschool != None):
                    if (len(subschool)>0):
                        schoolOutput = f"[{school}]({subschool})"

    ### add class who can cast the spell to the response
    url = 'http://localhost:5241/api/v1/Spells/{0}/class'.format(fid)
    print (url)
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        message = "**Class:** "
        for r in response:
            classname = r['className']
            level = r['level']
            message = message + f"{classname}({level}) "
        spell = f"""
            >>> __**{title}**__  {schoolOutput}
            {description}
            **Casting Time:** {castingTime}
            **Saving Throw:** {savingThrow}
            **Spell Resistance** {spellResistance}
            **Duration:** {duration} 
            **Target** {target}
            **Range** {range}
            {message}
            """
        if (len(spell)>2000):
            for chunk in chunks(spell, 1975):
                if (chunk.find(">>>")>0):
                    await ctx.send(chunk)
                else:
                    await ctx.send(">>> " + chunk)
        else:
            await ctx.send(spell)

def chunks(s, n):
    for start in range(0, len(s), n):
        yield s[start:start+n]

@bot.command(name='dbcs')
async def common_sense(ctx):
    book_of_common_sense = [
        'Don\'t die.  It\'s bad for your career.',
        'Don\'t run naked after ogre magi.',
        'Don\'t associate with gnomes.',
        'Don\'t associate with Bards, especially Gallants and Gypsies',
        'Frequent establishments run by Halfling Chefs',
        'DO NOT associate with megalomaniac psions. Ever',
        'Don\'t associate with Elven bounty hunters- their motivations are never what you expect.',
        'Don\'t mention marriage or paternity to unmarried nobles with children.',
        'Don\'t bother cleaver wielding Halfling chefs',
        'Don\'t ask gnomes to change an infant\'s diapers.  Even if they\'re the parent',
        'DO NOT CHARGE DOGGEDENS! Or associate with those that do.',
        'DO NOT CHARGE Kaldur Deth! Or associate with those that do.',
        'Avoid Gnomish magical warehouses.',
        'Avoid Gnomish conga lines- stay away, as far away as you can.',
        'DO NOT ENCOURAGE THE GNOME!',
        'Associating with Cavalier types (Paladins, Eshalmon, Gallants etc) is hazardous.',
        'DO NOT ENTER MIND FLAYER CITIES OF YOUR OWN FREE WILL',
        'Beholders Suck',
        'The Underdark and everything in it sucks.',
        'Leave mysterious albino elves and their cities where you find them',
        'Let sleeping mutant bats lie (especially when they outnumber you 100 to 1)',
        'When underground, defer to the Dwarf.',
        'Don\'t store the Vampire with the corpse.',
        'Beware of smart gnomes, intelligence is inversely proportional to common sense.',
        'Don\'t get within sighting of a tinker.',
        'When (not if) the Tinker says OOPS, run.  Fast.  Teleport if possible',
        'You occasionally have to tempt fate.  Only occasionally',
        '200 Ogres, with or without the 25 ogre magi thrown in for good measure is 200 to many.',
        'Never leave home without the elven archer',
        'Leave magic to the wizard!!!',
        'Lead, rune covered tunnels most likely lead to your own destruction.',
        'Obsidian, rune covered doors most likely lead to your own destruction.',
        'When on the outer planes, don\'t drink the water',
        'Always start on the right',
        'When about to voluntarily enter a lower plane ask: do I really want to do this? Really?',
        'Don\'t touch the fiends',
        'Anyone who goes into battle with gnome designed weapons has already lost',
        'The vastness of space just means there\'s more room to get into trouble',
        'People who worship death are low on the common sense scale.',
        'If you are going to challenge the Orc with the 8\' hekuta you had better be that good',
        'Honor and common sense often conflict, except in extreme situations common sense comes first.',
        'NEVER set foot aboard a Gnomish spelljammer ship',
        'You\'ve never seen it all',
        'There is no such thing as overkill',
        'Ask a stupid question get a stupid answer',
        'Timing is everything ',
        'If it\'s free it\'s crap.  If they\'ll work for free don\'t trust them.',
        'Do not contradict the powers. E.g. do not raise your voice to Behamut.',
        'When trying to protect someone don\'t take them to the Abyss',
        'If the worst thing you encounter in the Abyss is a drunken snake, count yourself lucky',
        'Friends don\'t leave dead friends hanging, i.e. in the lower planes',
        'Don\'t quibble over semantics',
        'Let Sleeping Trolls lie',
        '"The ones who speak Gnomish are the Gnomes."\n -  Luthien attempting to ferret out enemies amidst a group',
        '"What sort of parents did you have?  I have excellent parents.  I have stupid siblings."\n -  Wallace Toppin to Calvin Trueheart as his sister Allyson and brother charged a Doggeden',
        '"Don\'t firestorm the fire giants.  It won\'t work"\n -  Attilla Fellows to Katrina',
        '"I\'ve come across some terrible contradictions in my life Gallant Bard is among the worst."\n -  Sanine upon meeting Allyson Trueheart',
        '"I did bad didn\'t I?"\n -   Katrina having just cast a powerful necromancy spell at her undead opponent',
        '"Things were going well until you showed up.  Really define going well?  Alive, uncaptured and not about to be sacrificed to a demon prince.  He\'s got you there Luigi."\n -   Escalon the Arrow to Luigi Wonderword. Response by Cloud.',
        '"Where gnomes are concerned I don\'t ask"\n - Rampart',
        '"The dead are not tough"\n - Borkon the Rusted\'s response to Allyson Trueheart when informed he was about to be surrounded by an Orcish legion',
        '"Won\'t that burn down the forest?  Bah!  The blood puts it out!\n -  Katrina to Korus before unleashing an augmented delayed blast fireball.',
        '"What was your grandfather\'s name?", "Um….er….I don\'t remember", "Wait, aren’t you Claude Greymander the 3rd?\n -  Claude and Daane talking about Claude’s past',
        'Don\'t enter tombs (Borkons) that require Kobald castrations',
        'Tombs full of hanging balls sacks are not safe',
        'But it\'s a Trumpet Archon, it\'s immune to poison',
        'Don\'t leave the golembane weapons at home if you\'re headed to the Plateau looking for trouble.\n On second thought, never leave the golembane weapons at home.'
        ]
    response = random.choice(book_of_common_sense)
    comment = f"""
    >>> {response} 
    """
    await ctx.send(comment)

bot.run(TOKEN)