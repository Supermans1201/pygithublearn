from pygitthub.yuchulilei import  Yuchuli

e=Yuchuli()
print e.__doc__
print e.__dict__

e.genmodel(type="all")

e.genmodel(type="java")

e.genmodel(type="xml")