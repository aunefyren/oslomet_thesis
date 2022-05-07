import botometer
import matplotlib.pyplot as plt
from datetime import datetime
from dateutil import tz
import pytz
import json
import os

rapidapi_key = "XXX"
twitter_app_auth = {
    'consumer_key': 'XXX',
    'consumer_secret': 'XXX',
    'access_token': 'XXX',
    'access_token_secret': 'XXX',
  }
bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)


data = []

# Generate array with unique Twitter authors
with open('tweets.json', encoding='utf-8') as file:
    tweets = json.load(file)
    for i, row in enumerate(tweets):
        # Create Datetime object using the syntax Twitter uses, set timezone to UTC
        if not tweets[i]['retweet']:
            user_id = tweets[i]['user_id']
            if user_id not in data:
                data.append(user_id)


# Print the amount of authors found in dataset
print("Proccessed " + str(len(data)) + " authors.")

path = 'botometer'

# Iterate over files in 'botometer replies' directory, checking each file with results
for filename in os.listdir(path):
    f = os.path.join(path, filename)
    # If the path is a file
    if os.path.isfile(f):

        # Go through each user id in current file. If Botometer already has downloaded the data, remove it from the list of accounts to request.
        with open(f, encoding='utf-8') as file:
            file_data = json.load(file)
            if "error" in file_data:
                print("Twitter user ID had error in it.")
                continue
            else:
                if int(file_data["user"]["user_data"]["id_str"]) in data:
                    data.remove(int(file_data["user"]["user_data"]["id_str"]))
                    print("Skipped Twitter user ID: " + file_data["user"]["user_data"]["id_str"])


# For each unique account in the list, call Botometer API and save the result in a file using the author Twitter ID
for screen_name, result in bom.check_accounts_in(data):
    # Write new version of tweets.json
    with open(path + '/' + str(screen_name) + '.json', 'w', encoding="utf8") as file:
        json.dump(result, file)