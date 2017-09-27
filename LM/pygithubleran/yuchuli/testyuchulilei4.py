from yuchuli.yuchulilei import  Yuchuli

e=Yuchuli()
print e.__doc__
print e.__dict__

# e.gendiffpicture("intent",type="all")

e.gendiffpicture("SNAPSHOT",type="all")

# e.gendiffpicture("intent",type="xml")