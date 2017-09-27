from pygitthub.fenxilei import  Fenxi
import time
e=Fenxi()
print e.__doc__
print e.__dict__

e.gendiff()
for k,v in e.__dict__.items():
    print k,":",v

for k,v in Fenxi.__dict__.items():
    print "-"+k,":"