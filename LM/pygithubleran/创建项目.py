import requests

USER = 'codinguser'
REPO = 'gnucash-android'

url = "https://api.github.com/user/repos"
headers={
    "Accept": "application/vnd.github.v3+json",
    "Authorization":"token 26bcc8aeb5ba2c3d090db892acbc3b5fa6c97d26",
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}
import time

data='{"name":"creatrepositoryin'+str(time.time())+'"'+',' \
     '"description":"create with api",' \
     '"auto_init":"true"}'
r = requests.post(url=url,headers=headers,data=data)
# r = requests.post("http://httpbin.org/post")
# r = requests.put("http://httpbin.org/put")
# r = requests.delete("http://httpbin.org/delete")
# r = requests.head("http://httpbin.org/get")
# r = requests.options("http://httpbin.org/get")

import os
emojis=r.json()

for name,url in emojis.items():
    print name, url
