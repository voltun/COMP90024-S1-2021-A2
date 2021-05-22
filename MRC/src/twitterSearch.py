import tweepy, json, configparser, os
from getPostCode import getPostCode

# Obtain full file path
pardir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(pardir, 'auth.cfg')

# Setup configparser to read in authentication credentials
config = configparser.ConfigParser()
config.read(filepath)

access_token = config.get('Twitter_Auth','access_token')
access_token_secret = config.get('Twitter_Auth','access_secret')
consumer_key = config.get('Twitter_Auth','api_key')
consumer_secret = config.get('Twitter_Auth','api_secret_key')

# Establish authentication to Twitter's API
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
places = api.geo_search(query="Australia",granularity="country")
place_id = places[0].id
api.wait_on_rate_limit = True
tweets = tweepy.Cursor(api.search,
                       q="place:%s" % place_id,
                       lang="en").items(1000000)

file=open("tweetSearch.txt","w")

count = 0
for tweet in tweets:
    count+=1
    if tweet.coordinates != None:
        tweet = tweet._json
        long,lat = tweet['coordinates']['coordinates']
        postcode = getPostCode(lat,long)
        if postcode == None:
            pass
        else:
            temp = {"postcode":postcode}
            tweet['coordinates'].update(temp)
            file.write(json.dumps(tweet)+ '\n')

