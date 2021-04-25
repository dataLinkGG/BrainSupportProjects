import tweepy
from my_tokens import *
from my_settings import *
from multipledispatch import dispatch


class TwitterAPI:
    def __init__(self):
        self.api = self.authenticate()

    @staticmethod
    def authenticate() -> tweepy.API:
        # Read Twitter Developer Keys & tokens saved on locally.
        # Please configure your own keys & tokens on my_tokens.py module.
        consumer_key = CONSUMER_KEY
        consumer_secret = CONSUMER_SECRET
        access_token = ACCESS_TOKEN
        access_token_key = ACCESS_TOKEN_KEY
        # Authenticate API.
        # As we can see, our app has limit request of 450 tweets per 15 min.
        authentication = tweepy.OAuthHandler(consumer_key, consumer_secret)
        authentication.set_access_token(access_token, access_token_key)

        # The last parameters handle Twitter API request limit, making the it sleep for a while.
        return tweepy.API(authentication, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    @dispatch(str)
    def get_cursor(self, keyword: str):
        # Making an analogy to Physics, this method would help us get the 'velocity' (likes/h)
        query = '{} lang:pt'.format(keyword)  # Some possible parameters: lang:pt -filter:retweets
        print('Searching for "{}"...'.format(keyword))
        # This part assembles the GET request for the search
        cursor_iterator = tweepy.Cursor(
            self.api.search,
            q=query,
            result_type='recent',
            tweet_mode='extended'
        ).items(MAX_TWEETS_PER_KEYWORD)

        return cursor_iterator

    @dispatch(str, object, object)
    def get_cursor(self, keyword, start_date, end_date):
        # Using the same analogy, this would get us the 'acceleration' (likes/h**2)
        # We won't be using this method, but it's here just in case
        query = '{} lang:pt'.format(keyword)
        cursor_iterator = tweepy.Cursor(
            self.api.search,
            q=query,
            since=start_date,
            until=end_date,
            result_type='recent',
            tweet_mode='extended'
        ).items(MAX_TWEETS_PER_KEYWORD)

        return cursor_iterator
