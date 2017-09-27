from pygitthub.paqulei import  Paqu

e=Paqu()
print e.__doc__
print e.__dict__
print e.__module__

e.genAllcommentstomongodb()

for k,v in e.__dict__.items():
    print k,":",v

for k,v in Paqu.__dict__.items():
    print k,":"