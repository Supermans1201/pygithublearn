from gensim.models import word2vec
import gensim.corpora
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus(u"F:/LM/pygithub_leran/yuchuli/codinguser_gnucash-android_difftext")

dictionary = gensim.corpora.Dictionary(sentences)
print len(dictionary)
dictionary.save_as_text("dictonary", sort_by_word=True)
for text in sentences:
    print "**",text
    print "??",dictionary.doc2bow(text)
# print len(dictionary)
# print dictionary.token2id
corpus = [dictionary.doc2bow(text) for text in sentences]
# print corpus
tfidf = gensim.models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
for doc in corpus_tfidf:
    pass
    # print doc
# print tfidf.dfs
# print tfidf.idfs
lsi = gensim.models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=2)
lsi.print_topics(2)