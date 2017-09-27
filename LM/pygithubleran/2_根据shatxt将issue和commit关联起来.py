import requests
def getshafromtxt():
    allcommitsha=[]
    f = open("allcommitsha.txt")
    line = f.readline()
    while line:
        allcommitsha.append(line)
        line = f.readline()
    f.close()
    return allcommitsha
def getcommitdetil(user="codinguser",repo="gnucash-android",sha="daf2e8ba4261d19b4b3c4eebee5a61773c86632b"):
    headers={
        "Accept": "application/vnd.github.VERSION.patch",
        "Authorization":"token 26bcc8aeb5ba2c3d090db892acbc3b5fa6c97d26",
        "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    }
    url = "https://api.github.com/repos/"+user+"/"+repo+"/commits/"+sha
    print url
    r = requests.get(url=url, headers=headers)
    print r
    return r.text
allcommitsha=getshafromtxt()
i =1
for sha in allcommitsha:
    print i,sha[:-1],
    i+=1
    r= getcommitdetil(sha=sha[:-1])
    # print r
    fileObject = open('F:/LM/pygithub_leran/diff/'+sha[:-1]+'.txt', 'w')
    fileObject.write(r.encode('ascii', 'ignore').decode('ascii'))
    fileObject.close()
