import os
import json
from thefuzz import fuzz
import itertools
import math
from alive_progress import alive_bar

master_count = 0
count = 0
keywords = ['innvandring', 'abort', 'klima', 'skole', 'velferd', 'rusreform']

# Loop through each keyword, looking for topics to check for plagiarism within
for keyword in keywords:
    print('Searching for: ' + keyword)
    filtered_tweets = []

    # Loop through every Tweet in data-set and look for Tweets which contains our keyword
    with open('tweets.json', encoding='utf-8') as file:
        tweets = json.load(file)
        for i, row in enumerate(tweets):
            if tweets[i]['retweet']:
                continue

            if keyword not in tweets[i]['tweet'].lower():
                continue

            filtered_tweets.append(tweets[i])


    # Calculate the number of combinations of Tweets to check
    combinations = math.factorial(len(filtered_tweets)) // math.factorial(2) // math.factorial(len(filtered_tweets)-2)
    print('Doing ' + str(combinations) + ' combinations.')

    # Generate progress bar
    with alive_bar(combinations) as bar:
        # Go through every unique combinations of Tweets to check
        for tweet_a, tweet_b in itertools.combinations(filtered_tweets, 2):

            count = count + 1
            
            # Check the plagiarism ratio
            ratio = fuzz.ratio(tweet_a['tweet'], tweet_b['tweet'])
            
            # Save if ratio is above 80
            if ratio > 80:
                #print('Found Tweets with ratio: ' + str(ratio))
                with open('compared_tweets/' + keyword + '_' + str(tweet_a['id']) + '_' + str(tweet_b['id']) + '_' + str(ratio) + '.txt', 'w', encoding="utf8") as new_file:
                    new_file.write(tweet_a['username'] + ': ' + tweet_a['tweet'] + "\n" + tweet_b['username'] + ': ' + tweet_b['tweet'])

            bar()


print('Complete.')