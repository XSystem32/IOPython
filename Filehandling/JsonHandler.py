import json

data = {}
data['people'] = []
data['people'].append({
    'name': 'Emil',
    'website': 'facebook.com/Emil',
    'from': 'Denmark'
})
data['people'].append({
    'name': 'Henrik',
    'website': 'vk.com/Henrik',
    'from': 'Norway'
})
data['people'].append({
    'name': 'Andrei',
    'website': 'vk.com/Andrei',
    'from': 'Russia'
})

json_example = 'data.json'

with open(json_example, 'r+') as outfile:
    json.dump(data, outfile)

def function(json_object, name):
    for dict in json_object:
        if dict['name'] == name:
            return dict['price']

with open('data.json') as json_file:
    data = json.load(json_file)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')