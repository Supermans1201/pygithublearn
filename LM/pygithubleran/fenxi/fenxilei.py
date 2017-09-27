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
        self.fenxiresult=[]
        self.fenxifile={}
        self.filetypes=[".java",".xml",".gradle",".jar",".so",".aar","png","jpg",".keystore",".zip",".rar",".md",".txt",".bat",".classpath",".project",".gitignore","pro",".properties","yml","gradlew",".sh","yaml","CONTRIBUTORS","LICENSE",".gnucash","other"]
        self.filetypesmap={}

        self.javafilenamesmap={}
        self.xmlfilenamesmap = {}
        for theft in self.filetypes:
            self.filetypesmap[theft]=0
        self.others=set([])
        Fenxi.fenxiCount += 1

    def displayCount(self):
        print "Total Paqu %d" % Fenxi.fenxiCount

    def genHistogrampic(self, data={}, xlabel="x", ylabel="y", title="title"):
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体,解决中文显示问题
        n_groups = len(data.keys())
        datavalue = data.values()
        fig, ax = plt.subplots(figsize=(22, 10))
        index = np.arange(n_groups)
        # bar_width = 0.35
        bar_width = 0.2
        opacity = 0.4
        error_config = {'ecolor': '0.3'}
        rects1 = plt.bar(index, datavalue, bar_width,
                         alpha=opacity,
                         color='b',
                         # yerr=std_men,
                         error_kw=error_config,
                         label='datavalue')
        def autolabel(rects):
            for rect in rects:
                height = rect.get_height()
                ax.text(rect.get_x() + rect.get_width() / 2.0, 1.05 * height,
                        '%d' % int(height), ha='center', va='bottom')
        autolabel(rects1)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.xticks(index + bar_width, data.keys())
        plt.tight_layout()
        # plt.show()
        plt.savefig(title+"_"+".png")

    def genPiechartpic(self, data={}, title=""):
        # 调节图形大小，宽，高
        plt.figure(figsize=(16, 19))
        # 定义饼状图的标签，标签是列表
        labels = data.keys()
        # 每个标签占多大，会自动去算百分比
        sizes = data.values()
        patches, l_text, p_text = plt.pie(sizes, labels=labels, labeldistance=1.05, autopct='%3.1f%%', shadow=False, startangle=20, pctdistance=0.7)
        for t in l_text:
            t.set_size = (1)
        for t in p_text:
            t.set_size = (1)
        plt.axis('equal')

        plt.savefig(title + "_"  + ".png")

    def statisticsdifferentfiletype(self):
        print "统计文件类型..."
        list_dirs = os.walk(self.rootdir)
        for root, dirs, files in list_dirs:
            i = 0
            for f in files:
                i += 1
                print "处理第"+str(i)+"个",
                path = os.path.join(root, f)
                self.getfiletypefromtxt(path)
            print "共处理"+str(i)+"个文件"
        print self.filetypesmap
        for o in self.others:
            print o
        self.genHistogrampic(data=self.filetypesmap, xlabel=u"文件类型", ylabel=u"频率", title=u"P_文件类型_频率柱状图")
        self.genPiechartpic(data=self.filetypesmap, title=u"P_文件类型_频率饼图")

    def statisticsdifferentfilename(self):
        print "统计文件名称..."
        list_dirs = os.walk(self.rootdir)
        for root, dirs, files in list_dirs:
            i = 0
            for f in files:
                i += 1
                print "处理第"+str(i)+"个",
                path = os.path.join(root, f)
                self.getfilenameromtxt(path)
            print "共处理"+str(i)+"个文件"

        self.genPiechartpic(self.javafilenamesmap, title=u"P_Java程序类型_文件频数饼图")
        print len(self.javafilenamesmap)
        result=self.javaresultreduceone()
        self.genPiechartpic(result, title=u"P_Java程序类型_文件个数频数饼图")
        result = self.javaresultreducetwo()
        self.genPiechartpic(result, title=u"P_Java程序类型_文件种类个数频数饼图")

        self.genPiechartpic(self.xmlfilenamesmap, title=u"P_Xml程序类型_文件频数饼图")
        print len(self.xmlfilenamesmap)
        result = self.xmlresultreduceone()
        self.genPiechartpic(result, title=u"P_xml程序类型_文件个数频数饼图")
        result = self.xmlresultreducetwo()
        self.genPiechartpic(result, title=u"P_xml程序类型_文件个数频数饼图")

    def javaresultreduceone(self):
        result={}
        for jfk, jfv in self.javafilenamesmap.items():
            if re.search("Activity.java", jfk, re.I):
                result["activity"] = result.get("activity", 0) + jfv
            elif re.search("Service.java", jfk, re.I):
                result["service"] = result.get("service", 0) + jfv
            elif re.search("Provider.java", jfk, re.I):
                result["provider"] = result.get("provider", 0) + jfv
            elif re.search("Fragment.java", jfk, re.I):
                result["fragment"] = result.get("fragment", 0) + jfv
            elif re.search("View.java", jfk, re.I):
                result["view"] = result.get("view", 0) + jfv
            elif re.search("Dialog.java", jfk, re.I):
                result["dialog"] = result.get("dialog", 0) + jfv
            elif re.search("EditText.java", jfk, re.I):
                result["edittext"] = result.get("edittext", 0) + jfv
            elif re.search("Button.java", jfk, re.I):
                result["button"] = result.get("button", 0) + jfv
            elif re.search("Keyboard.java", jfk, re.I):
                result["keyboard"] = result.get("keyboard", 0) + jfv
            elif re.search("Layout.java", jfk, re.I):
                result["layout"] = result.get("layout", 0) + jfv
            elif re.search("Adapter.java", jfk, re.I):
                result["adapter"] = result.get("adapter", 0) + jfv
            elif re.search("Helper.java", jfk, re.I):
                result["helper"] = result.get("helper", 0) + jfv
            elif re.search("Handler.java", jfk, re.I):
                result["handler"] = result.get("handler", 0) + jfv
            elif re.search("Listener.java", jfk, re.I):
                result["listener"] = result.get("listener", 0) + jfv
            elif re.search("Test.java", jfk, re.I):
                result["test"] = result.get("test", 0) + jfv
            else:
                result["other"] = result.get("other", 0) + jfv
                # print jfk, jfv
        return result

    def javaresultreducetwo(self):
        result = {}
        for jfk in self.javafilenamesmap.keys():
            if re.search("Activity.java", jfk, re.I):
                result["activity"] = result.get("activity", 0) + 1
            elif re.search("Service.java", jfk, re.I):
                result["service"] = result.get("service", 0) + 1
            elif re.search("Provider.java", jfk, re.I):
                result["provider"] = result.get("provider", 0) + 1
            elif re.search("Fragment.java", jfk, re.I):
                result["fragment"] = result.get("fragment", 0) + 1
            elif re.search("View.java", jfk, re.I):
                result["view"] = result.get("view", 0) + 1
            elif re.search("Dialog.java", jfk, re.I):
                result["dialog"] = result.get("dialog", 0) + 1
            elif re.search("EditText.java", jfk, re.I):
                result["edittext"] = result.get("edittext", 0) + 1
            elif re.search("Button.java", jfk, re.I):
                result["button"] = result.get("button", 0) + 1
            elif re.search("Keyboard.java", jfk, re.I):
                result["keyboard"] = result.get("keyboard", 0) + 1
            elif re.search("Layout.java", jfk, re.I):
                result["layout"] = result.get("layout", 0) + 1
            elif re.search("Adapter.java", jfk, re.I):
                result["adapter"] = result.get("adapter", 0) + 1
            elif re.search("Helper.java", jfk, re.I):
                result["helper"] = result.get("helper", 0) + 1
            elif re.search("Handler.java", jfk, re.I):
                result["handler"] = result.get("handler", 0) + 1
            elif re.search("Listener.java", jfk, re.I):
                result["listener"] = result.get("listener", 0) + 1
            elif re.search("Test.java", jfk, re.I):
                result["test"] = result.get("test", 0) + 1
            else:
                result["other"] = result.get("other", 0) + 1
        return result

    def xmlresultreduceone(self):
        result = {}
        for jfk, jfv in self.xmlfilenamesmap.items():
            dealedjfk=re.split("/",jfk)[-1]
            if re.search("strings", dealedjfk, re.I):
                result["strings"] = result.get("strings", 0) + jfv
            elif re.search("styles", dealedjfk, re.I):
                result["styles"] = result.get("styles", 0) + jfv
            elif re.search("dimens", dealedjfk, re.I):
                result["dimens"] = result.get("dimens", 0) + jfv
            elif re.search("color", dealedjfk, re.I):
                result["color"] = result.get("colors", 0) + jfv
            elif re.search("arrays", dealedjfk, re.I):
                result["arrays"] = result.get("arrays", 0) + jfv
            elif re.search("pom.xml", dealedjfk, re.I):
                result["pom"] = result.get("pom", 0) + jfv
            elif re.search("AndroidManifest.xml",dealedjfk,re.I):
                result["androidmanifest"]=result.get("androidmanifest",0)+jfv
            elif re.search("fragment",dealedjfk,re.I):
                result["fragment"]=result.get("fragment",0)+jfv
            elif re.search("dialog",dealedjfk,re.I):
                result["dialog"]=result.get("dialog",0)+jfv
            elif re.search("button",dealedjfk,re.I):
                result["button"]=result.get("buttton",0)+jfv
            elif re.search("action",dealedjfk,re.I):
                result["action"]=result.get("action",0)+jfv
            elif re.search("abs",dealedjfk,re.I):
                result["abs"]=result.get("abs",0)+jfv
            elif re.search("toolbar",dealedjfk,re.I):
                result["toolbar"]=result.get("toolbar",0)+jfv
            elif re.search("header",dealedjfk,re.I):
                result["header"]=result.get("header",0)+jfv
            elif re.search("list", dealedjfk, re.I):
                result["list"] = result.get("list", 0) + jfv
            elif re.search("spinner", dealedjfk, re.I):
                result["spinner"] = result.get("spinner", 0) + jfv
            elif re.search("themes", dealedjfk, re.I):
                result["themes"] = result.get("themes", 0) + jfv
            elif re.search("flags", dealedjfk, re.I):
                result["flags"] = result.get("flags", 0) + jfv
            elif re.search("activity", dealedjfk, re.I):
                result["activity"] = result.get("activity", 0) + jfv
            elif re.search("view", dealedjfk, re.I):
                result["view"] = result.get("view", 0) + jfv
            elif re.search("keyboard", dealedjfk, re.I):
                result["keyboard"] = result.get("keyboard", 0) + jfv
            elif re.search("menu", dealedjfk, re.I):
                result["menu"] = result.get("menu", 0) + jfv
            else:
                result["other"] = result.get("other", 0) + jfv
                # print jfk,jfv
        return result
    def xmlresultreducetwo(self):
        result = {}
        for jfk in self.xmlfilenamesmap.keys():
            dealedjfk=re.split("/",jfk)[-1]
            if re.search("strings", dealedjfk, re.I):
                result["strings"] = result.get("strings", 0) +1
            elif re.search("styles", dealedjfk, re.I):
                result["styles"] = result.get("styles", 0) + 1
            elif re.search("dimens", dealedjfk, re.I):
                result["dimens"] = result.get("dimens", 0) + 1
            elif re.search("color", dealedjfk, re.I):
                result["color"] = result.get("colors", 0) + 1
            elif re.search("arrays", dealedjfk, re.I):
                result["arrays"] = result.get("arrays", 0) + 1
            elif re.search("pom.xml", dealedjfk, re.I):
                result["pom"] = result.get("pom", 0) + 1
            elif re.search("AndroidManifest.xml",dealedjfk,re.I):
                result["androidmanifest"]=result.get("androidmanifest",0)+1
            elif re.search("fragment",dealedjfk,re.I):
                result["fragment"]=result.get("fragment",0)+1
            elif re.search("dialog",dealedjfk,re.I):
                result["dialog"]=result.get("dialog",0)+1
            elif re.search("button",dealedjfk,re.I):
                result["button"]=result.get("buttton",0)+1
            elif re.search("action",dealedjfk,re.I):
                result["action"]=result.get("action",0)+1
            elif re.search("abs",dealedjfk,re.I):
                result["abs"]=result.get("abs",0)+1
            elif re.search("toolbar",dealedjfk,re.I):
                result["toolbar"]=result.get("toolbar",0)+1
            elif re.search("header",dealedjfk,re.I):
                result["header"]=result.get("header",0)+1
            elif re.search("list", dealedjfk, re.I):
                result["list"] = result.get("list", 0) + 1
            elif re.search("spinner", dealedjfk, re.I):
                result["spinner"] = result.get("spinner", 0) + 1
            elif re.search("themes", dealedjfk, re.I):
                result["themes"] = result.get("themes", 0) + 1
            elif re.search("flags", dealedjfk, re.I):
                result["flags"] = result.get("flags", 0) + 1
            elif re.search("activity", dealedjfk, re.I):
                result["activity"] = result.get("activity", 0) + 1
            elif re.search("view", dealedjfk, re.I):
                result["view"] = result.get("view", 0) + 1
            elif re.search("keyboard", dealedjfk, re.I):
                result["keyboard"] = result.get("keyboard", 0) + 1
            elif re.search("menu", dealedjfk, re.I):
                result["menu"] = result.get("menu", 0) + 1
            else:
                result["other"] = result.get("other", 0) + 1
        return result

    def getfiletypefromtxt(self, filepath):
        f = open(filepath)
        line = f.readline()
        self.thedata = []
        start = False

        print "正在处理...:", filepath
        while line:
            line = f.readline()

            if line.startswith("Subject"):
                start = True

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
                        infiletypes = False
                        for theft in self.filetypes:
                            if ft.endswith(theft):
                                self.filetypesmap[theft] += 1
                                infiletypes = True
                        if not infiletypes:
                            self.filetypesmap["other"] += 1
                            self.others.add(ft)
                except:
                    print "except"
                    import time
                    time.sleep(10)

            if start == False:
                pass
            if start == True:
                if re.search("(\s*)\\|(\s* )([0-9]+)(\+*\-*)", line, re.I):
                    temp = re.split("\\|", "".join(line.replace("+", " ").replace("-", " ").split()))
                    self.thedata.append(temp)
                else:
                    pass
        f.close()

    def getfilenameromtxt(self, filepath):
            f = open(filepath)
            line = f.readline()
            self.thedata = []
            start = False

            print "正在处理...:", filepath
            while line:
                line = f.readline()

                if line.startswith("Subject"):
                    start = True

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

                            if ft.endswith("java") :
                                self.javafilenamesmap[ft] = self.javafilenamesmap.get(ft,0)+1
                            if ft.endswith("xml"):
                                self.xmlfilenamesmap[ft] = self.xmlfilenamesmap.get(ft, 0) + 1


                    except:
                        print "except"
                        import time
                        time.sleep(10)

                if start == False:
                    pass
                if start == True:
                    if re.search("(\s*)\\|(\s* )([0-9]+)(\+*\-*)", line, re.I):
                        temp = re.split("\\|", "".join(line.replace("+", " ").replace("-", " ").split()))
                        self.thedata.append(temp)
                    else:
                        pass
            f.close()