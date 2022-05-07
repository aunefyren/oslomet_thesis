import matplotlib.pyplot as plt
from datetime import datetime
from dateutil import tz
import pytz
import json
from urllib.parse import urlparse

data = {}

# Iterate through each Tweet in data-set
with open('tweets.json', encoding='utf-8') as file:
    tweets = json.load(file)
    for i, row in enumerate(tweets):
        # Check if retweet
        if not tweets[i]['retweet']:
            # Find each URL, clean it, and save it with occurence
            urls = tweets[i]['urls']
            for url in urls:
                domain = urlparse(str(url)).netloc
                if 'www.' in domain:
                    domain = domain.replace('www.','')
                if domain not in data:
                    data[domain] = 1
                else:
                    data[domain] = data[domain] + 1


# Sort dict and limit to top 25
while len(data) > 25:
    key_min = min(data.keys(), key=(lambda k: data[k]))
    data.pop(key_min)


data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)}

authors = list(data.keys())
tweet_count = list(data.values())

# Create figure size
fig = plt.figure(figsize = (25, 15))
 
# Add values
plt.bar(authors, tweet_count, color ='yellow',
        width = 0.4)

# Label and show figure
plt.xlabel("Domain (does not include subdomain)")
plt.xticks(rotation=45, fontsize=8)
plt.ylabel("Number of links")
plt.title("Frequency of domains shared in Tweets")
plt.show()