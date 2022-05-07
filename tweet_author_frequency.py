import matplotlib.pyplot as plt
from datetime import datetime
from dateutil import tz
import pytz
import json
import itertools
from datetime import date

last_six_weeks = True
election_date = date.fromisoformat('2021-09-13')
data = {}

# Go through each Tweet in data-set
with open('tweets.json', encoding='utf-8') as file:
    tweets = json.load(file)
    for i, row in enumerate(tweets):
        # Check if retweet
        if not tweets[i]['retweet']:

            # If last_six_weeks is true, skip any Tweet not made within six week of election day
            if last_six_weeks:
                split_tweet_time = tweets[i]['created_at'].split()
                tweet_time = date.fromisoformat(split_tweet_time[0])
                duration = election_date - tweet_time
                duration_in_s = duration.total_seconds()
                days = duration.days
                if days > 42:
                    print("Skipped date: " + tweets[i]['created_at'])
                    continue
                else:
                    print("Didn't skip date: " + tweets[i]['created_at'])

            # Define userID as variable
            user_id = str(tweets[i]['user_id'])

            # Add occurence of userID to dict
            if user_id not in data:
                data[user_id] = 1
            else:
                data[user_id] = data[user_id] + 1


print("Proccessed " + str(len(data)) + " authors.")

# Sort dict and limit to top 25
data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)}
data = dict(itertools.islice(data.items(),25))

authors = list(data.keys())
tweet_count = list(data.values())

print(data.keys())

# Create figure size
fig = plt.figure(figsize = (25, 15))
 
# Add values
plt.bar(authors, tweet_count, color ='red',
        width = 0.4)

# Label and show figure
plt.xlabel("Tweet author user ID")
plt.xticks(rotation=45, fontsize=6)
plt.ylabel("Number of Tweets")
plt.title("Tweet frequency from authors")
plt.show()