import matplotlib.pyplot as plt
from datetime import datetime
from dateutil import tz
import pytz
import json

# Create class for creating Twitter account objects
class Author(object):
    pass

# Define empty array of accounts
authors = []

# Generate variables with Tweet-time found in Tweets within tweets.json
with open('tweets.json', encoding='utf-8') as file:
    tweets = json.load(file)
    for i, row in enumerate(tweets):
        # Check each Tweet
        if not tweets[i]['retweet']:
            
            # Define variables from Tweet
            user_id = str(tweets[i]['user_id'])
            likes_count = tweets[i]['likes_count']
            retweets_count = tweets[i]['retweets_count'] + 1

            # Look for account in array
            author_index = False
            for index,author in enumerate(authors):
                if authors[index].user_id == user_id:
                    author_index = index

            # If not found, create new Author object with variables
            if author_index is False:
                author = Author()
                author.user_id = user_id
                author.likes = likes_count
                author.retweets = retweets_count
                author.tweets = 1
                authors.append(author)
            else:
                # If author exists, apply variables to the existing object
                authors[author_index].likes = likes_count + authors[author_index].likes
                authors[author_index].retweets = retweets_count + authors[author_index].retweets
                authors[author_index].tweets = authors[author_index].tweets + 1


# Utilize the formula for engagement on each object in account array
data = {}
for author in authors:
    data[author.user_id] = (author.likes + author.retweets * 2) / author.tweets


# Sort array and limit to the top 25
while len(data) > 25:
    key_min = min(data.keys(), key=(lambda k: data[k]))
    data.pop(key_min)


data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)}

print(data.keys())

authors = list(data.keys())
tweet_count = list(data.values())

# Create figure size
fig = plt.figure(figsize = (25, 15))
 
# Add values
plt.bar(authors, tweet_count, color ='green',
        width = 0.4)

# Label and show figure
plt.xlabel("Tweet author user ID")
plt.xticks(rotation=45, fontsize=5)
plt.ylabel("(Like sum + Retweet sum x 2) / Tweet count")
plt.title("Tweet engagement by authors")
plt.show()