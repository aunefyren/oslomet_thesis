import json

new_array = []
count = 0

# Count Tweets containing '2021' and save them to a new array
with open('tweets.json', encoding='utf-8') as file:
    data = json.load(file)
    for i, row in enumerate(data):
        if '2021' in data[i]['date']:
            print(data[i]['date'])
            new_array.append(data[i])
            count = count + 1
            

print(count)

# Write the new array back to the orginal file
with open('tweets.json', 'w', encoding="utf8") as file:
    json.dump(new_array, file)