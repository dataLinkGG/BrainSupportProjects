import sqlite3
from my_queries import *
from twitter_api import *


class Database:
    def __init__(self, path='database.db'):
        self.location = path

    def connect(self) -> sqlite3.Connection:
        try:
            connection = sqlite3.connect(self.location)
            return connection
        except Exception as e:
            print(e)

    def select_all(self):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(select_all)

        rows = cursor.fetchall()

        for row in rows:
            print(row)

        cursor.close()

    def create_tables(self):
        # This method has to be called only if there's no database
        connection = self.connect()
        cursor = connection.cursor()

        # todo: wouldn't a try catch be better?
        if connection is None:
            print('[ERROR] Failed to connect to the database.')
            exit()

        # Create tables if they DO NOT exist.
        cursor.execute(create_table_fact)
        cursor.execute(create_table_tweet)
        cursor.execute(create_table_author)

        connection.commit()
        connection.close()

    def fetch_and_insert_into_tables(self, keyword, timestamp: int):
        connection = self.connect()
        cursor = connection.cursor()

        # Get tweets containing 'keyword'
        twitter_section = TwitterAPI()
        cursor_iterator = twitter_section.get_cursor(keyword)

        for tweet in cursor_iterator:
            # We should perform insertions starting from the outer to inner scopes
            # insert data into dimension table 'author'

            cursor.execute(insert_into_author, (
                tweet.author.id,
                tweet.author.name,
                tweet.author.location,
            ))
            # insert data into dimension table 'tweet'
            cursor.execute(insert_into_tweet, (
                tweet.id,
                keyword,
                tweet.full_text,
                tweet.created_at,
            ))
            # insert data into fact table 'fact'
            cursor.execute(insert_into_fact, (
                tweet.id,
                timestamp,
                tweet.author.id,
                tweet.favorite_count,
                tweet.retweet_count,
            ))

        connection.commit()
        connection.close()