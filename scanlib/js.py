import json

def jsd(filename, json_data):
    with open('{}.json'.format(filename), 'w') as fp:
        json.dump(json_data, fp, indent=True)

def pdata(need, s):
    data = {}
    for k, v in s.items():
        if k in need:
            data[k] = v

    return data
