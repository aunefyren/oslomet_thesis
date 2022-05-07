import matplotlib.pyplot as plt
from datetime import datetime
from dateutil import tz
import pytz
import json
import pandas as pd
import networkx as nx
import scipy

users = []
tweet_list = []
G = nx.Graph()

# Go through each Tweet in data-set
with open('tweets.json', encoding='utf-8') as file:
    tweets = json.load(file)
    for i, row in enumerate(tweets):
        # Check if not retweet and stop a sub 1000 for testing purposes
        if not tweets[i]['retweet'] and i < 1000:

            user_id = str(tweets[i]['user_id'])

            if user_id not in users:
                users.append(user_id)

            for mentioned in tweets[i]['mentions']:
                if mentioned['id'] not in users:
                    users.append(mentioned['id'])

            tweet_list.append(tweets[i])


for tweet in tweet_list:
    for mentioned in tweet['mentions']:
        G.add_edge(tweet['user_id'], mentioned['id'], weight=10 )


nx.draw_networkx(G, pos=None, arrows=None, with_labels=False)

plt.show()  