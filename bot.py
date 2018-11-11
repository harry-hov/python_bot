import tweepy
import time

print("Twitter bot is working")

CONSUMER_KEY = '0blh3DmV0NEqZYjoY8BmL27LO'
CONSUMER_SECRET = 'GnN8ry6JuWQmLOWzdpDhNKxeJAdfgEYooGTZP33WUSHxleqAl1'
ACCESS_KEY = '2904651089-JKbnqW1M8YxB8Y9nn0HGeEMN6kw7hMWfwQBXFvJ'
ACCESS_SECRET = '7746W0OnloVCuPRi2NhCkYqzy7XjQ6iq4C1IRjL1ULqOn'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return



def reply_to_tweets():
    print("retrieving and replying to tweets...", flush=True)
    last_seen_id = retrieve_last_seen_id(FILE_NAME)

    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')
    mentions.__dict__
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#helloharry' in mention.full_text.lower():
            print('found HelloHarry..!', flush=True)
            print('Responding back...', flush=True)
            api.update_status('@' + mention.user.screen_name + ' ' +
                    'this is test reply. Ty :)', mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)
