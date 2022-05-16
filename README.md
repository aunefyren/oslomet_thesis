# Analyzing automated activity and social deception on Twitter during the 2021 Norwegian election
These are the scripts and files utilized in my master thesis. The data set is not included, but can be recreated using the code.

## Explainations:

### add_commas.py
When "Twint" generated the JSON files used for the data set, the files were not in the standard JSON format. Each JSON line was a unique Tweet, but there were no brackets wrapping them, and no commas in-between. This Python script added a comma to every line, except the last one. Then brackets are added to each end of the file.

### combine_unique_json.py
When Tweets were collected by "Twint" they were stored in individual files, based on the current keyword in use. This script goes through every JSON file in the folder, collects the Tweets, removes duplicates, and saves the final data set to a new final file.

### download_tweets.py
This Python script utilizes "Twint" to scrape Tweets from Twitter. The script loads the CSV file containing search strings (keyword), collects every Tweet it applies to within the correct time frame and saves all the results to a file.

### generate_word_cloud.py
As an attempt to visualize the conversation, this Python script collects every word in every Tweet in the data set. Some words from predefined lists are filtered out. Then a visual word cloud is generated, where each occurrence of a word grows its size. The word cloud takes the form of a Norwegian flag and is then displayed.

### tweet_author_botometer.py
This script collects every unique Twitter user ID from the data set, retrieves their Botometer scores using their API, and then saves the result to a file. It also checks the saving-directory for Botometer scores before attempting to retrieve scores from Botometer, skipping additional downloads in case of multiple script executions. If Botometer already gave a score, but the result was an error, it retries to fetch the scores.

### tweet_author_engagement.py
As an attempt to visualize engagement, each user in the data set has an engagement score calculated. The script retrieves every Tweet in the data set and saves certain data for each unique Twitter user. The amount of Tweets, likes received, and retweets received. This generates a score for the user where the sum of likes and the sum of retweets times two are divided by the sum of Tweets. The users are then sorted by most engagement and the top 25 users are displayed in descending order.

### tweet_author_frequency.py
As an attempt to visualize activity, each user is ranked by Tweet activity. The script retrieves every Tweet in the data set and gives every user point for each Tweet published. The users are then sorted by most Tweets and the top 25 users are displayed in descending order.

### tweet_author_relation.py
As an attempt to visualize relations, each user is displayed on a network figure using nodes, and each mention of another user (node), draws a line between them. The script retrieves every Tweet in the data set, creating a node for each user. Then every Tweet is examined again, drawing lines from Tweet authors to other nodes using the "mention" metadata tag in the Tweet. The final figure is then displayed using "networkx".

### tweet_botometer_average.py
As an attempt to visualize Botometer scores, every Botometer reply is calculated into averages. The script retrieves every Botometer reply in the data set, and adds every category score, while also increasing the increment. Every time a score is above 0.8 it is also printed to the console for manual inspection. The averages are at the end printed to the console.

### tweet_domain_frequency.py
As an attempt to visualize sharing activity, each domain is ranked by Tweet occurrence. The script retrieves every Tweet in the data set, and gives finds every domain from the "urls" metadata tag. Each URL is cleaned using "urlparse" and saved. Each time it occurs it gains one point. The domains are then sorted by most occurrences and the top 25 domains are displayed in descending order.

### tweet_plagiarism.py
In an attempt to investigate the automated activity, Tweets within certain categories are checked against each other for plagiarism. The script retrieves every Tweet in the data set which matches the current keyword and uses "itertools" to create every unique combination of the Tweets. Each Tweet is then compared using "thefuzz", providing a match ratio between 0 and 100. If the match is above 80, the Tweets are saved with relevant metadata for manual inspection.

### tweet_search.py
A some points certain items within the data set had to be inspected, but the text files were too big to be managed through a text editor. This simple Python script searched for certain predetermined variables in the data set and printed them to the console for inspection.

### tweet_time_bar.py
As an attempt to visualize user activity, each Tweet is mapped into a bar chart showing each hour in a day. The script retrieves every Tweet in the data set and converts the time from the metadata into the Norwegian time zone. The hour that the Tweet was published is then extracted and one point is given to the corresponding bar in the bar chart. The hours are then displayed in the bar chart, showing how much activity occurs in each hour.

### tweet_to_text.py
This script ended up not being needed, but it was created for a plagiarism approach. It iterated through every Tweet in the data set and saved the Tweet text to a unique file named after the Tweet ID.
