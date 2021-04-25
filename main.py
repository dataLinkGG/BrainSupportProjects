from datetime import datetime
from into_database import *
from into_csv import *


class Problem:
    def __init__(self):
        self.file_keyword_lst = INPUT
        self.file_database = OUTPUT

    def _read_keywords(self) -> [str]:
        try:
            # Return a list of keywords saved in the folder of this project.
            with open(self.file_keyword_lst, 'r') as file:
                # removes blanks at the end (e.g.: ' python ' -> ' python')
                keyword_lst = [line.rstrip() for line in file]
        except IOError as e:
            # [ERROR] No such file or directory: keywords.txt
            print('[ERROR] {}: {}'.format(e.args[1], self.file_keyword_lst))
            exit()
        return keyword_lst

    @staticmethod
    def _get_current_timestamp():
        now = datetime.utcnow()
        # Since we will be fetching data N times a day, minutes and seconds are not so important
        current_time_grained_to_hours = datetime(now.year, now.month, now.day, now.hour, 0, 0)
        return int(current_time_grained_to_hours.strftime("%Y%m%d%H"))  # e.g.: 2021021224

    def iterate_keywords(self):
        keyword_lst = self._read_keywords()
        # UNCOMMENT FOR DATABASE USAGE
        # database = Database(self.file_database)
        # database.create_tables()  # if not exist
        # We need to know WHEN a tweet had N likes
        timestamp = self._get_current_timestamp()
        if not keyword_lst:
            print('[ERROR] Empty list! Empty file?')
            exit()
        for keyword in keyword_lst:
            # todo: code a decision maker for database or table
            # UNCOMMENT FOR DATABASE USAGE
            # database.fetch_and_insert_into_tables(keyword, timestamp)
            # UNCOMMENT FOR TABLES USAGE
            fetch_and_insert_into_csv(keyword, timestamp)


if __name__ == '__main__':
    backend = Problem()
    Problem.iterate_keywords(backend)

    # test = Database(OUTPUT)
    # test.select_all()

