Client ID
697637033518170112

TOKEN
Njk3NjM3MDMzNTE4MTcwMTEy.Xo6MUw.L0oAey4WxplHX4-RQiGQQbAB4p0

https://discordapp.com/oauth2/authorize?client_id=697637033518170112&scope=bot

URL	DESCRIPTION
https://discordapp.com/api/oauth2/authorize?client_id=697637033518170112&scope=bot

##@client.event
##async def on_message(message):
    ## if I created this message, don't respond.
##    if message.author == client.user:
##        return

##    if message.content. == 'Common Sense!':
##        response = random.choice(brooklyn_99_quotes)
##        await message.channel.send(response)

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )






    @client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


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
        ]


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    print('happy birthday called')
    if 'happy birthday' in message.content.lower():
        await message.channel.send('Happy Birthday! 🎈🎉')
