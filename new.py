
import tweepy
import webbrowser


# Make constants to hold values of our keys
CONSUMER_KEY = "0vCXY0d749szF6sJ2TUdp050S"
CONSUMER_SECRET = "7QkNqpK1qU2tZO8SuaY6Qs7GRxAxrmLyXuCvPzhGvb0zswzLbw"
ACCESS_TOKEN = "2259569294-mcPgMfJNO7UafgGONRuR0bKjOejIy7qpXP1lpu8"
ACCESS_SECRET = "Z22Nt5tI1rtEs2eq3ZjrTuma5CMHz5jiANrPknqnBiOXX"


# set auth variables
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)


# create a new api
api = tweepy.API(auth)


# create an instance of the twitter api class
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth_url = auth.get_authorization_url()


# open the window for authorization, twitter will generate the pin
webbrowser.open(auth_url)
print "Copy PIN from the window that opens"


# get the pin number from the user
verifier = raw_input('PIN: ').strip()
auth.get_access_token(verifier)


# get the access key and secret returned from twitter
access_key = auth.access_token.key
access_secret = auth.access_token.secret


# set authorization token
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


# make a tweet
def send_tweet():
    to_tweet = True
    tweet_text = raw_input("Enter your tweet content below... Only the first 140 characters will be used.\n>>> ")
    api.update_status(tweet_text[0:140])
    print "You tweeted \n'" + tweet_text[0:140] + "'"
    restart = raw_input("Do you want to tweet again? (Y/N)\n>>> ")
    if restart.lower() == "y":
        send_tweet()
    else:
        print "Returning to the Main Menu...\n"


# search twitter
def keyword_follow():
    search_phrase = raw_input("What do you want to search for?\n>>> ").strip()
    search_number = raw_input("How many results do you want to return?\n>>> ")
    search_result = api.search(search_phrase, rpp=search_number)
    for i in search_result:
        print i.from_user + " said " + i.text + "\n"
        to_follow = raw_input("Do you want to follow " + i.from_user + "? (Y/N)\n>>> ")
        if to_follow.lower() == "n":
            print i.from_user + " was not followed!"
        else:
            api.create_friendship(i.from_user)
            print "You followed " + i.from_user + "!\n"

    # check if the user wants to search again
    restart = raw_input("Do you want to search again? (Y/N)\n>>> ")
    if restart.lower() == "n":
        print "Returning to the Main Menu...\n"
    else:
        return keyword_follow()

def keyword_retweet():
    search_phrase = raw_input("What do you want to search for?\n>>> ").strip()
    search_number = raw_input("How many results do you want to return?\n>>> ")
    search_result = api.search(search_phrase, rpp=search_number)
    for i in search_result:
        print i.from_user + " said " + i.text + "\n"
        to_retweet = raw_input("Do you want to retweet" + i.from_user + "? (Y/N)\n>>> ")
        if to_retweet.lower() == "n":
            print i.from_user + " was not retweeted!"
        else:
            api.retweet(i.id)
            print "Retweeted!\n"
            again = raw_input("See more? (Y/N)\n>>> ")
            if again.lower() == "n":
                break       
    # check if the user wants to search again
    restart = raw_input("Do you want to search again? (Y/N)\n>>> ")
    if restart.lower() == "n":
        print "Returning to the Main Menu...\n"
    else:
        return keyword_retweet()



def mass_unfollow():
    hits_left = api.rate_limit_status()['remaining_hits']
    print "You can unfollow " + str(hits_left) + " people this hour...\n"
    print "Checking who doesn't follow you back. This will take a minute.\n"
    # first, create some lists to hold the followers
    followers = []
    friends = []

    # we have to use a Cursor for pagination purposes
    for follower in tweepy.Cursor(api.followers).items():
        followers.append(follower)


    for friend in tweepy.Cursor(api.friends).items():
        friends.append(friend)

    # create a non_reciprocals list, these are non-followers (set - set)
    non_reciprocal = list(set(friends) - set(followers))
    print str(len(non_reciprocal)) + " non-reciprocal followers.\n"


    # first, double check that we want to unfollow
    double_check = raw_input("Unfollow them? (Y/N) ***WARNING, THIS ACTION CANNOT BE UNDONE***\n>>> " )


    if double_check.lower() == "y":
        # count the number of people we unfollow, just for fun
        counter = 0
        for i in non_reciprocal:
            if hits_left > 0:
                api.destroy_friendship(i.screen_name)
                print "Successfully unfollowed " + i.screen_name
                hits_left -= 1
            else:
                print "You ran out of hits! Try again in an hour!"

            counter += 1
        print "You unfollowed " + str(counter) + " people!\n"
        print "Now returning to the Main Menu."
    else:
        print "Returning to the Main Menu...\n"

        #todo - automatically DM new followers      
def direct_messages():
    new_followers = API.followers(user)

    for i in new_followers:
        newDM = raw_input (i.from_user + "send follower DM?" + "Y/N" )
        if newDM.lower() == "n":
            print i.from_user + " was not messaged"
            print "Now returning to the Main Menu."
    else:
        api.send_direct_message(user_id = i.from_user, text = "message text here"
        print "You messaged " + i.from_user


# create the menu
keep_running = True
while keep_running:
    print "Main Menu"
    print "---------\n"
    selection = raw_input("(1)Tweet | (2)Keyword Follow | (3)Keyword Retweet | (4)Mass Unfollow | (5)End | (6)Direct Message\n\n>>> ")
    if selection == "1":
        print "New Tweet"
        print "---------\n"
        send_tweet()
    elif selection == "2":
        print "Keyword Follow"
        print "--------------\n"
        keyword_follow()
    elif selection == "3":
        print "Keyword Retweet"
        print "---------------\n"
        keyword_retweet()
    elif selection == "4":
        print "Mass Unfollow"
        print "-------------\n"
        print "WARNING: MASS UNFOLLOW IS AGAINST THE TOS OF TWITTER. YOU'VE BEEN WARNED\n"
        mass_unfollow()
    elif selection == "5":
        print "Direct Message"
        print "------------\n"
        direct_messages()
    else:
        print "BYE!\n\n"
keep_running = False