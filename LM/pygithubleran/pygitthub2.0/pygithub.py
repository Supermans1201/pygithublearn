#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from pymongo import MongoClient
class Pygithub:
    '一个pygithub对应一个Android爬取项目'
    count=0

    def __init__(self, user="codinguser", repo="gnucash-android"):
        Pygithub.count+=1
        self.user = user
        self.repo = repo
        self.name=self.user + "_" + self.repo
        self.mongodbname =self.user + "_" + self.repo
        #数据库名称
        self.rootdir = "F:/LM/pygithub_learn2.0/pygitthub/"+self.user + "_" + self.repo+"/"

        ### part1 from paqu
        # 根目录
        self.allissuesnumfilename = self.user + "_" + self.repo + "_" + "allissuesnum.txt"
        self.allcommitshafilename = self.user + "_" + self.repo + "_" + "allscommitssha.txt"


        self.diffdirpath = self.rootdir + "/" + "diff3"

        self.diffdirpath2 = self.rootdir + "/" + "diff2"
        self.diffdirpath3 = self.rootdir + "/" + "diff1"

        if not os.path.exists(self.rootdir):
            os.mkdir(self.rootdir)
        if not os.path.exists(self.diffdirpath):
            os.mkdir(self.diffdirpath)
        if not os.path.exists(self.diffdirpath2):
            os.mkdir(self.diffdirpath2)
        if not os.path.exists(self.diffdirpath3):
            os.mkdir(self.diffdirpath3)
        self.allissuesnumfilepath=os.path.join(self.rootdir,self.allissuesnumfilename)
        self.allcommitshafilepath=os.path.join(self.rootdir,self.allcommitshafilename)

        self.initissues_url()
        ###part2 from yuchuli

        self.difffilename = self.user + "_" + self.repo + "_" + "difftext"
        self.diffpredealfilename = self.user + "_" + self.repo + "_" + "diffpredealtext"
        self.directoryfilename = self.user + "_" + self.repo + "_" + "directory.txt"
        self.diffmodelfilename = self.user + "_" + self.repo + "_" + "diff.model"

        self.diffjavafilename = self.user + "_" + self.repo + "_" + "difftext_java"
        self.diffpredealjavafilename = self.user + "_" + self.repo + "_" + "diffpredealtext_java"
        self.directoryjavafilename = self.user + "_" + self.repo + "_" + "directory_java.txt"
        self.diffmodeljavafilename = self.user + "_" + self.repo + "_" + "diff_java.model"

        self.diffxmlfilename = self.user + "_" + self.repo + "_" + "difftext_xml"
        self.diffpredealxmlfilename = self.user + "_" + self.repo + "_" + "diffpredealtext_xml"
        self.directoryxmlfilename = self.user + "_" + self.repo + "_" + "directory_xml.txt"
        self.diffmodelxmlfilename = self.user + "_" + self.repo + "_" + "diff_xml.model"


        self.difffilepath = os.path.join(self.rootdir,self.difffilename)
        self.diffpredealfilepath = os.path.join(self.rootdir,self.diffpredealfilename)
        self.directoryfilepath = os.path.join(self.rootdir,self.directoryfilename)
        self.diffmodelfilepath = os.path.join(self.rootdir,self.diffmodelfilename)

        self.diffjavafilepath = os.path.join(self.rootdir,self.diffjavafilename)
        self.diffpredealjavafilepath = os.path.join(self.rootdir,self.diffpredealjavafilename)
        self.directoryjavafilepath = os.path.join(self.rootdir,self.directoryjavafilename)
        self.diffmodeljavafilepath = os.path.join(self.rootdir,self.diffmodeljavafilename)

        self.diffxmlfilepath = os.path.join(self.rootdir,self.diffxmlfilename)
        self.diffpredealxmlfilepath = os.path.join(self.rootdir,self.diffpredealxmlfilename)
        self.directoryxmlfilepath = os.path.join(self.rootdir,self.directoryxmlfilename)
        self.diffmodelxmlfilepath = os.path.join(self.rootdir,self.diffmodelxmlfilename)
        self.picpath    =os.path.join(self.rootdir,"pic")

        self.commentsoll = self.openmongdb("comments")
        self.issuescoll = self.openmongdb("issues")
        self.commitscoll = self.openmongdb("commits")

        self.commitsinfocoll = self.openmongdb("commitsinfo")
        self.commentsinfocoll = self.openmongdb("commentsinfo")
        self.issuesinfocoll = self.openmongdb("issuesinfo")
        self.issuesinfo2coll = self.openmongdb("issuesinfo2")
        self.issuesinfo3coll = self.openmongdb("issuesinfo3")
        self.diffinfocoll = self.openmongdb("diffinfo")

    def initissues_url(self):
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": "token 26bcc8aeb5ba2c3d090db892acbc3b5fa6c97d26",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
        }
        self.params = {
            "state": "all"
        }
        self.pacth_headers = {
            "Accept": "application/vnd.github.VERSION.patch",
            "Authorization": "token 26bcc8aeb5ba2c3d090db892acbc3b5fa6c97d26",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
        }

        # https: // api.github.com / repos /codinguser/gnucash-android/issues
        self.issues_url = "https://api.github.com/repos/" + self.user + "/" + self.repo + "/issues"
        self.commits_url = "https://api.github.com/repos/" + self.user + "/" + self.repo + "/commits"

    def openmongdb(self, collname='comments'):
        print "打开数据库" + self.mongodbname + ": collname" + collname
        client = MongoClient()
        db = client[self.mongodbname]
        coll = db[collname]
        return coll

