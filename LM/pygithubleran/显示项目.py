import requests

USER = 'codinguser'
REPO = 'gnucash-android'


headers={
    "Accept": "application/vnd.github.v3+json",
    "Authorization":"token 26bcc8aeb5ba2c3d090db892acbc3b5fa6c97d26",
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}
import time
# url = "https://api.github.com/user/repos"
# data='{"name":"creatrepositoryin'+str(time.time())+'"'+',' \
#      '"description":"create with api",' \
#      '"auto_init":"true"}'
# r = requests.get(url=url,headers=headers)
# # r = requests.post("http://httpbin.org/post")
# # r = requests.put("http://httpbin.org/put")
# # r = requests.delete("http://httpbin.org/delete")
# # r = requests.head("http://httpbin.org/get")
# # r = requests.options("http://httpbin.org/get")
# result=r.json()
# print "there is all  "+str(len(result))+"  repository"
# for i in result:
#     print i['name'], " ",i['language']," ",i['description']
    # for a,b in i.items():
    #     print a,b
url = "https://api.github.com/repos/supermans1201/WeixinBot/languages"
r = requests.get(url=url,headers=headers)
result=r.json()
print result

url="https://api.github.com/users/bitfireAT/repos"
r = requests.get(url=url,headers=headers)
result=r.json()
print "there is all  "+str(len(result))+"  repository"
for i in result:
    print i['name'], " ",i['language']," ",i['description']

url='https://api.github.com/projects/columns/34/cards'
r = requests.get(url=url,headers=headers)
result=r.json()
print result