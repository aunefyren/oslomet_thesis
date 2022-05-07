import matplotlib.pyplot as plt
from datetime import datetime
from dateutil import tz
import pytz
import json
import os
import itertools
from datetime import date

last_six_weeks = True
election_date = date.fromisoformat('2021-09-13')
last_six_weeks = True
election_date = date.fromisoformat('2021-09-13')
directory = 'botometer'
number = 0
error = 0
astroturf = 0.0
fake_follower = 0.0
financial = 0.0
other = 0.0
overall = 0.0
self_declared = 0.0
spammer = 0.0

valid_user_ids = []

# If last_six_weeks is true, validate all unique user ID from the data-set who Tweeted within six weeks of the election day
if last_six_weeks:
    with open('tweets.json', encoding='utf-8') as file2:
        tweets = json.load(file2)
        for i, row in enumerate(tweets):
            # Create Datetime object using the syntax Twitter uses, set timezone to UTC
            if not tweets[i]['retweet']:
                split_tweet_time = tweets[i]['created_at'].split()
                tweet_time = date.fromisoformat(split_tweet_time[0])
                duration = election_date - tweet_time
                duration_in_s = duration.total_seconds()
                days = duration.days
                if days > 42:
                    print("Skipped date: " + tweets[i]['created_at'])
                    continue
                else:
                    print('Found Tweet within time frame.')
                    user_id = str(tweets[i]['user_id'])
                    if user_id not in valid_user_ids:
                        valid_user_ids.append(user_id)


# Iterate over files in the Botometer reply directory, checking each file
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # If the path is a file
    if os.path.isfile(f):

        with open(f, encoding='utf-8') as file:
            file_data = json.load(file)

            # Get user ID from the file name
            file_name = file.name.split('.')
            file_name2 = file.name.split('\\')
            file_name3 = file_name2[1].split('.')

            # Validate the user ID if last_six_weeks is true
            if last_six_weeks and file_name3[0] not in valid_user_ids:
                continue

            # If the file contains 'error', ignore it and log the occurence
            if "error" in file_data:
                print("Twitter user ID had error in it.")
                error = error + 1
                continue
            else:
                # Add the different scores from Botometer to the averages
                astroturf = astroturf + file_data['raw_scores']['universal']['astroturf']
                fake_follower = fake_follower + file_data['raw_scores']['universal']['fake_follower']
                financial = financial + file_data['raw_scores']['universal']['financial']
                other = other + file_data['raw_scores']['universal']['other']
                overall = overall + file_data['raw_scores']['universal']['overall']
                self_declared = self_declared + file_data['raw_scores']['universal']['self_declared']
                spammer = spammer + file_data['raw_scores']['universal']['spammer']
                number = number + 1
                
                any_takes = False
                
                # if any category is above 0.8, output it to the console
                if file_data['raw_scores']['universal']['astroturf'] > 0.8:
                    print(str(file_name3[0]) + ": astroturf - " + str(file_data['raw_scores']['universal']['astroturf']))
                    any_takes = True
                
                if file_data['raw_scores']['universal']['fake_follower'] > 0.8:
                    print(str(file_name3[0]) + ": fake_follower - " + str(file_data['raw_scores']['universal']['fake_follower']))
                    any_takes = True

                if file_data['raw_scores']['universal']['financial'] > 0.8:
                    print(str(file_name3[0]) + ": financial - " + str(file_data['raw_scores']['universal']['financial']))
                    any_takes = True
                
                if file_data['raw_scores']['universal']['other'] > 0.8:
                    print(str(file_name3[0]) + ": other - " + str(file_data['raw_scores']['universal']['other']))
                    any_takes = True

                if file_data['raw_scores']['universal']['overall'] > 0.8:
                    print(str(file_name3[0]) + ": overall - " + str(file_data['raw_scores']['universal']['overall']))
                    any_takes = True

                if file_data['raw_scores']['universal']['self_declared'] > 0.8:
                    print(str(file_name3[0]) + ": self_declared - " + str(file_data['raw_scores']['universal']['self_declared']))
                    any_takes = True

                if file_data['raw_scores']['universal']['spammer'] > 0.8:
                    print(str(file_name3[0]) + ": spammer - " + str(file_data['raw_scores']['universal']['spammer']))
                    any_takes = True

                if any_takes:
                    print('________________________')


# Print the results
print('Processed ' + str(number) + ' users.')
print(str(error) + ' errors.')
print('________________________')
print('astroturf: ' + str(format(astroturf / number, '.2f')))
print('fake_follower: ' + str(format(fake_follower / number, '.2f')))
print('financial: ' + str(format(financial / number, '.2f')))
print('other: ' + str(format(other / number, '.2f')))
print('overall: ' + str(format(overall / number, '.2f')))
print('self_declared: ' + str(format(self_declared / number, '.2f')))
print('spammer: ' + str(format(spammer / number, '.2f')))