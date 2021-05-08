import tweepy,json

access_token="437679061-ETGabTR6ZlFZeymd0taF9JuGsgipnQVk1kRtyT4X"
access_token_secret="VCMPpNluQJGCk28qrQdau5lt5vS9HLG5vQxvDUgHKfrli"
consumer_key="Wl5xYqP6L6effcQfE23aewTJR"
consumer_secret="BBei97Aol6CxMdPQ4nfrQ6mWnQv3fZwtpFOvAkdAgVOhotnNmC"
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

tweet_list=[]
class MyStreamListener(tweepy.StreamListener):
    def __init__(self,api=None):
        super(MyStreamListener,self).__init__()
        self.num_tweets=0
        self.file=open("tweet.txt","w")
    def on_status(self,status):
        tweet=status._json
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
stream.filter(track=['covid','corona','covid19','coronavirus',
'facemask','sanitizer','social-distancing'])

tweets_data_path='tweet.txt'
tweets_data=[]
tweets_file=open(tweets_data_path,"r")
#read in tweets and store on list
for line in tweets_file:
    tweet=json.loads(line)
    tweets_data.append(tweet)
tweets_file.close()
print(tweets_data[0])
