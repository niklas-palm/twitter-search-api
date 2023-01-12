import os
import tweepy
from aws_lambda_powertools import Logger


# Get Twitter API keys from environment
CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]

# Get query from environment
QUERY = os.environ["QUERY"]

# init logger
logger = Logger()


@logger.inject_lambda_context
def lambda_handler(event, context):

    assert QUERY
    assert CONSUMER_KEY
    assert CONSUMER_SECRET

    # authenticate with the Twitter API
    auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET)

    api = tweepy.API(auth)

    # fetch the most recent tweets
    tweets = api.search_tweets(
        q=QUERY,
        lang="en",
        count=40,
        tweet_mode="extended",
    )

    logger.info("{} tweets returned from API.".format(len(tweets)))

    # print the text of each tweet
    for tweet in tweets:
        if "retweeted_status" in tweet._json:
            # Retweeted tweet
            logger.info(tweet._json["retweeted_status"]["full_text"])
        else:
            # New tweet
            logger.info(tweet.full_text)

    return
