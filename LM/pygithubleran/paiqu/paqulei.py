#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import os
import re
from pymongo import MongoClient

class Paqu:
    '爬取类'
    paquCount = 0

    def __init__(self, user="codinguser",repo="gnucash-android"):
        self.user = user
        self.repo = repo
        Paqu.paquCount += 1

        self.initissues_url()
        self.allissuesnum = []
        self.allcommitsha=[]

        self.params = {
            "state": "all"
        }
        self.allissuesnumfilename=self.user+"_"+self.repo+"_"+"allissuesnum.txt"
        self.allcommitshafilename = self.user + "_" + self.repo + "_" + "allscommitssha.txt"

        self.rootdir=self.user + "_" + self.repo
        self.diffdir=self.rootdir+"/"+"diff3"
        if not os.path.exists(self.rootdir):
            os.mkdir(self.rootdir)
        if not os.path.exists(self.diffdir):
            os.mkdir(self.diffdir)

        self.writeallissuesnumtxt=False
        self.writeallcommitsshatxt = False
        self.mongodbname=self.user+"_"+self.repo


    def initissues_url(self):
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": "token 26bcc8aeb5ba2c3d090db892acbc3b5fa6c97d26",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
        }

        self.pacth_headers ={
            "Accept": "application/vnd.github.VERSION.patch",
            "Authorization": "token 26bcc8aeb5ba2c3d090db892acbc3b5fa6c97d26",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
        }

        self.issues_url = "https://api.github.com/repos/" + self.user + "/" + self.repo + "/issues"
        self.commits_url = "https://api.github.com/repos/" + self.user + "/" + self.repo + "/commits"

    def displayCount(self):
        print "Total Paqu %d" % Paqu.paquCount

    def displayEmployee(self):
        print "Name : ", self.repo, ", Repo: ", self.repo

    def genAllissuesnumtxt(self):
        print "获取所有的issue 存入到"+self.allissuesnumfilename
        self.getallissuenums()
        print "写入文件"+self.allissuesnumfilename
        self.writeallissuesnumtxt = True
        fileObject = open(os.path.join(self.rootdir,self.allissuesnumfilename), 'w')
        for num in self.allissuesnum:
            # print num
            fileObject.write(str(num))
            fileObject.write('\n')
        fileObject.close()
        self.writeallissuesnumtxt = False

    def genAllcommitsshatxt(self):
        print "获取所有的issue 存入到"+self.allcommitshafilename
        self.getallcommitsha()
        print "写入文件"+self.allcommitshafilename
        self.writeallcommitsshatxt = True
        fileObject = open(os.path.join(self.rootdir,self.allcommitshafilename), 'w')
        for num in self.allcommitsha:
            # print num
            fileObject.write(str(num))
            fileObject.write('\n')
        fileObject.close()
        self.writeallcommitsshatxt= False

    def openmongdb(self, collname='comments'):
        print "打开数据库"+self.mongodbname+": collname"+collname
        client = MongoClient()
        db = client[self.mongodbname]
        coll = db[collname]
        return coll

    def genAllissuestomongodb(self):
        print "将所有issues存入到数据库中..."
        coll = self.openmongdb(collname='issues')

        while True:
            print "获取数据...",
            r = requests.get(url=self.issues_url, headers=self.headers, params=self.params)
            rlink = r.headers['link']
            print r
            result = r.json()
            print "将issues "+str(len(result))+"[",
            for i in result:
                print str(i['number']),

            print "] 存入到数据库.."
            m = self.getlink(rlink)
            self.issues_url = m[0]
            if m[0] == m[1]:
                break


    def genAllcommentstomongodb(self):
        print "将所有comment存入到数据库中..."
        coll = self.openmongdb(collname='comments')

        if os.path.exists(os.path.join(self.rootdir,self.allissuesnumfilename)):
            print "检测到存在文件"+self.allissuesnumfilename+"..."
            self.getallissuenumfromtxt()
            if len(self.allissuesnum)==0:
                "重新获得allissuesnum"
                self.getallissuenums()
        i = 1
        for num in self.allissuesnum:
            print "正在处理第"+str(i)+"个issue...","编号："+str(num[:-1]),
            i += 1
            result = self.getcommentdetil(num=num[:-1])
            if len(result)==0:
                print "该issue下无评论"
            else:
                print "将评论插入到数据库中.."
            for comment in result:
                comment["issue"] = num[:-1]
                coll.insert(comment)

    def genAllcommitstomongodb(self):
        print "将所有commit存入到数据库中..."
        coll = self.openmongdb(collname='commits')

        if os.path.exists(os.path.join(self.rootdir,self.allcommitshafilename)):
            print "检测到存在文件" + self.allcommitshafilename + "..."
            self.getallcommitshafromtxt()
            if len(self.allcommitsha) == 0:
                "重新获得allcommitsha"
                self.getallcommitsha()
        i = 1
        for sha in self.allcommitsha:
            print "正在处理第" + str(i) + "个commit...", "编号：" + str(sha[:-1]),
            i += 1
            result = self.getcommitdetil(sha=sha[:-1])
            coll.insert(result)

    def genAllcommitsdiffpatch(self):
        print "获取每次commit提交的不同..."

        if os.path.exists(os.path.join(self.rootdir,self.allcommitshafilename)):
            print "检测到存在文件" + self.allcommitshafilename + "..."
            self.getallcommitshafromtxt()
            if len(self.allcommitsha) == 0:
                "重新获得allcommitsha"
                self.getallcommitsha()
        i = 1
        for sha in self.allcommitsha:
            print "正在处理第" + str(i) + "个commit...", "编号：" + str(sha[:-1]),
            i += 1
            result = self.getcommitpatchdetil(sha=sha[:-1])

            fileObject = open(self.diffdir+"/" + sha[:-1] + '.txt', 'w')
            fileObject.write(result.encode('ascii', 'ignore').decode('ascii'))
            fileObject.close()

    def getlink(self,rlink):
        p = re.compile('<.*?>')
        m = re.findall(p, rlink)
        m2 = [re.sub('<|>', '', x) for x in m]
        return m2

    def getallissuenumfromtxt(self):
        print "从"+self.allissuesnumfilename+"获得issuesnum"
        f = open(os.path.join(self.rootdir,self.allissuesnumfilename))
        line = f.readline()
        while line:
            self.allissuesnum.append(line)
            line = f.readline()
        f.close()

    def getallcommitshafromtxt(self):
        print "从" + self.allcommitshafilename + "获得commitsha"
        f = open(os.path.join(self.rootdir,self.allcommitshafilename))
        line = f.readline()
        while line:
            self.allcommitsha.append(line)
            line = f.readline()
        f.close()

    def getallissuenums(self):
        print "分页处理中..."
        i = 0
        while True:
            i += 1
            print "正在处理issues第"+str(i)+"分页..."
            response = requests.get(url=self.issues_url, headers=self.headers, params=self.params)
            rlink = response.headers['link']
            results = response.json()
            for result in results:
                self.allissuesnum.append(result['number'])
            m = self.getlink(rlink)
            self.issues_url = m[0]
            if m[0] == m[1]:
                print "处理完毕..."
                break
        print "所有issues共"+str(i)+"分页，共"+str(len(self.allissuesnum)) + "个"

    def getallcommitsha(self):
        print "分页处理中..."
        i = 0
        while True:
            i += 1
            print "正在处理commits第" + str(i) + "分页..."
            response = requests.get(url=self.commits_url, headers=self.headers, params=self.params)
            rlink = response.headers['link']
            results = response.json()
            for result in results:
                self.allcommitsha.append(result['sha'])
            m = self.getlink(rlink)
            self.commits_url = m[0]
            if m[0] == m[1]:
                print "处理完毕..."
                break
        print "所有commits共" + str(i) + "分页，共" + str(len(self.allcommitsha)) + "个"


    def getcommentdetil(self, num="42"):
        self.comment_url = "https://api.github.com/repos/" + self.user + "/" + self.repo + "/issues/" + num + "/comments"
        print self.comment_url
        r = requests.get(url=self.comment_url, headers=self.headers)
        print "获取结果："+str(r)
        return r.json()

    def getcommitdetil(self,sha="daf2e8ba4261d19b4b3c4eebee5a61773c86632b"):
        self.commit_url= "https://api.github.com/repos/"+ self.user+"/"+self.repo+"/commits/"+sha
        print self.commit_url
        r = requests.get(url=self.commit_url, headers=self.headers)
        print "获取结果：" + str(r)
        return r.json()

    def getcommitpatchdetil(self,sha="daf2e8ba4261d19b4b3c4eebee5a61773c86632b"):
        self.commit_url= "https://api.github.com/repos/"+ self.user+"/"+self.repo+"/commits/"+sha
        print self.commit_url
        r = requests.get(url=self.commit_url, headers=self.pacth_headers)
        print "获取结果：" + str(r)
        return r.text