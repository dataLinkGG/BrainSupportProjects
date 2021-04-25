# Twitter API Data Requester V5

This software intends to fetch & treat data into a Data Warehouses model, for reports generation. Such reports will be generated with Power BI, so we just tried to ensure the data is correctly collected, treated and saved using the tweet search requests v1.1.

[https://api.twitter.com/1.1/search/tweets.json][Tweet Requests V1.1]

## Modules
##### 1) main
This serves as a driver for our program. All the classes, methods and functions are described bellow.
##### 2) credentials
A file with containing generated tokens. You will have to provide your own tokens, which can be generated using an App on a Twitter Developer account.

[https://developer.twitter.com/en/docs/apps/overview][Twitter Developer Account]
##### 3) keywords
A static list of words in .txt format save locally.

This list has been made based on analyses with Google Analytics, listing the most common terms that directed users to our website.
##### 4) parameters
Parameters to be set by the user of this software, which may influence in the type of search.
##### 5) queries
Here, you can set the SQLite3 queries to be used by this program to manage the database.

[Tweet Requests V1.1]: https://api.twitter.com/1.1/search/tweets.json

[Twitter Developer Account]: https://developer.twitter.com/en/docs/apps/overview