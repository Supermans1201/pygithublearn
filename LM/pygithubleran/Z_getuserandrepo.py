import requests

# encoding:utf=8
from pymongo import MongoClient

from pymongo import MongoClient
def openmongdb(dbname='xiangmu',collname='xiangmu'):
    client = MongoClient()
    db = client[dbname]
    coll = db[collname]
    return coll
coll=openmongdb()
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
headers={
    "Accept": "application/json",
    "Authorization":"token 26bcc8aeb5ba2c3d090db892acbc3b5fa6c97d26",
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "x-ratelimit-limit":"100"
}
url = "https://api.github.com/search/repositories?q=stars%3A1000..1050&order=desc"


def getxiangmu(url=url):
    r = requests.get(url=url, headers=headers)
    result=r.json()
    theresult=[]
    thedata = []
    print len(result["items"])
    print result["total_count"]


    count=0
    # print r.text
    def getlink(rlink):
        import re
        p=re.compile('<.*?>')
        m=re.findall(p,rlink)
        m2=[re.sub('<|>','',x) for x in m]
        return m2


    while True:
        r = requests.get(url=url, headers=headers)
        rlink = r.headers['link']
        # print rlink
        results = r.json()
        list=[]
        for result in results["items"]:
            count+=1
            theresult.append(result["full_name"])
            tup = [
                result["full_name"], result["language"], str(result["size"]), result["description"],
                result["homepage"], result["html_url"], str(result["forks_count"]), str(result["watchers_count"]),
                str(result["open_issues_count"])]
            thedata.append(tup)
            # print "subscribers_count", result["subscribers_count"]

        m=getlink(rlink)
        url=m[0]
        if m[0]==m[1]:
            r = requests.get(url=url, headers=headers)
            rlink = r.headers['link']
            # print rlink
            results = r.json()

            for result in results["items"]:
                count += 1
                theresult.append(result["full_name"])
                tup = [
                    result["full_name"], result["language"], str(result["size"]), result["description"],
                    result["homepage"],result["html_url"], str(result["forks_count"]), str(result["watchers_count"]),
                    str(result["open_issues_count"])]
                thedata.append(tup)
            break
    print count
    return theresult,thedata


def getxiangmu2(num1=10000,num2=400000):
    urls = "https://api.github.com/search/repositories?q=stars%3A"+str(num1)+".."+str(num2)+"&order=desc"
    theresult,thedata=getxiangmu(url=urls)
    # fileObject = open("F:/LM/xiangmu/"+str(num1)+"_"+str(num2)+'.txt', 'w')
    # for sha in thedata:
    #     fileObject.write(sha)
    #     fileObject.write('\n')
    # fileObject.close()
    print len(thedata)

    import csv
    with open("F:/LM/xiangmu/"+str(num1)+"_"+str(num2)+'.csv', 'w') as f:
        f.write('\xEF\xBB\xBF')
        writer = csv.writer(f)
        for data in thedata:
            writer.writerow(data)

#>10000 40000 513
#6000 10000 718
#4500 6000 666
#3500 4500 772
#3000 3500 617

#2400 3000 (100)
#1000 2400 (50)
for i in range(2700,3000,100):
    print i
    try:
        getxiangmu2(i,i+100)
    except Exception, Argument:
        print "excption:"+str(i)
        print Exception,Argument
        pass
# try:
#     getxiangmu2(3000,3500)
# except Exception, Argument:
#     print "excption1"
#     print Exception,Argument
#     pass
# try:
#      getxiangmu2(3500,4500)
# except Exception, Argument:
#      print "excption2"
#      print Exception, Argument
#      pass
#
# try:
#     getxiangmu2(4500,6000)
# except Exception, Argument:
#     print "excption3"
#     print Exception, Argument
#     pass
# try:
#     getxiangmu2(6000,10000)
# except Exception, Argument:
#     print "excption4"
#     print Exception, Argument
#     pass
# try:
#     getxiangmu2(10000,400000)
# except Exception, Argument:
#     print "excption5"
#     print Exception, Argument
#     pass


