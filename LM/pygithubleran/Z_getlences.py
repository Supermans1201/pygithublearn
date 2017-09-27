import requests


headers={
    "Accept": "application/vnd.github.drax-preview+json",
    "Authorization":"token 26bcc8aeb5ba2c3d090db892acbc3b5fa6c97d26",
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}
url = "https://api.github.com/repos/"
user_repo="/moby/moby"
map={}
def getlanguage(user_repo=user_repo):
    url2=url+user_repo

    r2=requests.get(url=url2,headers=headers)
    result2=r2.json()
    # print result2
    key=result2["license"]["spdx_id"]
    map[key]=map.get(key,0)+1

    theresult = (user_repo,key)
    return theresult


def getxiangmufromtxt():
    allcommitsha=[]
    f = open("all2.txt")
    line = f.readline()
    while line:
        allcommitsha.append(line)
        line = f.readline()
    f.close()
    return allcommitsha
thexiangmus=getxiangmufromtxt()
allresult=[]
i=0;
for xiangmu in thexiangmus:
    user_repo="".join(xiangmu.replace("\n",""))
    i += 1;
    try:
        allresult.append(getlanguage(user_repo=user_repo))
    except:
        allresult.append((user_repo,"exception",sum))
        print "exception",i

    print i


import csv
with open("F:/LM/xiangmu/all_licenses.csv", 'w') as f:
    f.write('\xEF\xBB\xBF')
    writer = csv.writer(f)
    writer.writerows(allresult)

print map