import pandas as pd
import twint
import datetime
start_date = datetime.date(2021, 1, 1)
end_date = datetime.date(2021, 9, 15)

# Read the CSV file containing search strings, and loop through each one
df = pd.read_csv('search_terms.csv', encoding = 'utf8', sep=';')
for index, row in df.iterrows():
    print('Searching for: ', row['search'])

    c = twint.Config()

    c.Store_json = True
    c.Count = True
    c.Stats = True
    c.Store_object = True
    c.User_full = True

    # Define search to use current string and limit the search to within the time frame
    c.Search = row['search']
    c.Since = start_date.strftime('%Y-%m-%d') + ' 00:00:00'
    c.Until = end_date.strftime('%Y-%m-%d') + ' 00:00:00'

    # Perform a search and save the results in a unique file
    c.Output = "tweets/tweets_term_" + str(index) + ".json"
    twint.run.Search(c)