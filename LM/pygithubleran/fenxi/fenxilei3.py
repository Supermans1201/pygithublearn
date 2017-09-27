#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import os

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

    def getinfofromtxt(self, filepath):
        self.fixdata = []
        self.thedata = []
        self.deletedata = []
        self.createdata = []

        f = open(filepath)
        line = f.readline()
        isFix = False
        subject = ""
        start = False
        diff = False
        print filepath
        while line:
            line = f.readline()

            if "Subject" in line:
                subject = line
                print line
            if re.search(u"fix", line, re.I):
                isFix = True
                print line

            if "---\n" == line:
                start = True
            if line.startswith("diff"):
                start = False
                fn = line.split()
                # print fn
                try:
                    if fn[2][2:] == fn[3][2:]:
                        ft = fn[2][2:]
                        # print ft

                        for td in self.thedata:
                            if td[0].startswith(".../"):
                                tt = td[0][4:]
                                if ft.endswith(tt):
                                    td[0] = ft
                        print ft

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
                if line.startswith("+") or line.startswith("-"):
                    if not (line.startswith("+++") or line.startswith("---")):
                        newline = line.replace(", ", ",").replace("}", " } ").replace(";", " ; ")
                        # if re.search("intent",newline,re.I):
                        #     print newline
                        self.diffflist.write(newline)

                        # print line

            if start == True:
                if re.search("(\s*)\\|(\s* )([0-9]+)(\+*\-*)", line, re.I):
                    temp = re.split("\\|", "".join(line.replace("+", " ").replace("-", " ").split()))
                    self.thedata.append(temp)
                else:
                    if re.search("( files changed, )|(insertions\\(\\+\\),)|(deletions\\(-\\))", line, re.I):
                        fid = re.split("([0-9]+)", "".join(line.split()))
                        for s in fid:
                            if not re.search("([0-9]+)", s):
                                fid.remove(s)
                        print fid
                        self.fixdata.append(fid)

                    if re.search("create", line):
                        cf = re.split("(createmode[0-9]+)", "".join(line.split()))
                        for s in cf:
                            # if re.search("createmode",s,re.I):
                            #     print "*",s
                            #     cf.remove(s)
                            if s == "":
                                cf.remove(s)
                        print cf
                        self.createdata.append(cf)
                    if re.search("delete", line):
                        df = re.split("(deletemode[0-9]+)", "".join(line.split()))
                        for s in df:
                            if s == "":
                                df.remove(s)
                        self.deletedata.append(df)
                        print df
        print self.thedata
        f.close()
        self.fixdata.append(isFix)
        self.fixdata.append(subject)
