def getnumfromtxt():
    allcommitsha=[]
    f = open("allissuesnum.txt")
    line = f.readline()
    while line:
        allcommitsha.append(line)
        line = f.readline()
    f.close()
    return allcommitsha

import requests
def getcommitdetil(user="codinguser", repo="gnucash-android", num="42"):
    headers={
        "Accept": "application/vnd.github.v3+json",
        "Authorization":"token 26bcc8aeb5ba2c3d090db892acbc3b5fa6c97d26",
        "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    }

    url = "https://api.github.com/repos/"+user+"/"+repo+"/issues/" + num+"/comments"
    print url
    r = requests.get(url=url, headers=headers)
    print r
    return r.json()

from pymongo import MongoClient
def openmongdb(dbname='codinguser_gnucash-android',collname='comments'):
    client = MongoClient()
    db = client[dbname]
    coll = db[collname]
    return coll

coll=openmongdb()
allissuenum=getnumfromtxt()
i =1
for num in allissuenum:
    print i, num[:-1],
    i+=1
    r= getcommitdetil(num=num[:-1])
    print r
    for comment in r:
        comment["issue"]=num[:-1]
        coll.insert(comment)