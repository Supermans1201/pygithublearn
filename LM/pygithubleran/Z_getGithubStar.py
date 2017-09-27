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
        if re.search(u"class=\"list-group-item paginated_item\" href",line,re.I):
            fid = re.split("><", line)
            temp=re.split(" ",fid[1])
            temp2=re.split("\"",temp[3])
            print temp2[1]




    f.close()

    return allcommitsha,thedata

rootDir="F:/LM/pygithub_leran/star4"
getnumfromtxt(rootDir)