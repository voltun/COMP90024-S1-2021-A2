import tweepy, json, configparser, os
#from geopy.geocoders import Nominatim

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
places = api.geo_search(query="Melbourne",granularity="city")
place_id = places[0].id
tweets = tweepy.Cursor(api.search,
                       q="place:%s" % place_id,
                       lang="en",).items(100)
count = 0
file=open("tweet2.txt","w")

for tweet in tweets:
    if tweet.coordinates != None:
        tweet = tweet._json
        file.write(json.dumps(tweet)+ '\n')

tweets_data_path='tweet2.txt'
tweets_data=[]
tweets_file=open(tweets_data_path,"r")
#read in tweets and store on list
for line in tweets_file:
    tweet=json.loads(line)
    tweets_data.append(tweet)
tweets_file.close()

# from geopy.geocoders import Nominatim
# geolocator = Nominatim(user_agent="test_app")
# location = geolocator.reverse("27.1751, 78.0421")
# print(location.raw['address']['country'])

