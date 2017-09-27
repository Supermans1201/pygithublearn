import os
import re
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
                                # print "**",ft, tt
                                # print
            except:
                print td
                import time
                time.sleep(10)


        if start==False:
            pass
            print "".join(line.split())

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

# for key,value in data.items():
#     print key,value
#
# for key, value in create.items():
#     print key, value
# for key, value in delete.items():
#     print key, value

# deal={}
# for d in data:
#     deal[d[0]]=deal.get(d[0],0)+int(d[1])
#     pass
#     print "***",d
# dealtype={"java":0,"xml":0,"gradle":0,"md":0,"txt":0,"other":0,"gnucash":0}
# for x, y in deal.items()
    # ]\:
#     if x.endswith("java"):
#         dealtype["java"]+=y
#     elif x.endswith("xml"):
#         dealtype["xml"]+=y
#     elif x.endswith("gradle"):
#         dealtype["gradle"]+=y
#     elif x.endswith("md"):
#         dealtype["md"]+=y
#     elif x.endswith("txt"):
#         dealtype["txt"]+=y
#     elif x.endswith("gnucash"):
#         dealtype["gnucash"] += y
#     else:
#         dealtype["other"]+=y
#         print x, y
#
#
# print dealtype
# for  f,y in result.items():
#     # print f,y
#     if True in y:
#         print f, y
#         shutil.move(rootDir+f, "F:/LM/pygithub_leran/diff_fixissue/"+f)