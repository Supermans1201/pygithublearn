
from pymongo import MongoClient
def openmongdb():
    client = MongoClient()
    db = client['androidbug']
    coll = db['commits']
    return coll

coll=openmongdb()
cursor = coll.find({"sha":"4db849d2b049cc25d05cd599bf9515f0657206db"})
for document in cursor:
    print(document)