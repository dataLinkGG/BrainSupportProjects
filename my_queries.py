'''
    Free free to write your own custom queries here.
    Just remember to assign them as variables here and
    check the module where they are used (database.py)
'''

create_table_fact = """
CREATE TABLE IF NOT EXISTS fact (
    tweet_id integer NOT NULL,
    timestamp integer NOT NULL,
    author_id integer NOT NULL,
    favorite_count integer,
    retweet_count integer,
    PRIMARY KEY (tweet_id, timestamp),
    FOREIGN KEY (tweet_id) REFERENCES tweet (id),
    FOREIGN KEY (author_id) REFERENCES author (id)
);
"""

create_table_tweet = """
CREATE TABLE IF NOT EXISTS tweet (
    id integer PRIMARY KEY,
    keyword text,
    content text,
    creation_time text
);
"""

create_table_author = """
CREATE TABLE IF NOT EXISTS author (
    id integer PRIMARY KEY,
    name text NOT NULL UNIQUE,
    location text
);
"""

insert_into_fact = """
INSERT OR IGNORE INTO fact (tweet_id,timestamp,author_id,favorite_count,retweet_count) VALUES (?,?,?,?,?);
"""

insert_into_tweet = """
INSERT OR IGNORE INTO tweet (id,keyword,content,creation_time) VALUES (?,?,?,?);
"""

insert_into_author = """
INSERT OR IGNORE INTO author (id,name,location) VALUES (?,?,?);
"""

select_all = """
    SELECT *
    FROM fact
    INNER JOIN tweet on fact.tweet_id = tweet.id
    INNER JOIN author on fact.author_id = author.id
    ORDER BY tweet.keyword, tweet.id;
"""

report1 = """
    SELECT fact.tweet_id as 'Tweet_ID',
    fact.timestamp as 'timestamp',
    substr(fact.timestamp,1,4) as 'Yaar',
    substr(fact.timestamp,5,2) as 'Month',
    substr(fact.timestamp,7,2) as 'Day',
    substr(fact.timestamp,9,2) as 'Hour',
    tweet.content,
    tweet.keyword
    FROM fact
    INNER JOIN tweet on fact.tweet_id = tweet.id
    INNER JOIN author on fact.author_id author.id
    ORDER BY tweet.keyword, tweet.id;
"""