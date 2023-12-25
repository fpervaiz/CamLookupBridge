import json
import requests

req = requests.get('https://www.lookup.cam.ac.uk/api/v1/inst/COLL?fetch=child_insts',
                   headers={'Accept': 'application/json'})
req.raise_for_status()
data = req.json()

out = []

for inst in data['result']['institution']['childInsts']:
    out.append(inst)
    instId = inst['instId']

    req = requests.get('https://www.lookup.cam.ac.uk/api/v1/inst/' +
                       instId + '?fetch=child_insts', headers={'Accept': 'application/json'})
    req.raise_for_status()
    childData = req.json()

    for childInst in childData['result']['institution']['childInsts']:
        out.append(childInst)

print(json.dumps(out))
