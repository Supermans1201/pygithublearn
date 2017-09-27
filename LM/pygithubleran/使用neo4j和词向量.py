#!/usr/bin/env python
# -*- coding: utf-8 -*-
from py2neo import Graph, Node, Relationship

g = Graph("http://localhost:7474", username="neo4j", password="123456")


from gensim.models import word2vec
import logging


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

model = word2vec.Word2Vec.load("diff8.model")
node=set([])

def get(startwordlist):
    result = []
    for word in startwordlist:
        node.add(word)
        y2 = model.most_similar(word)
        for item in y2:
            result.append(item[0])
            node.add(item[0])
    return result
start=["activity"]
i=0;

while True:
    i+=1;
    if i==6:
        break
    result=get(start)
    print result
    start = result
print len(node)
for n in node:
    print n,










if __name__ == "__main__":
    pass



