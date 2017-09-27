#!/usr/bin/env python
# -*- coding: utf-8 -*-


from gensim.models import word2vec
import gensim.corpora
import logging

# 主程序
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus(u"F:/LM/pygithub_leran/yuchuli/codinguser_gnucash-android_difftext")  # 加载语料

dictionary = gensim.corpora.Dictionary(sentences)
print len(dictionary)
dictionary.save_as_text("dictonary", sort_by_word=True)

print len(dictionary)
print dictionary.token2id
corpus = [dictionary.doc2bow(text) for text in sentences]
print corpus
tfidf = gensim.models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
for doc in corpus_tfidf:
    print doc
print tfidf.dfs
print tfidf.idfs
lsi = gensim.models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=2)
lsi.print_topics(2)
# model_2 = word2vec.Word2Vec.load("text8.model")

if __name__ == "__main__":
    pass