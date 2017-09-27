
from pymongo import MongoClient
def openmongdb():
    client = MongoClient()
    db = client['androidbug']
    coll = db['commits']
    return coll

import requests
def getcommitdetil(user="codinguser",repo="gnucash-android",sha="daf2e8ba4261d19b4b3c4eebee5a61773c86632b"):
    headers={
        "Accept": "application/vnd.github.v3+json",
        "Authorization":"token 26bcc8aeb5ba2c3d090db892acbc3b5fa6c97d26",
        "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    }
    url = "https://api.github.com/repos/"+user+"/"+repo+"/commits/"+sha
    r = requests.get(url=url, headers=headers)
    return r.json()

coll=openmongdb()
r= getcommitdetil()
coll.insert(r)