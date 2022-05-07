import matplotlib.pyplot as plt
from datetime import datetime
from dateutil import tz
import pytz
import json
from urllib.parse import urlparse

# Select Twitter user ID to seacrh for
search_term_id = 0000000  

# Go through each Tweet in data-set
with open('tweets.json', encoding='utf-8') as file:
    tweets = json.load(file)
    for i, row in enumerate(tweets):
        # Check if Tweet is retweet
        if not tweets[i]['retweet']:
            if tweets[i]['user_id'] == search_term_id:
                # Print Tweets made by the user ID
                print(tweets[i]['username'] + ": " + tweets[i]['tweet'])
                print("_________________________")
                continue
            