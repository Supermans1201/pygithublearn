# encoding:utf=8
from pymongo import MongoClient

client = MongoClient()
# admin
# local
# test
for dbname in client.database_names():
    print dbname
# 连接数据库
db = client['androidbug']
# 连接对应的数据集
for collname in db.collection_names():
    print collname
#collection
coll = db['commits']
print coll


