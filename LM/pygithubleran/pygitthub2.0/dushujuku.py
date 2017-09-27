#!/usr/bin/python
# -*- coding: UTF-8 -*-
from pymongo import MongoClient
import requests
from pygitthub.pygithub import Pygithub
import re

class Dushujuku:
    '读取数据类'
    count = 0

    def __init__(self, user="codinguser",repo="gnucash-android"):
        self.pyg = Pygithub(user=user, repo=repo)
        Dushujuku.count +=1


        self.newcommitsdata = {}
        self.newcomentsdata = {}
        self.newissuesdata={}
        self.newdiffinfodata={}

    def dealdiffinfo(self):
        self.newdiffinfodata={}
        result=[]
        for data in self.pyg.diffinfocoll.find():
            print data


    def dealcommits(self):
        self.newcommitsdata = {}
        result=[]
        print self.pyg.commitscoll.count()
        for data in self.pyg.commitscoll.find():
            # print data
            # print type(data)
            sha=""
            stats=""
            deletions=""
            additions=""
            total=""
            files=[]
            for k,v in data.items():
                # print k,v
                if k=="sha":
                    sha = v
            for k, v in data.items():
                if k == "stats":
                    deletions = v["deletions"]
                    additions = v["additions"]
                    total=v["total"]
                    # print temp
            for k, v in data.items():
                if k == "files":
                    # print v
                    # print type(v)

                    if type(v)==type([]):
                        for f in v:

                            ftup = (f["filename"],f["status"],f["deletions"],f["additions"],f["changes"])
                            # print ftup
                            files.append(ftup)
            result.append((sha,deletions,additions,total,files))


        key=set([])
        for data in result:
            key.add(data[0])
        print len(key)
        for k in key:
            self.newcommitsdata[k]=[]
        i=0

        for data in result:
            if not (data[1] in self.newcommitsdata[data[0]] and data[2] in self.newcommitsdata[data[0]] and data[3] in self.newcommitsdata[data[0]]):
                # print "*",
                self.newcommitsdata[data[0]].append(data[1])
                self.newcommitsdata[data[0]].append(data[2])
                self.newcommitsdata[data[0]].append(data[3])
                self.newcommitsdata[data[0]].append(data[4])
        print self.newcommitsdata["995081989302e71a246c2eb53e9c915df92cbc9a"]
        self.pyg.commitsinfocoll.insert(self.newcommitsdata)

        # print self.newcommitsdata['667']


    def dealcomments(self):
        self.newcomentsdata = {}
        result=[]
        print self.pyg.commentsoll.count()
        for data in self.pyg.commentsoll.find():
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

        self.pyg.commentsinfocoll.insert(self.newcomentsdata)
    def dealissues(self):
        self.newissuesdata = {}
        result=[]

        print self.pyg.issuescoll.find_one()
        print self.pyg.issuescoll.count()
        i = 0
        for data in self.pyg.issuescoll.find():
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
        self.pyg.issuesinfocoll.insert(self.newissuesdata )


    def dealissues2(self):
        self.newissuesdata = {}
        i=0
        for data in self.pyg.issuesinfocoll.find():
            print data
            for k, v in data.items():
                if  type(v)==type([]):
                    if  v[4].startswith("https"):
                        print v[4]
                        r = requests.get(url=v[4], headers=self.pyg.pacth_headers, verify=False)
                        if r.text.startswith("From"):
                            pullrequest= r.text[5:45]
                            i+=1
                            print i
                            self.newissuesdata[k]=pullrequest
                        else:
                            print r.text
        print self.newissuesdata
        self.pyg.issuesinfo2coll.insert(self.newissuesdata)

    def readdealcomments(self):
        for data in self.pyg.commentsinfocoll.find():
            print data
    def getlabelset(self):
        labelset = set([])
        for data in self.pyg.issuesinfocoll.find():
            # print data
            for k,v in data.items():
                    if type(v)==type([]):
                        if type(v[2])==type([]):
                            for l in v[2]:
                                labelset.add(l)
        print labelset

    def readdealissuesandcommits(self):

        issueset1=set([])
        issueset2= set([])
        for data in self.pyg.issuesinfocoll.find():
            ## 所使用的策略1，根据标签bug读取
            for k,v in data.items():
                if not k in issueset1:
                    if type(v)==type([]) :
                        if "bug" in  v[2] or "Bug" in v[2]:
                            issueset1.add(k)
                        if re.search("fix",v[0],re.I) or re.search("fix",v[1],re.I) or re.search("bug",v[0],re.I) or re.search("bug",v[1],re.I):
                            issueset2.add(k)
        issueshamap=self.pyg.issuesinfo2coll.find_one()
        shaissuemap=self.pyg.issuesinfo3coll.find_one()

        shashamap={}
        ##issueshamap and shaissuemap
        for key, value in issueshamap.items():
            print key,value
        for key, value in shaissuemap.items():
            print key, value
            shashamap[key]=[]
            try:
                for v in value:
                    shashamap[key].append(issueshamap.get(v))
            except:
                print "error"
                pass
        for key,value in shashamap.items():
            print key,value

        issueset3=set(issueshamap.keys())
        issueset4=set([])
        for key, value in shaissuemap.items():
            print key, value
            shashamap[key] = []
            try:
                for v in value:
                   issueset4.add(v)
            except:
                print "error"
                pass

        print issueset1
        print issueset2
        print issueset3
        print issueset4

        # self.drawisuuesvenn(issueset1,issueset2,issueset3,issueset4)
        issueset= (issueset1|issueset2)&(issueset3|issueset4)
        shaset=set([])
        for  issue in issueset:
            if issueshamap.get(issue):
                shaset.add(issueshamap[issue])
            for key, value in shaissuemap.items():
                if type(value)==type([]) and issue in value:
                    shaset.add(key)
        print len(shaset)
        print shaset

        self.getfixbugdiff(shaset)
        ##复制文件

    def getfixbugdiff(self,set=set([])):
        self.bugissues = {}
        import os
        list_dirs = os.walk(self.pyg.diffdirpath)

        for root, dirs, files in list_dirs:
            i = 0
            for f in files:
                i += 1
                path = os.path.join(root, f)
                if not os.path.exists(self.pyg.diffdirpath2):
                    os.mkdir(self.pyg.diffdirpath2)
                path2=os.path.join(self.pyg.diffdirpath2,f)
                if f.replace(".txt","") in set:
                    self.copyfile(path,path2)
            print i

    def copyfile(self,srcpath="",descpath=""):
        import shutil,os

        shutil.copyfile(src=srcpath,dst=descpath)

    def drawisuuesvenn(self, A = set([]), B = set([]),C=set([]),D=set([])):
        import matplotlib.pyplot as plt
        from matplotlib_venn import venn3

        from matplotlib_venn import venn2
        plt.figure(figsize=(22, 10))



        venn3([A | B, C, D], ["inlabel|title|body", "haspullrequest", "fromdifftxt"])
        import os
        savepath = os.path.join(self.pyg.picpath + "Inlabel-title-body_haspullrequest_fromdifftxt" + ".png")
        print savepath
        plt.savefig(savepath)

