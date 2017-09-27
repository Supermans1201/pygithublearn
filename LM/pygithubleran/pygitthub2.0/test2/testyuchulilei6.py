from pygitthub.yuchulilei import  Yuchuli

e=Yuchuli()
print e.__doc__
print e.__dict__
print e.__module__



for k,v in e.__dict__.items():
    print k,":",v

for k,v in Yuchuli.__dict__.items():
    print "-"+k,":"