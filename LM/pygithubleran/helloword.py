
def getmin2(list,s,e,k=5,m=3):
    result = []
    if m==1:
        temp=[]
        for j in range(k + 1):
            temp.append(-float("inf"))
        temp[0] = float("inf")

        for j in range(1,k+1):
            for i in range(s,e+1):
                if list[i]<temp[j-1] and list[i]>temp[j]:
                    temp[j]=list[i]
        for t in temp:
            if not t == float("inf"):
                result.append(t)
        return result

    if k/m<1:
        return getmin2(list,s,e,k,1)
    else:
        for i in range(m):
            ns=s+i*(((e+1-s)/m))
            ne=ns+((e+1-s)/m-1)
            nk=k/m
            if not nk*m ==k:
                nk=nk+1
            if ne+(e+1-s)%m==e:
                ne=e
            temp=getmin2(list,s=ns,e=ne,k=nk,m=m)

            for t in temp:
                if not t==-float("inf"):
                    result.append(t)
        return getmin2(result, 0, len(result) - 1, k, 1)


list = []
slist = raw_input().split()
for s in slist:
    list.append(int(s))
k = int(raw_input())


print getmin2(list,0,e=len(list)-1,k=k,m=k)