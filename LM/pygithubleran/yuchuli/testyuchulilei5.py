from yuchuli.yuchulilei import  Yuchuli

e=Yuchuli()
print e.__doc__
print e.__dict__

# e.gendiffpicture("intent",type="all")

word=e.getsmailarword("SNAPSHOT",type="all",number=10)
print word
# e.gendiffpicture("intent",type="xml")