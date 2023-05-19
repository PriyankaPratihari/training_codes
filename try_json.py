import json

# Opening JSON file
f = open('text.json')

# returns JSON object as
# a dictionary
data = json.load(f)
f.close()
data_store = []
# Iterating through the json
# list
datas = data['parametersList']
for item in datas:
    # print(item['parameterName'])
    myDict = {
        "parameterName": item['parameterName'],
        "min_value": item['min'],
        "max_value": item['max'],
        "avg_value": item['avg']
    }
    data_store.append(myDict)

print(data_store)
json_object = json.dumps(data_store, indent=4)

# Writing to sample.json
with open("ans.json", "w") as outfile:
    outfile.write(json_object)
