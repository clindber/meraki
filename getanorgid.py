import sys, getopt, requests, json

p_apikey = ''
p_orgname = ''

def getorgid(p_apikey, p_orgname):
    # looks up org id for a specific org name
    # on failure returns 'null'


    r = requests.get('https://dashboard.meraki.com/api/v0/organizations',
                     headers={'X-Cisco-Meraki-API-Key': p_apikey, 'Content-Type': 'application/json'})

    if r.status_code != requests.codes.ok:
        return 'null'

    rjson = r.json()

    for record in rjson:
        if record['name'] == p_orgname:
            return record['id']
    return ('null')

print(getorgid(p_apikey, p_orgname))
