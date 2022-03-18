# import required module
import os
import json

# Assign variables
directory = 'tweets'
tweets_proccessed = 0
 
# Iterate over files in tweets directory, checking each file
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # If the path is a file
    if os.path.isfile(f):

        # Generate list of ID's already in masterfile, tweets.json
        id_array = []
        with open('tweets.json', encoding='utf-8') as file:
            tweets = json.load(file)
            for i, row in enumerate(tweets):
                id_array.append(tweets[i]['id'])
        
        # Go through each Tweet in current file
        with open(f, encoding='utf-8') as file:
            data = json.load(file)
            tweets_proccessed = tweets_proccessed + len(data)

            # Loop through each Tweet in file
            for i, row in enumerate(data):
                found = False
                
                # Check for the Tweet ID in the already established ID array
                for j in id_array:
                    if j == data[i]['id']:
                        found = True
                        break
                
                # If not found in the ID list, add to master file
                if not found:
                    tweets.append(data[i])
        
        # Write new version of tweets.json
        with open('tweets.json', 'w', encoding="utf8") as file:
            json.dump(tweets, file)


# Sort final array using created_at
tweets.sort(key=lambda x: x["created_at"])

# Write new sorted version of tweets.json
with open('tweets.json', 'w', encoding="utf8") as file:
    json.dump(tweets, file)


# Print some stats of Tweets
print('Induvidual Tweets proccessed: ', tweets_proccessed)
print('Final Tweet count: ', len(tweets))
print('Tweet duplicates found: ', (tweets_proccessed-len(tweets)))