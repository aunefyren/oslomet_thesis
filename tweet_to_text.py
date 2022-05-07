import json

count = 0

# Go through every Tweet in the data-set
with open('tweets.json', encoding='utf-8') as file:
    tweets = json.load(file)
    for i, row in enumerate(tweets):
        # Skip retweets
        if not tweets[i]['retweet']:
            tweet_id = str(tweets[i]['id'])
            tweet_body = tweets[i]['tweet']
            # Save the Tweet to a TXT file
            with open('tweet_text/' + tweet_id + '.txt', 'w') as f:
                f.write('tweet_body')
                count = count + 1


print('Finished writing ' + str(count) + ' tweets.')

