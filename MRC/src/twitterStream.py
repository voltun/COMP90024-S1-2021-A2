import tweepy, json

class MyStreamListener(tweepy.StreamListener):
    def __init__(self,api=None):
        super(MyStreamListener,self).__init__()
        self.num_tweets=0
        self.file=open("tweetStream.txt","w")

    def on_status(self,status):
        tweet=status._json
        if status.coordinates != None:
            self.file.write(json.dumps(tweet)+ '\n')
            self.num_tweets+=1
        if self.num_tweets<1000:
            return True
        else:
            return False
        self.file.close()

def twitterStream(config):

    access_token = config.get('Twitter_Auth','access_token')
    access_token_secret = config.get('Twitter_Auth','access_secret')
    consumer_key = config.get('Twitter_Auth','api_key')
    consumer_secret = config.get('Twitter_Auth','api_secret_key')

    # Establish authentication to Twitter's API
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)

    #use streaming object and authenticate
    l = MyStreamListener()
    stream = tweepy.Stream(auth,l)
    #this line filters twiiter streams to capture data from Australia's bounding box
    australia = [113.338953078, -43.6345972634, 153.569469029, -10.6681857235]
    stream.filter(locations=australia)
