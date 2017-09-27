import requests

USER = 'codinguser'
REPO = 'gnucash-android'


headers={
    "Accept": "application/vnd.github.v3+json",
    "Authorization":"token 26bcc8aeb5ba2c3d090db892acbc3b5fa6c97d26",
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}
url = "https://api.github.com/repos/codinguser/gnucash-android/pulls"
params={
"state":"all"
}

r = requests.get(url=url,headers=headers,params=params)
result=r.json()
print len(result)
for i in result:
    print i
    # for a,b in i.items():
    #     print a,b
