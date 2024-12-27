import json

with open('rewardAdSource.json', 'r') as file:
    data = json.load(file)

with open('dictionary.json', 'r') as file:
    comp = json.load(file)

# counter = 0

# for i, e in enumerate(data):
#     if e['word'] == comp[i]['word']:
#             counter += 1


for i, e in enumerate(data):
    data[i] = {
        "id": i+1,
        "word": e['word'],
        "translate": e['translate'],
        "TabsBar": "Sedang Dipelajari"
    }


with open('rewardAdSource.json', 'w') as file:
    json.dump(data, file, indent=4)
