import tweepy, json, configparser, os

# Obtain full file path 
pardir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(pardir, '../auth.cfg')

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

tweet_list=[]
class MyStreamListener(tweepy.StreamListener):
    def __init__(self,api=None):
        super(MyStreamListener,self).__init__()
        self.num_tweets=0
        self.file=open("tweetStream.txt","w")
    def on_status(self,status):
        tweet=status._json
        if status.coordinates != None:
            self.file.write(json.dumps(tweet)+ '\n')
            tweet_list.append(status)
            self.num_tweets+=1
        if self.num_tweets<1000:
            return True
        else:
            return False
        self.file.close()

#create streaming object and authenticate
l = MyStreamListener()
stream = tweepy.Stream(auth,l)
#this line filters twiiter streams to capture data by keywords
australia = [113.338953078, -43.6345972634, 153.569469029, -10.6681857235]
stream.filter(locations=australia)
