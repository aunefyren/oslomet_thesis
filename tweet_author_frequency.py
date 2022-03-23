import matplotlib.pyplot as plt
from datetime import datetime
from dateutil import tz
import pytz
import json

data = {}

# Generate variables with Tweet-time found in Tweets within tweets.json
with open('tweets.json', encoding='utf-8') as file:
    tweets = json.load(file)
    for i, row in enumerate(tweets):
        # Create Datetime object using the syntax Twitter uses, set timezone to UTC
        if not tweets[i]['retweet']:
            user_id = str(tweets[i]['user_id'])
            if user_id not in data:
                data[user_id] = 1
            else:
                data[user_id] = data[user_id] + 1


while len(data) > 25:
    key_min = min(data.keys(), key=(lambda k: data[k]))
    data.pop(key_min)


data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)}

authors = list(data.keys())
tweet_count = list(data.values())

# Create figure size
fig = plt.figure(figsize = (25, 15))
 
# Add values
plt.bar(authors, tweet_count, color ='red',
        width = 0.4)

# Label and show figure
plt.xlabel("Tweet author user ID")
plt.xticks(rotation=90)
plt.ylabel("Number of Tweets")
plt.title("Tweet frequency from authors")
plt.show()