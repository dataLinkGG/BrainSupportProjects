from twitter_api import *
from pandas import DataFrame, set_option

# Open the Terminal and run
# (venv) C:\Users\thomas\PycharmProjects\TwitterDataRequesterV5>pip install tabulate


def fetch_and_insert_into_csv(keyword, timestamp):
    twitter_section = TwitterAPI()
    cursor_iterator = twitter_section.get_cursor(keyword)
    # All data will be fetched into the folder DATA
    name_table_author = 'DATA/author{}.csv'.format(timestamp)
    name_table_tweet = 'DATA/tweet{}.csv'.format(timestamp)
    name_table_fact = 'DATA/fact{}.csv'.format(timestamp)

    author_name = []
    author_location = []
    author_id = []

    tweet_id = []
    tweet_keyword = []
    tweet_text = []
    tweet_date = []

    fact_id = []
    fact_timestamp = []
    fact_author_id = []
    fact_likes = []
    fact_retweets = []

    for tweet in cursor_iterator:
        # author table
        author_name.append(tweet.author.name)
        author_id.append(tweet.author.id)
        author_location.append(tweet.author.location)
        # tweet table
        tweet_id.append(tweet.id)
        tweet_keyword.append(keyword)
        tweet_text.append((tweet.full_text[:TRUNCATION_AT]).replace('\n', '§'))
        tweet_date.append(tweet.created_at)
        # fact table
        fact_id.append(tweet.id)
        fact_timestamp.append(timestamp)
        fact_author_id.append(tweet.author.id)
        fact_likes.append(tweet.favorite_count)
        fact_retweets.append(tweet.favorite_count)

    data_frame_author = DataFrame({
        'author_id': author_id,
        'author_name': author_name,
        'author_location': author_location
    })

    data_frame_tweet = DataFrame({
        'tweet_id': tweet_id,
        'author name': tweet_keyword,
        'tweet text': tweet_text,
        'tweet date': tweet_date
    })

    data_frame_fact = DataFrame({
        'fact_id': fact_id,
        'fact_timestamp': fact_timestamp,
        'fact_author_id': fact_author_id,
        'fact_likes': fact_likes,
        'fact_retweets': fact_retweets
    })

    set_option('display.expand_frame_repr', False)

    # Select only the top_n tweets.
    # data_author = data_frame_author.loc[data_frame_author.fact_likes.nlargest(TOP_N_TWEETS).index]
    # data_tweet = data_frame_tweet.loc[data_frame_tweet.fact_likes.nlargest(TOP_N_TWEETS).index]
    # data_fact = data_frame_fact.loc[data_frame_fact.fact_likes.nlargest(TOP_N_TWEETS).index]
    # I will comment the following, since it's not really needed
    # data = data.reset_index(drop=True)  # this would be like an 'ORDER BY' in sql

    # Append result to the output file. No header and no index since we're appending it.
    # data_author.to_csv(name_table_author, mode='a', header=False, index=False)
    # data_tweet.to_csv(name_table_tweet, mode='a', header=False, index=False)
    # data_fact.to_csv(name_table_fact, mode='a', header=False, index=False)

    data_frame_author.to_csv(name_table_author, mode='a', header=False, index=False)
    data_frame_tweet.to_csv(name_table_tweet, mode='a', header=False, index=False)
    data_frame_fact.to_csv(name_table_fact, mode='a', header=False, index=False)

    # Optional step. Verbose results.
    print(data_frame_author.to_markdown(tablefmt="grid"))
    print(data_frame_tweet.to_markdown(tablefmt="grid"))
    print(data_frame_fact.to_markdown(tablefmt="grid"))