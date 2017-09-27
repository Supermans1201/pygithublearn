#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：测试gensim使用
时间：2016年5月21日 18:07:50
"""

from gensim.models import word2vec
import gensim.corpora
import logging

# 主程序
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

model = word2vec.Word2Vec.load("diff_java.model")

import networkx as nx
import matplotlib.pyplot as plt
from pylab import mpl
G=nx.Graph()
blacknode=set([])
def get(startwordlist):
    result = []
    for word in startwordlist:
        y2 = model.most_similar(word)  # 20个最相关的
        for item in y2:
            if not item[0] in blacknode:
                result.append(item[0])
                G.add_node(item[0])
                G.add_weighted_edges_from([(word, item[0], item[1])])
        blacknode.add(word)
    return result
start=["intent"]
i=0;
while True:
    i+=1;
    if i==3:
        break
    result=get(start)
    print result
    start = result
for node in G.nodes():
    print node
pos = nx.spring_layout(G)
nx.draw(G, pos=pos,node_color="r", with_labels=True,node_size=900,font_size=10)
plt.show()


# # 寻找对应关系
# print ' "boy" is to "father" as "girl" is to ...? \n'
# y3 = model.most_similar(['girl', 'father'], ['boy'], topn=3)
# for item in y3:
#     print item[0], item[1]
# print "--------\n"
#
# more_examples = ["he his she", "big bigger bad", "going went being"]
# for example in more_examples:
#     a, b, x = example.split()
#     predicted = model.most_similar([x, b], [a])[0][0]
#     print "'%s' is to '%s' as '%s' is to '%s'" % (a, b, x, predicted)
# print "--------\n"
#
# # 寻找不合群的词
# y4 = model.doesnt_match("breakfast cereal dinner lunch".split())
# print u"不合群的词：", y4
# print "--------\n"

if __name__ == "__main__":
    pass