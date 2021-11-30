# ViBot-Submission
# Inspiration
The inspiration for this project originated from the Discord Rhythm bot. After playing around with various Discord Bots, we thought that it would be an interesting idea if we could create a music bot... but instead, suggested songs. To make the bot relevant to the current pandemic, we decided to make it suggest songs based off of the messages our users send, a way to combat the lack of social interaction in the pandemic. The bot is coded within python and uses the API from the Discord.py library as well as the Natural Languages ToolKit or the NLTK python library.

# What it Does
The goal for the bot is to provide support to those that need it. Especially during the pandemic, most can’t interact with their friends due to the lockdown. This bot reads in a message with the ‘v!mood ’ command. After detecting the mood of the message, the bot then sends a corresponding song that matches the mood and produces an emotion score ranging from -1 to 1 (-1 being most sad, 1 being most happy). Our bot also stores the previous data from each user to compute your average vibe score, comparing your most recent mood with your average. For more commands, use the ‘v!help’ command!

# How We Built it
ViBot was mainly built using python and the discord API from the python library discord.py. The backend is coded using python, while the database is scripted with SQL hosted with Microsoft Azure’s servers. To process emotions within messages, we used the built in VADER sentiment analyzer from the NLTK library in python.

# Challenges We Ran Into
It took a long time for our team to come up with a unique yet feasible project idea. After hours of discussion, we decided on creating a discord bot. Some challenges that we ran into include finding a good platform to create our idea on. We were worried that we may not be able to finish implementing the bot in time for the deadline. ViBot was an extensive idea to finish within 24 hours within formulating it.

# Accomplishments that We Are Proud of
We are most proud of being able to successfully implement a machine-learning, database-required Discord Bot. All the concepts and technology were new to us, since our team’s experience is limited to Competitive Programming. This was our first time writing a hackathon for many of us, this was a great learning experience teaching us what cloud computing was and how it worked.

# What We Learned
Throughout the course of this hackathon, we learned how to implement a discord bot as this would be the first time any of us implemented a discord bot. We also learnt how to implement a server in order to run the bot from a remote database. It took a lot of research and
