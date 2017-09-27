from pygitthub.yuchulilei import  Yuchuli
import time
e=Yuchuli()
print e.__doc__
print e.__dict__

e.gendiffpredealtxt()
print "java"

e.gendiffpredealtxt(type ="java")
print "xml"

e.gendiffpredealtxt(type= "xml")