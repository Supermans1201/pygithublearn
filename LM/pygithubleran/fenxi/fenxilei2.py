#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import os
from pymongo import MongoClient

import numpy as np
import matplotlib.pyplot as plt

class Fenxi:
    '预处理类'
    fenxiCount = 0

    def __init__(self, user="codinguser", repo="gnucash-android",rootdir = "F:/LM/pygithub_leran/paiqu/testpaqu/codinguser_gnucash-android/diff3"):
        self.user = user
        self.repo = repo
        self.rootdir=rootdir


        self.diffflist = open('diff_intent_text', 'a')
        self.mongodbname = self.user + "_" + self.repo
        Fenxi.fenxiCount += 1

    def displayCount(self):
        print "Total Paqu %d" % Fenxi.fenxiCount


def gendiff(self):
    list_dirs = os.walk(self.rootdir)
    for root, dirs, files in list_dirs:
        i = 0
        for f in files:
            i += 1
            path = os.path.join(root, f)
            self.diffflist.write(f + "\n")
            self.getinfofromtxt(path)
        print i
    self.diffflist.close()


def openmongdb(self, collname='comments'):
    print "打开数据库" + self.mongodbname + ": collname" + collname
    client = MongoClient()
    db = client[self.mongodbname]
    coll = db[collname]
    return coll


def getinfofromtxt(self, filepath):
    self.diffdata = {}

    self.infodata = {}
    self.infodata["change"] = [0, 0, 0, 0, 0]
    self.infodata["create"] = []
    self.infodata["delete"] = []
    self.infodata["files"] = []
    self.infodata["subject"] = []
    self.isFix = False

    f = open(filepath)
    line = f.readline()

    isnotejava = False
    isnotexml = False
    start = False
    diff = 0

    diffname = ""
    tempdata = {}

    print filepath
    while line:
        line = f.readline()

        if "Subject" in line:

            start = False
            self.infodata["subject"].append(line)
            if not self.diffdata.get(diffname):
                self.diffdata[diffname] = tempdata
                tempdata = {}
                # print "*subject*",diffname,self.diffdata[diffname]
                #

        if re.search(u"fix", line, re.I):
            self.isFix = True
            # print line

        if "---\n" == line:
            start = True
        if line.startswith("diff"):
            start = False

            # 如果没有初值赋予初值
            if not self.diffdata.get(diffname):
                self.diffdata[diffname] = tempdata
                tempdata = {}
            # print "*diff*", diffname, tempdata, self.diffdata[diffname]
            # for k, v in self.diffdata.items():
            #     print "diff",k, v

            fn = line.split()
            # print fn
            try:
                if fn[2][2:] == fn[3][2:]:
                    ft = fn[2][2:]
                    # print ft

                    for td in self.infodata["files"]:
                        if td[0].startswith(".../"):
                            tt = td[0][4:]
                            if ft.endswith(tt):
                                td[0] = ft
                    # print "暂时注释掉，不要删除以后添加日志输出diff",ft
                    diff = 0
                    diffname = ft.replace(".", "_")

                    if not ft.endswith(".java") and not ft.endswith(".xml"):
                        start = True
                    if start == False:
                        self.diffflist.write(ft + "\n")
                        # print "**",ft, tt
                        # print
            except:
                print "td"
                import time
                time.sleep(10)

        if start == False:
            if re.search("@@(.*) @@", line, re.I):
                diff += 1
                tempdata[diff] = []

            if re.search("/\*", line, re.I):
                isnotejava = True
            if re.search("//", line, re.I) \
                    and not re.search("http://", line, re.I) and not re.search("https://", line,
                                                                               re.I) and not re.search("file://",
                                                                                                       line, re.I):
                temp = re.split("//", line, re.I)
                temps = ""
                for s in temp[:-1]:
                    temps += s
                # print "[",line,"->",temps,"]"
                line = temps

            if re.search("<!--", line, re.I):
                isnotexml = True
                # print line
                pass
            if isnotejava or isnotexml:
                pass
            else:
                if line.startswith("+") or line.startswith("-"):
                    if not (line.startswith("+++") or line.startswith("---")):
                        newline = line.replace("<", " < ").replace(">", " > ").replace("{", " { ").replace("}",
                                                                                                           " } ") \
                            .replace(",", " , ").replace("!", " ! ").replace("+", "+ ").replace("-", "- ").replace(
                            "\"",
                            " \" ") \
                            .replace(".", ".").replace("(", " ( ").replace(")", " ) ").replace(";", " ; ").replace(
                            "=",
                            " = ").replace(
                            "\n", " ").replace("\s", " ").replace("\r", " ") \
                            .replace("\t", " ").replace("   ", " ").replace("  ", " ").replace("|", " | "). \
                            replace("= =", "==").replace(
                            "! =", "!=").replace("!  =", "!=").replace("< =", "<=").replace("> =", ">=") \
                            .replace("{ }", "{}").replace("{  }", "{}").replace("( )", "()").replace("(  )",
                                                                                                     "()").replace(
                            "* =", "*=").replace("+ =", "+=").replace("- =", "-=")
                        if diff == 0:
                            self.infodata["subject"].append(line)
                        if diff > 0:

                            if not tempdata.get(diff):
                                tempdata[diff] = []
                            tempdata[diff].append(newline)
                            # print tempdata
                            # print diff, tempdata[diff]
                            # print "*", newline
                            # print newline

            if re.search("\*/", line, re.I):
                isnotejava = False
            if re.search("-->", line, re.I):
                isnotexml = False

        if start == True:

            if re.search("(\s*)\\|(\s* )([0-9]+)(\+*\-*)", line, re.I):
                temp = re.split("\\|", "".join(line.replace("+", " ").replace("-", " ").split()))
                self.infodata["files"].append(temp)
            else:
                if re.search(
                        "( files changed, )|(insertions\\(\\+\\),)|(deletions\\(-\\))|( file changed, )|(insertion\\(\\+\\),)|(deletion\\(-\\))",
                        line, re.I):
                    # print line
                    fid = re.split("([0-9]+)", "".join(line.split()))
                    for s in fid:
                        if not re.search("([0-9]+)", s):
                            fid.remove(s)
                    if len(fid) == 3:
                        self.infodata["change"][0] += int(fid[0])
                        self.infodata["change"][1] += int(fid[1])
                        self.infodata["change"][2] += int(fid[2])
                    if len(fid) == 2:
                        if re.search("insertion", line, re.I):
                            self.infodata["change"][0] += int(fid[0])
                            self.infodata["change"][1] += int(fid[1])

                        if re.search("deletion", line, re.I):
                            self.infodata["change"][0] += int(fid[0])
                            self.infodata["change"][2] += int(fid[1])
                            # print fid

    self.diffdata[diffname] = tempdata

    for dn, td in self.diffdata.items():
        num = 0
        newtd = {}
        for k, v in td.items():

            if not v == []:
                num += 1
                newtd[str(num)] = v
        self.diffdata[dn] = newtd
        if self.diffdata[dn] == {}:
            del self.diffdata[dn]

    self.infodata["isfix"] = self.isFix
    self.infodata["change"][3] += (len(self.infodata["create"]))
    self.infodata["change"][4] += (len(self.infodata["delete"]))
    # print self.infodata["files"]
    print self.infodata["change"]
    # print self.infodata["subject"]
    # print self.diffdata
    data = {}
    data = {"name": filepath, "info": self.infodata, "diff": self.diffdata}
    coll = self.openmongdb(collname="diffinfo")
    coll.insert(data)
    f.close()
