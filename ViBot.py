import discord
from discord.utils import get
from discord.ext import commands
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
nltk.download('punkt')
nltk.download('wordnet')
import pyodbc
import random
from decouple import config

client = commands.Bot(command_prefix = 'v!', help_command=None)
TOKEN = config('TOKEN')

gloomyList = [
    ["https://www.youtube.com/watch?v=w5_X-QFwmoo", "Epiphany", "BTS"],
    ["https://www.youtube.com/watch?v=AG-erEMhumc", "you broke me first", "Tate McRae"],
    ["https://www.youtube.com/watch?v=EtLtZoCwquw", "I hate u I love u", "gnash, Olivia O'Brien"],
    ["https://www.youtube.com/watch?v=RqcjBLMaWCg", "2U", "David Guetta, Justin Bieber"],
    ["https://www.youtube.com/watch?v=2tJjplMngFE", "princess don’t cry", "Carys"],
    ["https://www.youtube.com/watch?v=4vzJA0nWF1g", "lost boy", "Ruth. B"],
    ["https://www.youtube.com/watch?v=h9hdorPqukU", "if you", "BIGBANG"],
    ["https://www.youtube.com/watch?v=tscMSXk_jaQ", "if we have each other", "Alec Benjamin"],
    ["https://www.youtube.com/watch?v=pBET-22qits", "six feet apart", "Alec Benjamin"],
    ["https://www.youtube.com/watch?v=Xc695u4RFeI", "dangerously", "Charlie Puth"],
    ["https://www.youtube.com/watch?v=v-FVihIlU2g", "as long as you love me", "Backstreet Boys"],
    ["https://www.youtube.com/watch?v=BwcFtiIPogo", "how miserable do I have to be before you’re happy", "Beowulf"],
    ["https://www.youtube.com/watch?v=L7mfjvdnPno", "falling", "Trevor Daniel"],
    ["https://www.youtube.com/watch?v=AddwSHpQuSM", "superficial love", "Ruth B."],
    ["https://www.youtube.com/watch?v=VjSmpJDhF0U", "complicated", "Olivia O'Brien"],
    ["https://www.youtube.com/watch?v=ZzUbjigZTpM", "selfish", "Madison Beer"],
    ["https://www.youtube.com/watch?v=0TSxB_Tb2F0", "sweater weather", "The Neighbourhood Covered by Max and Alyston Stoner"],
    ["https://www.youtube.com/watch?v=dMEF8Olrvyc", "superhero", "Hard"],
    ["https://www.youtube.com/watch?v=0XRx5Jwjp4k", "wait wait wait", "Kun"],
    ["https://www.youtube.com/watch?v=jhVc-phLHJA", "one day", "Tate McRae"]
]

sadList = [
    ["https://www.youtube.com/watch?v=iWZmdoY1aTE", "happier", "Ed Sheeran "],
    ["https://www.youtube.com/watch?v=KRaWnd3LJfs", "payphone", "Marron 5"],
    ["https://www.youtube.com/watch?v=7C2z4GqqS5E", "fake love", "BTS"],
    ["https://www.youtube.com/watch?v=ogalmk6K0zs", "cry for me", "TWICE"],
    ["https://www.youtube.com/watch?v=-RJSbO8UZVY", "young blood", "5 Seconds of Summer"],
    ["https://www.youtube.com/watch?v=NFNQEPcgsmA", "better", "Zayn"],
    ["https://www.youtube.com/watch?v=LdH7aFjDzjI", "I’m a mess", "Bebe Rexha"],
    ["https://www.youtube.com/watch?v=eNd4tt9raeg", "dusk til dawn", "Zayn, Sia"],
    ["https://www.youtube.com/watch?v=C_3d6GntKbk", "pillow talk", "Jeff Kaele"],
    ["https://www.youtube.com/watch?v=sZSf5dpZdlI", "centuries", "Fall Out Boy"],
    ["https://www.youtube.com/watch?v=fXw0jcYbqdo", "talking to the moon", "Bruno Mars"],
    ["https://www.youtube.com/watch?v=7JJfJgyHYwU", "me and my broken heart", "Rixton"],
    ["https://www.youtube.com/watch?v=GDTD24KsdGc", "love like you", "Steven Universe"],
    ["https://www.youtube.com/watch?v=4h26oYuE2h0", "trampoline", "Shaed and Zayn"],
    ["https://www.youtube.com/watch?v=HiXZGbLRQrY", "running back to you", "Martin Jensen, Alle Farben, Nico Santos"],
    ["https://www.youtube.com/watch?v=izIyhdEHSPo", "love lies", "Khalid, Normani"],
    ["https://www.youtube.com/watch?v=109HJ6_1rfg", "Tyler Durden", "Madison Beer"],
    ["https://www.youtube.com/watch?v=BwBeHrCCJ6M", "boys like you", "Anna Clendening"],
    ["https://www.youtube.com/watch?v=PXGycbkbtW0", "it’s you", "Alie Gatie"],
    ["https://www.youtube.com/watch?v=3mWbRB3Y4R8", "don’t you worry child", "Swedish House Mafia, John Martin"],
    ["https://www.youtube.com/watch?v=Qzc_aX8c8g4", "dancing with your ghost", "Sasha Sloan"],
]

