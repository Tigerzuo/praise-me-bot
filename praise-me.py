# praise me bot

import praw
import time

# create the objects from the imported modules

# reddit api login
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     username='',
                     password='',
                     user_agent='')
                    

# the subreddits you want your bot to live on
subreddit = reddit.subreddit('testingground4bots')

# phrase to activate the bot
keyphrase = '!praiseme'

# look for phrase and reply appropriately
for comment in subreddit.stream.comments():
    time.sleep(0.001)
    if keyphrase in comment.body:
        try:
            comment.reply('You\'re awesome, you\'re great, you\'re the best!')
            print("Commented")
        except:
            print('to frequent')
            
