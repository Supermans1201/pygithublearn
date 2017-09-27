from tiquxinxi.dushujuku import Dushujuku

a= Dushujuku()

coll=a.openmongdb("comments")
print coll.find()

coll=a.openmongdb("issues")
print coll.find()

coll=a.openmongdb("commits")
print coll.find()

coll=a.openmongdb("diffinfo")
print coll.full_name

print coll.find_one()