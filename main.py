from pprint import pprint
import tweepy
#from linkedin import linkedin
from techcrunch import techcrunch
from wired import wired
from techradar import techradar
from robotics import robotics
import time
from flask import Flask, render_template
from datetime import date, timedelta


#180 queries every 15 minutes
existing_followers = []
present_followers = []

# Authenticate to Twitter
# Check Twitter developer API for more information
auth = tweepy.OAuthHandler("xxxxxxxxxxxxxxxxxxxxx",
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
auth.set_access_token("xxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                         "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)
    
app = Flask(__name__)

def retweets(topics):
    tweets_per_query  = 50
    new_tweets = 0
    for topic in topics:
        print ("Starting new querry: " + topic)
        for tweet in tweepy.Cursor(api.search, q=topic, tweet_mode="extended").items(tweets_per_query ):

            user = tweet.user.screen_name
            id = tweet.id
            url = 'https://twitter.com/' + user +  '/status/' + str(id)
            print (url)

            try:
                text = tweet.retweeted_status.full_text.lower()
            except:
                text = tweet.full_text.lower()
            
            if "retweet" in text or "rt" in text:
                if not tweet.retweeted:
                    try:
                        tweet.retweet()
                        print("\tRetweeted")
                        new_tweets += 1
                    except tweepy.TweepError as e:
                        print('\tAlready Retweeted')

            if "like" in text or "fav" in text:
                try:
                    tweet.favorite()
                    print('\t' + "Liked")
                except:
                    print('\tAlready Liked')
            if "follow" in text:
                try:
                    to_follow = [tweet.retweeted_status.user.screen_name] + [i['screen_name'] for i in tweet.entities['user_mentions']]
                # Don't follow origin user (person who retweeted)
                except:
                    to_follow = [user] + [i['screen_name'] for i in tweet.entities['user_mentions']]

                for screen_name in list(set(to_follow)):
                    api.create_friendship(screen_name)
                    print('\t' + "Followed: " + screen_name)

    print ("New Tweets: " + str(new_tweets))

def message_followers():
    followers = api.followers()
    
    for follower in followers:
        present_followers.append(follower.screen_name)
    
    with open("followers.txt", 'r') as file:
        existing_followers = [line.replace('\n', '') for line in file]

    if (len(existing_followers) == len(present_followers)):
        print ("There are no new followers")
        return

    if (len(existing_followers) != len(present_followers)):
        new_followers = list(set(present_followers)-set(existing_followers))
        print (new_followers)
        for follower in new_followers:
            direct_message = api.send_direct_message(recipient_id='@'+follower, text='Thank you for following')

        with open("followers.txt", "w") as file:
            for follower in present_followers:
                file.write(follower + '\n')

    else:
        print ("Someone has unfollowed you")

def direct_messages():
    new_followers = api.followers_ids()
    
    with open("followers.txt", 'r') as file:
        existing_followers = [line.replace('\n', '') for line in file]

    for i in new_followers:
        api.send_direct_message(recipient_id = i.recipient_id, text = "Thank you for following")
        print ("You messaged " + i.recipient_id)

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    if False:
        current_date = date        
    else:
        current_date = date(2019, 12, 29)
    end_date = current_date + timedelta(days=10)
    no_of_days = (end_date - current_date).days

    print (no_of_days)
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")

    topics = ['ai', 'robotics', 'iiot', 'iot']
   
    try:
        tech = techcrunch(topics)
        title, link = tech.parse()
        #print (title,'\n', link)        
        api.update_status(title + '\n' + link)

    except:
        print ("Techcrunch is not supporting a tag in {}. Hence skipping".format(topics))
        pass
    time.sleep(3)
    
    try:
        wired = wired(topics)
        title, link = wired.parse()
        #print (title,'\n', link)
        api.update_status(title + '\n' + link)
    except:
        print ("Wired is not supporting a tag in {}. Hence skipping".format(topics))
        pass
    time.sleep(3)

    try:
        techrad = techradar(topics)
        title, link = techrad.parse()
        #print (title,'\n', link)
        api.update_status(title + '\n' + link)
    except:
        print ("techradar is not supporting a tag in {}. Hence skipping".format(topics))
        pass
    time.sleep(3)

    try:
        robo = robotics()
        title, link = robo.parse()
        #print (title,'\n', link)
        api.update_status(title + '\n' + link)
    except:
        print ("Robotics.org is not supporting a tag in {}. Hence skipping".format(topics))
        pass
    '''
    #retweets(topics)
    message_followers()
    #direct_messages()
    '''
