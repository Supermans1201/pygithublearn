from pygitthub.yuchulilei import  Yuchuli
import time
e=Yuchuli()
print e.__doc__
print e.__dict__

e.gendiffsanitizationtxt(type="all")
#
#
# print "java"
# time.sleep(10)
e.gendiffsanitizationtxt(type="java")
#
# print "xml"
e.gendiffsanitizationtxt(type="xml")


