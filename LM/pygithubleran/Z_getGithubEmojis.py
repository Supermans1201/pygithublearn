import requests


headers={
    "Accept": "application/vnd.github.v3+json",
    "Authorization":"token 26bcc8aeb5ba2c3d090db892acbc3b5fa6c97d26",
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}
url = "https://api.github.com/repos"
user_repo="/moby/moby"

url1=url+user_repo
r = requests.get(url=url1, headers=headers)

result = r.json()
print "full_name",result["full_name"]
print "language",result["language"]
print "size",result["size"]
print "description",result["description"]
print "homepage",result["homepage"]
print "html_url",result["html_url"]
print "forks_count",result["forks_count"]
print "watchers_count",result["watchers_count"]
print "open_issues_count",result["open_issues_count"]
print "subscribers_count",result["subscribers_count"]

url2=url1+"/languages"
r2=requests.get(url=url2)
result2=r2.json()
sum=0
string=""
for key in result2:
    string+="("+key+", "
    string+=str(result2[key])+"), "
    sum+=result2[key]
print "languages",string
print "lines",sum



# while True:
#     r = requests.get(url=url, headers=headers, params=params)
#     rlink = r.headers['link']
#     result = r.json()
#     print len(result)
#     for i in result:
#         print i
#         allcommitsha.append(i['sha'])
#     m=getlink(rlink)
#     url=m[0]
#     if m[0]==m[1]:
#         break
# print len(allcommitsha)
