import os
import re
def getnumfromtxt(filepath):
    allcommitsha=[]
    thedata=[]
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
        if "diff" in line:
            start=False

            # print line

        if start==False:
                pass
                # print "".join(line.split())

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
                    print fid

                if re.search("create",line):
                    cf= re.split("(createmode[0-9]+)","".join(line.split()))
                    for s in cf:
                        # if re.search("createmode",s,re.I):
                        #     print "*",s
                        #     cf.remove(s)
                        if s=="":
                            cf.remove(s)
                    print cf
                if re.search("delete",line):
                    df=re.split("(deletemode[0-9]+)", "".join(line.split()))
                    for s in df:
                        if s=="":
                            df.remove(s)
                    print df

    f.close()
    allcommitsha.append(isFix)
    allcommitsha.append(subject)
    return allcommitsha,thedata

rootDir="F:/LM/pygithub_leran/diff/"
import shutil
result={}
data=[]
list_dirs = os.walk(rootDir)

for root, dirs, files in list_dirs:
    i =0
    datatemp=[]
    for f in files:
        i+=1
        path=os.path.join(root, f)
        result[f],datatemp=getnumfromtxt(path)
        for dt in datatemp:
            data.append(dt)
    print i, len(data)

for d in data:
    pass
    # print "***",d

# for  f,y in result.items():
#     # print f,y
#     if True in y:
#         print f, y
#         shutil.move(rootDir+f, "F:/LM/pygithub_leran/diff_fixissue/"+f)