import matplotlib.pyplot as plt
from datetime import datetime
from dateutil import tz
from datetime import date
import pytz
import json

hours = ['00:00+', '01:00+', '02:00+', '03:00+', '04:00+', '05:00+', '06:00+', '07:00+', '08:00+', '09:00+', '10:00+', '11:00+', '12:00+', '13:00+', '14:00+', '15:00+', '16:00+', '17:00+', '18:00+', '19:00+', '20:00+', '21:00+', '22:00+', '23:00+']
tweet_hours = [0] * 24
from_zone = tz.gettz('UTC')
to_zone = tz.gettz('Europe/Oslo')
last_six_weeks = True
election_date = date.fromisoformat('2021-09-13')

# Generate variables with Tweet-time found in Tweets within tweets.json
with open('tweets.json', encoding='utf-8') as file:
    tweets = json.load(file)
    for i, row in enumerate(tweets):
        if not tweets[i]['retweet']:

            # If enabled, skip Tweets not made within six weeks of election day
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


            # Create Datetime object using the syntax Twitter uses, set timezone to UTC
            created_at = datetime.strptime(tweets[i]['created_at'], "%Y-%m-%d %H:%M:%S %Z")
            created_at = created_at.replace(tzinfo=from_zone)

            # Convert to GMT+1
            created_at = created_at.astimezone(to_zone)
            
            # Add one Tweet to the related hour
            tweet_hours[int(created_at.hour)] = tweet_hours[int(created_at.hour)] + 1


print(tweet_hours)

# Create figure size
fig = plt.figure(figsize = (25, 5))
 
# Add values
plt.bar(hours, tweet_hours, color ='blue',
        width = 0.4)

# Label and show figure
plt.xlabel("Hours Tweeted")
plt.ylabel("Number of Tweets")
plt.title("Hour Tweeted in GMT+1")
plt.show()