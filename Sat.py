import json

with open('rewardAdSource.json', 'r') as file:
    data = json.load(file)

with open('dictionary.json', 'r') as file:
    comp = json.load(file)

# counter = 0

# for i, e in enumerate(data):
#     if e['word'] == comp[i]['word']:
#             counter += 1


for e in data:
    j = 0
    for ee in data[e]:
        data[e][j] = {
            "id": j+1,
            "word": ee['word'],
            "translate": ee['translate'],
            "TabsBar": "Sedang Dipelajari"
        }
        j += 1


with open('rewardAdSource.json', 'w') as file:
    json.dump(data, file, indent=4)