neutralList = [
    ["https://www.youtube.com/watch?v=W8a4sUabCUo", "dandelions", "Ruth. B"],
    ["https://www.youtube.com/watch?v=-grLLLTza6k", "wolves", "Selena Gomez"],
    ["https://www.youtube.com/watch?v=ycy30LIbq4w", "lost in Japan", "Shawn Mendes"],
    ["https://www.youtube.com/watch?v=SlPhMPnQ58k", "memories", "Maroon 5"],
    ["https://www.youtube.com/watch?v=ulNswX3If6U", "back to you", "Selena Gomez"],
    ["https://www.youtube.com/watch?v=j60ClcNYWu4", "zero", "Imagine Dragons"],
    ["https://www.youtube.com/watch?v=8qZgRHgguXk", "willow", "Taylor Swift"],
    ["https://www.youtube.com/watch?v=g9aNdMLYUrk", "champagne problems", "Taylor Swift"],
    ["https://www.youtube.com/watch?v=GTWqwSNQCcg", "city of stars", "La La Land Original Motion Picture Soundtrack"],
    ["https://www.youtube.com/watch?v=tk36ovCMsU8", "silence", "Marshmello"],
    ["https://www.youtube.com/watch?v=av5JD1dfj_c", "dancing with a stranger", "Sam Smith, Normani"],
    ["https://www.youtube.com/watch?v=Y2E71oe0aSM", "10000 hours", "Dan + Shay, Justin Bieber"],
    ["https://www.youtube.com/watch?v=0yi5tiv9FwM", "life goes on", "BTS"],
    ["https://www.youtube.com/watch?v=Rdlc4b5NL5g", "peace and love", "Steven Universe"],
    ["https://www.youtube.com/watch?v=pTOC_q0NLTk", "ophelia", "The Lumineers"],
    ["https://www.youtube.com/watch?v=FlSxBCHul1A", "all the things she said", "Seraphine"],
    ["https://www.youtube.com/watch?v=Rnu83PtOQfc", "made me this way", "Seraphine"],
    ["https://www.youtube.com/watch?v=Yp4yF5hb89I", "come thru", "Jeremy Zucker"],
    ["https://www.youtube.com/watch?v=eY_eqNHguwg", "fools", "Madison Beer"],
    ["https://www.youtube.com/watch?v=cMg8KaMdDYo", "fly away", "TheFatRat"],
    ["https://www.youtube.com/watch?v=Uh3cbLgVXP0", "summer wind", "Various Artists"],
    ["https://www.youtube.com/watch?v=pk7ESz6vtyA&t=5s", "winter bear", "V"],
    ["https://www.youtube.com/watch?v=CKZvWhCqx1s", "on the ground", "Rose"]
]

