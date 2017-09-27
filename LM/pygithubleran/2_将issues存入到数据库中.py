import requests

headers={
    "Accept": "application/vnd.github.v3+json",
    "Authorization":"token 26bcc8aeb5ba2c3d090db892acbc3b5fa6c97d26",
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}
url = "https://api.github.com/repos/codinguser/gnucash-android/issues"
params={
"state":"all"
}
from pymongo import MongoClient
def openmongdb(dbname='codinguser_gnucash-android',collname='issues'):
    client = MongoClient()
    db = client[dbname]
    coll = db[collname]
    return coll
coll=openmongdb()

def getlink(rlink):
    import re
    p=re.compile('<.*?>')
    m=re.findall(p,rlink)
    m2=[re.sub('<|>','',x) for x in m]
    return m2

while True:
    r = requests.get(url=url, headers=headers, params=params)
    rlink = r.headers['link']
    result = r.json()
    print len(result)
    for i in result:
        print i['number'],r
        coll.insert(i)
    m=getlink(rlink)
    url=m[0]
    if m[0]==m[1]:
        break
