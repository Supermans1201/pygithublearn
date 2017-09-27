#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import os
import re

from pygitthub.pygithub import  Pygithub

class Paqu:
    '爬取类'
    count = 0

    def __init__(self, user="codinguser",repo="gnucash-android"):

        self.pyg= Pygithub(user=user,repo=repo)

        Paqu.count += 1
        self.writeallissuesnumtxt = False
        self.writeallcommitsshatxt = False
        self.allissuesnum = []
        self.allcommitsha=[]


    def genAllissuesnumtxt(self):
        print "获取所有的issue 存入到"+self.pyg.allissuesnumfilename
        self.getallissuenums()
        print "写入文件"+self.pyg.allissuesnumfilename
        self.writeallissuesnumtxt = True
        fileObject = open(self.pyg.allissuesnumfilepath, 'w')
        for num in self.allissuesnum:
            # print num
            fileObject.write(str(num))
            fileObject.write('\n')
        fileObject.close()
        self.writeallissuesnumtxt = False

    def genAllcommitsshatxt(self):
        print "获取所有的commit sha存入到"+self.pyg.allcommitshafilename
        self.getallcommitsha()
        print "写入文件"+self.pyg.allcommitshafilename
        self.writeallcommitsshatxt = True
        fileObject = open(self.pyg.allcommitshafilepath, 'w')
        for num in self.allcommitsha:
            # print num
            fileObject.write(str(num))
            fileObject.write('\n')
        fileObject.close()
        self.writeallcommitsshatxt= False

    def genAllissuestomongodb(self):
        print "将所有issues存入到数据库中..."
        coll = self.pyg.issuescoll

        while True:
            print "获取数据...",
            r = requests.get(url=self.pyg.issues_url, headers=self.pyg.headers, params=self.pyg.params)
            rlink = r.headers['link']
            print r
            result = r.json()
            print "将issues "+str(len(result))+"[",
            for i in result:
                print str(i['number']),
                coll.insert(i)
            print "] 存入到数据库.."
            m = self.getlink(rlink)
            self.pyg.issues_url = m[0]
            if m[0] == m[1]:
                break


    def genAllcommentstomongodb(self):
        print "将所有comment存入到数据库中..."
        coll = self.pyg.commentsoll

        if os.path.exists(self.pyg.allissuesnumfilepath):
            print "检测到存在文件"+self.pyg.allissuesnumfilename+"..."
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
        coll = self.pyg.commitscoll

        if os.path.exists(self.pyg.allcommitshafilepath):
            print "检测到存在文件" + self.pyg.allcommitshafilename + "..."
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

        if os.path.exists(self.pyg.allcommitshafilepath):
            print "检测到存在文件" + self.pyg.allcommitshafilename + "..."
            self.getallcommitshafromtxt()
            if len(self.allcommitsha) == 0:
                "重新获得allcommitsha"
                self.getallcommitsha()
        i = 1
        for sha in self.allcommitsha:
            print "正在处理第" + str(i) + "个commit...", "编号：" + str(sha[:-1]),
            i += 1
            result = self.getcommitpatchdetil(sha=sha[:-1])

            fileObject = open(self.pyg.diffdirpath+"/" + sha[:-1] + '.txt', 'w')
            fileObject.write(result.encode('ascii', 'ignore').decode('ascii'))
            fileObject.close()

    def getlink(self,rlink):
        p = re.compile('<.*?>')
        m = re.findall(p, rlink)
        m2 = [re.sub('<|>', '', x) for x in m]
        return m2

    def getallissuenumfromtxt(self):
        print "从"+self.pyg.allissuesnumfilename+"获得issuesnum"
        f = open(self.pyg.allissuesnumfilepath)
        line = f.readline()
        while line:
            self.allissuesnum.append(line)
            line = f.readline()
        f.close()

    def getallcommitshafromtxt(self):
        print "从" + self.pyg.allcommitshafilename + "获得commitsha"
        f = open(self.pyg.allcommitshafilepath)
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
            response = requests.get(url=self.pyg.issues_url, headers=self.pyg.headers, params=self.pyg.params)
            rlink = response.headers['link']
            results = response.json()
            for result in results:
                self.allissuesnum.append(result['number'])
            m = self.getlink(rlink)
            self.pyg.issues_url = m[0]
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
            response = requests.get(url=self.pyg.commits_url, headers=self.pyg.headers, params=self.pyg.params)
            rlink = response.headers['link']
            results = response.json()
            for result in results:
                self.allcommitsha.append(result['sha'])
            m = self.getlink(rlink)
            self.pyg.commits_url = m[0]
            if m[0] == m[1]:
                print "处理完毕..."
                break
        print "所有commits共" + str(i) + "分页，共" + str(len(self.allcommitsha)) + "个"


    def getcommentdetil(self, num="42"):
        comment_url = self.pyg.issues_url+ "/" + num + "/comments"
        print comment_url
        r = requests.get(url=comment_url, headers=self.pyg.headers)
        print "获取结果："+str(r)
        return r.json()

    def getcommitdetil(self,sha="daf2e8ba4261d19b4b3c4eebee5a61773c86632b"):
        commit_url=self.pyg.commits_url+"/"+sha
        print commit_url
        r = requests.get(url=commit_url, headers=self.pyg.headers)
        print "获取结果：" + str(r)
        return r.json()

    def getcommitpatchdetil(self,sha="daf2e8ba4261d19b4b3c4eebee5a61773c86632b"):
        commit_url = self.pyg.commits_url + "/" + sha
        print commit_url
        r = requests.get(url=commit_url, headers=self.pyg.pacth_headers)
        print "获取结果：" + str(r)
        return r.text