# web_app/services/twitter_service.py

import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

def twitter_api():
    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    print("AUTH", auth)
    api = tweepy.API(auth)
    print("API", api)
    #print(dir(api))
    return api

if __name__ == "__main__":

    api = twitter_api()
    user = api.get_user("keinobaird")
    print("USER", user)
    print(user.screen_name)
    print(user.name)
    print(user.followers_count)

    #breakpoint()

api = twitter_api() 
tweets = api.user_timeline("keinobaird", tweet_mode="extended", count=150, exculude_replies=True, include_rts=False)
#tweets = api.user_timeline("keinobaird", tweet_mode="extended", count=150) 
print(type(tweets)) # <class 'tweepy.models.ResultSet'>

for tweet in tweets:
    print("-----------")
    print(tweet.id, tweet.full_text)
   

    public_tweets = api.home_timeline()
    
    for tweet in public_tweets:
        print(type(tweet)) #> <class 'tweepy.models.Status'>
        #print(dir(tweet))
        print(tweet.text)
        print("-------------")