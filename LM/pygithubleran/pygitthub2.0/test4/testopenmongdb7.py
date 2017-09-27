from pygitthub.dushujuku import  Dushujuku
import time
e=Dushujuku()
print e.__doc__
print e.__dict__

# e.gendiff()
for k,v in e.__dict__.items():
    print k,":",v

for k,v in Dushujuku.__dict__.items():
    print "-"+k,":"