import json

new_array = []
count = 0

with open('tweets.json', encoding='utf-8') as file:
    data = json.load(file)
    for i, row in enumerate(data):
        if '2021' in data[i]['date']:
            print(data[i]['date'])
            new_array.append(data[i])
            count = count + 1
            

print(count)

# and write everything back
with open('tweets.json', 'w', encoding="utf8") as file:
    json.dump(new_array, file)