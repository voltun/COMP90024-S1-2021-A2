import configparser

config = configparser.ConfigParser()

config.read('auth.cfg')

access_token= config.get('Twitter_Auth','access_token')
access_token_secret= config.get('Twitter_Auth','access_secret')
consumer_key= config.get('Twitter_Auth','api_key')
consumer_secret= config.get('Twitter_Auth','api_secret_key')

print
