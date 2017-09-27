from paiqu.paqulei import  Paqu

e=Paqu()
print e.__doc__
print e.__dict__
for k,v in e.__dict__.items():
    print k,":",v

e.genAllcommentstomongodb()
