import requests

USER = 'codinguser'
REPO = 'gnucash-android'


headers={
    "Accept": "application/vnd.github.v3+json",
    # "Authorization":"token 26bcc8aeb5ba2c3d090db892acbc3b5fa6c97d26",
    "Authorization": "token a79e595be6add51ba45bfdeef4db0b5ff55fd862",
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}
import time
url = "https://api.github.com/repos/supermans1201/1234/issues"
data="""
{
  "title": "Found a bug",
  "body": "I'm having a problem with this.",
  "labels": [
    "fun","bug"
  ]
}
"""
r = requests.post(url=url,headers=headers,data=data)
result=r.json()
print result


url="https://api.github.com/repos/supermans1201/1234/issues/1/comments"
data="""
{
  "body": "Me too"
}
"""
r = requests.post(url=url,headers=headers,data=data)
result=r.json()
print result