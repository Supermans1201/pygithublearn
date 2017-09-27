import os
import re
os.remove('F:/LM/pygithub_leran/text8/difftext')
difff=open('F:/LM/pygithub_leran/text8/difftext','a')
def getnumfromtxt(filepath):
    fixdata=[]
    thedata=[]
    deletedata=[]
    createdata=[]
    f = open(filepath)
    line = f.readline()
    isFix=False
    subject=""
    start=False
    diff=False
    print filepath
    while line:
        line = f.readline()

        if "Subject" in line:
            subject=line
        if re.search(u"fix",line,re.I):
            isFix=True

        if "---\n" == line:
            start=True
        if line.startswith("diff"):
            start=False
            print line
            fn=line.split()
            # print fn
            try:
                if fn[2][2:]==fn[3][2:]:
                    ft=fn[2][2:]
                    # print ft
                    for td in thedata:
                        if td[0].startswith(".../"):
                            tt = td[0][4:]
                            if ft.endswith(tt):
                                td[0]=ft
                    if ft.endswith(".jar") or ft.endswith(".so")or ft.endswith(".aar") or ft.endswith("png") or ft.endswith("jpg") or ft.endswith(".keystore"):
                        start=True
                                # print "**",ft, tt
                                # print
            except:
                print "td"
                import time
                time.sleep(10)


        if start==False:
            newline=line.replace(", ",",").replace("}"," } ").replace(";"," ; ")
            difff.write(newline)
            pass
            if line.startswith("+") or line.startswith("-"):
                if not (line.startswith("+++") or line.startswith("---")):
                    pass
            # print line

        if start==True:
            if re.search("(\s*)\\|(\s* )([0-9]+)(\+*\-*)", line, re.I):
                temp=re.split("\\|", "".join(line.replace("+", " ").replace("-", " ").split()))
                thedata.append(temp)
            else:
                if re.search("( files changed, )|(insertions\\(\\+\\),)|(deletions\\(-\\))",line,re.I):
                    fid=re.split("([0-9]+)","".join(line.split()))
                    for s in fid:
                        if not re.search("([0-9]+)",s):
                            fid.remove(s)
                    # print fid
                    fixdata.append(fid)

                if re.search("create",line):
                    cf= re.split("(createmode[0-9]+)","".join(line.split()))
                    for s in cf:
                        # if re.search("createmode",s,re.I):
                        #     print "*",s
                        #     cf.remove(s)
                        if s=="":
                            cf.remove(s)
                    createdata.append(cf)
                if re.search("delete",line):
                    df=re.split("(deletemode[0-9]+)", "".join(line.split()))
                    for s in df:
                        if s=="":
                            df.remove(s)
                    deletedata.append(df)

    f.close()
    fixdata.append(isFix)
    fixdata.append(subject)
    return fixdata,thedata,createdata,deletedata

rootDir="F:/LM/pygithub_leran/diff_fixissue/"
import shutil
result={}
data={}
create={}
delete={}

list_dirs = os.walk(rootDir)

for root, dirs, files in list_dirs:
    i =0
    datatemp=[]
    for f in files:
        i+=1
        path=os.path.join(root, f)
        result[f],data[f],create[f],delete[f]=getnumfromtxt(path)
    print i

difff.close()