from gensim.models import word2vec
import gensim.corpora
import logging


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

model = word2vec.Word2Vec.load("codinguser_gnucash-android_diff.model")


print model.wv['intent']