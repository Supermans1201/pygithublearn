import requests
def getlink(rlink):
    import re
    p=re.compile('<.*?>')
    m=re.findall(p,rlink)
    m2=[re.sub('<|>','',x) for x in m]
    return m2
def getallcommit(url = "https://api.github.com/repos/codinguser/gnucash-android/issues"):
    allcommitsha=[]
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": "token 26bcc8aeb5ba2c3d090db892acbc3b5fa6c97d26",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    }
    params = {
        "state": "all"
    }
    i=0
    while True:
        i+=1
        print i
        response = requests.get(url=url, headers=headers, params=params)
        rlink = response.headers['link']
        results = response.json()
        for result in results:
            allcommitsha.append(result['number'])
        m=getlink(rlink)
        url=m[0]
        if m[0]==m[1]:
            break
    print len(allcommitsha)
    return allcommitsha

allissuesnum=getallcommit()
print allissuesnum
fileObject = open('allissuesnum.txt', 'w')
for num in allissuesnum:
    print num
    fileObject.write(str(num))
    fileObject.write('\n')
fileObject.close()