happyList = [
    ["https://www.youtube.com/watch?v=qDRORgoZxZU", "Me Too", "Meghan Trainor"],
    ["https://www.youtube.com/watch?v=BQ0mxQXmLsk", "Havana", "Camila Cabello ft. Young Thug"],
    ["https://www.youtube.com/watch?v=PKWHYLtmAGA", "Salt", "Ava Max"],
    ["https://www.youtube.com/watch?v=bQCg73ox1Rc", "Childhood Dreams", "Cover by Seraphine"],
    ["https://www.youtube.com/watch?v=jiXP-FRrSOg", "Everybody Wants You", "Johnny Orlando"],
    ["https://www.youtube.com/watch?v=Il-an3K9pjg", "2002", "Anna-Marie"],
    ["https://www.youtube.com/watch?v=2z5un3c8hbo", "I Love You 3000 II", "Stephanie Poetri ft. Jackson Wang"],
    ["https://www.youtube.com/watch?v=Y7ix6RITXM0", "Maps", "Maroon 5"],
    ["https://www.youtube.com/watch?v=an3R3XQ4sgk", "North Star", "Tyler Shaw"],
    ["https://www.youtube.com/watch?v=6RLLOEzdxsM", "All Falls Down", "Alan Walker"],
    ["https://www.youtube.com/watch?v=u-qYMl9T9wQ", "Liar Liar", "Cris Cab"],
    ["https://www.youtube.com/watch?v=2NbC8kGGNus", "Counting Stars", "OneRepublic"],
    ["https://www.youtube.com/watch?v=0yBnIUX0QAE", "Dancing in the Moonlight", "Toploader"],
    ["https://www.youtube.com/watch?v=Y2V6yjjPbX0", "Handclap", "Fitz and the Trantrums"],
    ["https://www.youtube.com/watch?v=VPRjCeoBqrI", "A Sky Full of Stars", "Coldplay"],
    ["https://www.youtube.com/watch?v=kOkQ4T5WO9E", "This Is What You Came For", "Calvin Harris ft. Rihanna"],
    ["https://www.youtube.com/watch?v=CvBfHwUxHIk", "Umbrella", "Rihanna ft. JAY-Z"],
    ["https://www.youtube.com/watch?v=KQetemT1sWc", "Here Comes The Sun", "The Beatles"],
    ["https://www.youtube.com/watch?v=Km3wOjaRyE4", "We Can’t Stop", "Miley Cyrus"],
    ["https://www.youtube.com/watch?v=FDWTP4_5eps", "Yellow Hearts", "Ant Saunders"]
]

ecstaticList = [
    ["https://www.youtube.com/watch?v=MBdVXkSdhwU", "DNA", "BTS"],
    ["https://www.youtube.com/watch?v=kTlv5_Bs8aw", "Mic Drop (Steve Aoki Remix)", "BTS"],
    ["https://www.youtube.com/watch?v=gdZLi9oWNZg", "Dynamite", "BTS"],
    ["https://www.youtube.com/watch?v=wS7anrSXKrY", "Blue Flame", "ASTRO"],
    ["https://www.youtube.com/watch?v=Zz7YZtpz2Ek", "Knock", "ASTRO"],
    ["https://www.youtube.com/watch?v=3VTkBuxU4yk", "MORE", "K/DA"],
    ["https://www.youtube.com/watch?v=OPf0YbXqDm0", "Uptown Funk", "Mark Ronson ft. Bruno Mars"],
    ["https://www.youtube.com/watch?v=PHn5Q7hCjxw", "Immortals", "Fall Out Boys"],
    ["https://www.youtube.com/watch?v=7-x3uD5z1bQ", "Watermelon Sugar", "Harry Styles"],
    ["https://www.youtube.com/watch?v=ZbZSe6N_BXs", "Happy", "Pharrell Williams"],
    ["https://www.youtube.com/watch?v=TzFRVk2ektI", "Blueberry Eyes", "MAX ft. SUGA of BTS"],
    ["https://www.youtube.com/watch?v=KhTeiaCezwM", "HIP", "MAMAMOO"],
    ["https://www.youtube.com/watch?v=YswhUHH6Ufc", "Bang Bang", "Jessie J, Ariana Grande, Nicki Minaj"],
    ["https://www.youtube.com/watch?v=glKgDqZ1ABU", "Miss Alissa", "Eagles Of Death Metal"],
    ["https://www.youtube.com/watch?v=pmanD_s7G3U", "Gurenge", "LiSA"],
    ["https://www.youtube.com/watch?v=DwRndYRTuyw", "Dionysius", "BTS"]
]

@client.event
async def on_ready():
    general_channel = client.get_channel(835324404841709589)
    mbed = discord.Embed(
        title = 'ViBot is Now Online!',
        description = 'See `v!help` for a list of commands. Enjoy!',
        color = discord.Color.green()
    )
    await general_channel.send(embed = mbed)

def getScore(txt):
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(txt)["compound"]

