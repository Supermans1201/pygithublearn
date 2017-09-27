import requests

USER = 'codinguser'
REPO = 'gnucash-android'

# url = "https://api.github.com/emojis"

url="https://github.com/codinguser/gnucash-android/pull/676.patch"
headers={
    "Accept": "application/vnd.github.v3+json",
    "Authorization":"token 26bcc8aeb5ba2c3d090db892acbc3b5fa6c97d26",
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}
# from requests import SNIAdapter
#
# s = requests.Session()
# s.mount('https://', SNIAdapter())
r = requests.get(url=url,headers=headers, verify=False)
# r = requests.post("http://httpbin.org/post")
# r = requests.put("http://httpbin.org/put")
# r = requests.delete("http://httpbin.org/delete")
# r = requests.head("http://httpbin.org/get")
# r = requests.options("http://httpbin.org/get")
print "date :", r.headers["date"]
print "status :", r.headers["status"]
print "x-ratelimit-remaining :",r.headers["x-ratelimit-remaining"]
print "content-type :", r.headers["content-type"]
# for key,value in r.headers.items():
#     print key+" : "+value
print  r.text