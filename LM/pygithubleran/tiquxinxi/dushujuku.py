#!/usr/bin/python
# -*- coding: UTF-8 -*-
from pymongo import MongoClient
import requests

class Dushujuku:
    '爬取类'
    paquCount = 0

    def __init__(self, user="codinguser",repo="gnucash-android"):
        self.user = user
        self.repo = repo
        self.mongodbname=self.user+"_"+self.repo

        self.commentsoll = self.openmongdb("comments")
        self.issuescoll=self.openmongdb("issues")
        self.commitscoll=self.openmongdb("commits")
        self.diffinfocoll=self.openmongdb("diffinfo")

        self.commentinfocoll=self.openmongdb("commentsinfo")

        self.issuesinfocoll=self.openmongdb("issuesinfo")
        self.issuesinfo2coll = self.openmongdb("issuesinfo2")

    def openmongdb(self, collname='comments'):
        print "打开数据库"+self.mongodbname+": collname"+collname
        client = MongoClient()
        db = client[self.mongodbname]
        coll = db[collname]
        return coll

    def dealcomments(self):
        self.newcomentsdata = {}
        result=[]
        print self.commentsoll.count()
        for data in self.commentsoll.find():
            # print data
            # print type(data)
            temp=""
            number=0
            for k,v in data.items():
                # print k,v
                if k=="issue":
                    number = v
            for k, v in data.items():
                if k == "body":
                    temp=v
                    # print temp
            result.append((number,temp))

        print result
        # for data in result:
        #     print data[0],data[1]
        #
        key=set([])
        for data in result:
            key.add(data[0])
        print len(key)
        for k in key:
            self.newcomentsdata[k]=[]
        for data in result:
            if not data[1] in self.newcomentsdata[data[0]]:
                # print "*",
                self.newcomentsdata[data[0]].append(data[1])

        print self.newcomentsdata['667']

        # self.commentinfocoll.insert(self.newcomentsdata)
    def dealissues(self):
        self.newissuesdata = {}
        result=[]

        print self.issuescoll.find_one()
        print self.issuescoll.count()
        i = 0
        for data in self.issuescoll.find():
            # print data
            # print type(data)
            labels=[]
            number=0
            title=""
            body=""
            state=""
            pullrequest = "False"

            for k,v in data.items():
                # print k,v
                if k=="number":
                    number = v
            for k, v in data.items():
                if k == "title":
                    title=v
            for k, v in data.items():
                if k == "body":
                    body = v
            for k, v in data.items():
                if k == "labels":
                    labels = []
                    for vv in v:
                        labels.append(vv["name"])
            for k, v in data.items():
                if k == "state":
                    state= v

            for k, v in data.items():
                if k == "pull_request":
                    pullrequest="True"
                    i+=1
                    print i
                    print pullrequest
                    print type(v["patch_url"])
                    print v["patch_url"]
                    pullrequest=v["patch_url"]
                    # r = requests.get(url=v["patch_url"], headers=self.headers, verify=False)
                    #
                    # pullrequest= r.text[5:45]
                    # result = r.json()

                    # if v["patch_url"]==""or v["patch_url"]==None:
                    #     print True
                    # print temp
            result.append((number,title,body,labels,state,pullrequest))

        print len(result)

        print result[0],result[1],result[2]
        # # for data in result:
        # #     print data[0],data[1]
        # #
        self.newissuesdata = {}
        key=set([])
        for data in result:
            if not data[3]==[]:
                for v in data[3]:
                    # print v["name"]
                    key.add(v)
        print len(key)
        print key

        idset=set([])
        for data in result:
            idset.add(data[0])
        for data in result:
            if data[0]==676:
                print data
        for id in idset:
            for data in result:
                if data[0] == id:
                    self.newissuesdata[str(id)]=((data[1]),data[2],data[3],data[4],data[5])
        print len( self.newissuesdata )
        print len(result)
        self.issuesinfocoll.insert(self.newissuesdata )


        # for k in key:
        #     self.newcomentsdata[k]=[]------
        # # for data in result:---------------------------------------------------------------
        # #     self.newcomentsdata[data[0]].append(data[1-----------------------------])----------------------
        #----------
        # #
        # ---------------------------------------------------------------------------------------

    def dealissues2(self):
        self.pacth_headers = {
                "Accept": "application/vnd.github.VERSION.patch",
                "Authorization": "token 26bcc8aeb5ba2c3d090db892acbc3b5fa6c97d26",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
            }
        self.newissuesdata = {}
        i=0
        for data in self.issuesinfocoll.find():
            print data
            for k, v in data.items():
                if  type(v)==type([]):
                    if  v[4].startswith("https"):
                        print v[4]
                        r = requests.get(url=v[4], headers=self.pacth_headers, verify=False)
                        if r.text.startswith("From"):
                            pullrequest= r.text[5:45]
                            i+=1
                            print i
                            self.newissuesdata[k]=pullrequest
                        else:
                            print r.text
        print self.newissuesdata
        self.issuesinfo2coll.insert(self.newissuesdata)






    def readdealcomments(self):
        for data in self.commentinfocoll.find():
            print data

