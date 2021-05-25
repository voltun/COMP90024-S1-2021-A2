import tweepy, json

def twitterSearch(config):

    access_token = config.get('Twitter_Auth','access_token')
    access_token_secret = config.get('Twitter_Auth','access_secret')
    consumer_key = config.get('Twitter_Auth','api_key')
    consumer_secret = config.get('Twitter_Auth','api_secret_key')

    # Establish authentication to Twitter's API
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)

    #set Australia as a filter
    places = api.geo_search(query="Australia",granularity="country")
    place_id = places[0].id

    #set wait time to prevent error
    api.wait_on_rate_limit = True
    tweets = tweepy.Cursor(api.search,q="place:%s" % place_id,lang="en").items(1000000)

    #output data onto file
    file=open("tweetSearch.txt","w")
    for tweet in tweets:
        if tweet.coordinates != None:
            file.write(json.dumps(tweet._json)+'\n')
