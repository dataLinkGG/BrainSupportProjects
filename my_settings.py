# Max amount of ( tweets / keyword ) / request
MAX_TWEETS_PER_KEYWORD = 100

# Selection of the TOP_N_TWEETS already fetched
TOP_N_TWEETS = 100

# File path to the given list of keywords
INPUT = 'keywords.txt'

# File path to desired or already existing database
OUTPUT = 'database.db'

# If you would like to truncate a text for being too long:
TRUNCATION_AT = 20
''' 
TRUNCATION_AT = [ -1 | 0 | N ]
Parameters used for tweet_text trunction:
- 1 no truncation (full text) 
- 0 empty string (no text)
- N truncation at the Nth character.
'''