def getEmotion(score):
    if score > 0.6:
        return 'ecstatic'
    elif score > 0.2:
        return 'happy'
    elif score < -0.6:
        return 'gloomy'
    elif score < -0.2:
        return 'sad'
    else:
        return 'neutral'
    
def storeScore(name, score):
    driverstr = config('driverstr')
    with pyodbc.connect(driverstr) as conn:
        with conn.cursor() as cursor:
            cnt = cursor.execute("select count(*) as cnt from vibeScores where username = '" + str(name) + "'").fetchone().cnt
            if cnt > 0:  # user exists, update
                cursor.execute("update vibeScores set recent = '" + str(score) + "' where username = '" + str(name) + "'")
                cursor.execute("update vibeScores set average = (average*vibeCount + '" + str(score) + "')/(vibecount+1) where username = '" + str(name) + "';")
                cursor.execute("update vibeScores set vibeCount = vibeCount + 1 where username = '" + str(name) + "'")
            else:
                cursor.execute("insert into vibeScores (username, recent, average, vibeCount) Values ('" + str(name) + "', '" + str(score) + "', '" + str(score) + "', '1');")
            cursor.commit()

def getLink(emotion):
    if(emotion=='ecstatic'):
        idx = random.randint(0, len(ecstaticList)-1)
        return ecstaticList[idx]
    elif(emotion=='happy'):
        idx = random.randint(0, len(happyList)-1)
        return happyList[idx]
    elif(emotion=='neutral'):
        idx = random.randint(0, len(neutralList)-1)
        return neutralList[idx]
    elif(emotion=='sad'):
        idx = random.randint(0, len(sadList)-1)
        return sadList[idx]
    else:
        idx = random.randint(0, len(gloomyList)-1)
        return gloomyList[idx]

def getEmoji(emotion):
    if(emotion=='ecstatic'):
        return ':smiling_face_with_3_hearts :'
    elif(emotion=='happy'):
        return ':slight_smile:'
    elif(emotion=='neutral'):
        return ':neutral_face:'
    elif(emotion=='sad'):
        return ':slight_frown:'
    else:
        return ':cry:'

def getStoredScore(name):
    driverstr = config('driverstr')
    with pyodbc.connect(driverstr) as conn:
        with conn.cursor() as cursor:
            cnt = cursor.execute("select count(*) as cnt from vibeScores where username = '" + str(name) + "'").fetchone().cnt
            if cnt > 0:
                return cursor.execute("select recent from vibeScores where username = '" + str(name) + "'").fetchone().recent
            else:
                return -2
            cursor.commit()

def getStoredAvg(name):
    driverstr = config('driverstr')
    with pyodbc.connect(driverstr) as conn:
        with conn.cursor() as cursor:
            cnt = cursor.execute("select count(*) as cnt from vibeScores where username = '" + str(name) + "'").fetchone().cnt
            if cnt > 0:
                return cursor.execute("select average from vibeScores where username = '" + str(name) + "'").fetchone().average
            else:
                return -2
            cursor.commit()

def getStoredCount(name):
    driverstr = config('driverstr')
    with pyodbc.connect(driverstr) as conn:
        with conn.cursor() as cursor:
            return cursor.execute("select count(*) as cnt from vibeScores where username = '" + str(name) + "'").fetchone().cnt

def getCompare(score, average):
    if score > average:
        return 'better'
    elif score == average:
        return 'the same'
    else:
        return 'worse'

@client.command()
async def mood(ctx, *, message):
    name = ctx.author
    score = getScore(message)
    emotion = getEmotion(score)
    link = getLink(emotion)
    emoji = getEmoji(emotion)
    storeScore(name, score)
    compare = getCompare(score, avg)

    mbed = discord.Embed(
        title = 'Calculating mood...',
        description = name.mention + ', check out your emotions!',
        color = discord.Color.blue()
    )
    mbed.add_field(name='You are currently ' + emotion + ' ' + emoji, value='From a scale of -1 to 1, your vibeScore is ' + str(round(score, 4)) + '. You are feeling ' + compare + ' than usual!', inline=False) # ADD DESCRIPTION ?? and insert youtube link or smt (figure link embed)
    mbed.add_field(name='Listen to this Song ~ ', value=link[1] + ' by ' + link[2], inline=False)
    await ctx.send(embed = mbed)
    await ctx.send(link[0])

@client.command()
async def dm(ctx):
    name = ctx.author
    mbed1 = discord.Embed(
        title = 'Hey ' + str(name).split('#')[0] + '!',
        description = 'Let\'s chat! Feel free to use ViBot commands to interact. For more info, type `p!help`.',
        color = discord.Color.blue()
    )
    await name.send(embed=mbed1)
    mbed2 = discord.Embed(
        title = "Direct Message Sent!",
        description = "Hey " + name.mention + ", check your DMs! :)",
        color = discord.Color.blue()
    )
    await ctx.send(embed=mbed2)


@client.command()
async def repeat(ctx):
    name = ctx.author
    cnt = getStoredCount(name)
    if cnt > 0:  # user exists, update
        score = getStoredScore(name)
        avg = getStoredAvg(name)
        emotion = getEmotion(score)
        emoji = getEmoji(emotion)
        link = getLink(emotion)
        compare = getCompare(score, avg)
        v
        mbed = discord.Embed(
            title = 'Retrieving mood...',
            description = name.mention + ', check out your emotions!',
            color = discord.Color.blue()
        )
        mbed.add_field(name='You are currently ' + emotion + ' ' + emoji, value='From a scale of -1 to 1, your vibeScore is ' + str(round(score, 4)) + '. You are feeling ' + compare + ' than usual!', inline=False)
        mbed.add_field(name='Listen to this Song ~ ', value=link[1] + ' by ' + link[2], inline=False)
        await ctx.send(embed=mbed)
        await ctx.send(link[0])
    else:
        mbed = discord.Embed(
            title = 'You are Currently Moodless :face_with_raised_eyebrow:',
            description = 'We don\'t have your recent moods saved! Calculate your mood using `v!mood` first before asking for another song.',
            color = discord.Color.red()
        )
        await ctx.send(embed=mbed)

@client.command()
async def clear(ctx):
    name = ctx.author
    driverstr = config('driverstr')
    with pyodbc.connect(driverstr) as conn:
        with conn.cursor() as cursor:
            cnt = cursor.execute("delete from vibeScores where username = '" + str(name) + "'")
            cursor.commit()

    mbed = discord.Embed(
        title = 'Clearing Data',
        description = 'Your average mood has been reset! Once you have checked your mood ten times, your average will be displayed.',
        color = discord.Color.blue()
    )
    await ctx.send(embed = mbed)

@client.command()
async def help(ctx):
    mbed = discord.Embed(
        title = 'Welcome to our help page! Here is a list of all ViBot commands:',
        color = 16776960
    )
    mbed.add_field(name='About Page: `v!about`', value='The About Page will introduce you to the purpose of ViBot and tell you a little about the creators!', inline=False)
    mbed.add_field(name='Clearing Data: `v!clear`', value='Use this command to clear your previous mood scores and averages! Start fresh for the new you.', inline=False)
    mbed.add_field(name='Direct Messaging: `v!dm`', value='If you want some private conversation between just you and ViBot, ask for a DM :eyes:')
    mbed.add_field(name='Help Page: `v!help`',  value = 'The Help Page will show you a list of commands and what they can be used for... Try experimenting with them!', inline=False)
    mbed.add_field(name='Mood Detector: `v!mood <message>`', value='Tell us about your day! ViBot will calculate your current emotions and recommend you a sick song to vibe to!', inline=False)
    mbed.add_field(name='Get Another Song: `v!repeat`', value='If you enjoyed the last song ViBot recommended, request for another song without changing your mood!', inline=False)
    await ctx.send(embed = mbed)

@client.command()
async def about(ctx):
    mbed = discord.Embed(
        title =  'About:',
        description = "This bot reads in message with the v!mood command followed by a message. After detecting the mood of the message, the bot then sends a corresponding song that matches the mood and produces an emotion score ranging from -1 (sad) to 1 (happy). Your previous emotion scores will be stores and the average is calculate to compare with your current emotion. For information on which commands ViBot supports, visit `v!help`. Have fun! :)\n",
        color = 16776960
    )
    await ctx.send(embed = mbed)

@client.event
async def on_command_error(ctx, error):
    mbed = discord.Embed(
        title = 'Error: Command does not Exist!',
        description = 'Visit `v!about` to learn about ViBot, or see `v!help` for a list of commands.',
        color = discord.Color.red()
    )
    await ctx.send(embed = mbed)

client.run(TOKEN)