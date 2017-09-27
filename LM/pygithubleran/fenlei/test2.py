
from gensim.models import word2vec
import gensim.corpora
import gensim.models.doc2vec
import gensim.corpora.dictionary
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
model = word2vec.Word2Vec.load("F:/LM/pygithub_leran/yuchuli/codinguser_gnucash-android_diff_java.model")

dictionary=gensim.corpora.dictionary.Dictionary.load_from_text("F:/LM/pygithub_leran/yuchuli/codinguser_gnucash-android_directory.txt")
print len(dictionary)


from fenxi.fenxilei2 import  Fenxi

e=Fenxi()
print e.__doc__
print e.__dict__
#
e.getinfofromtxt("F:/LM/pygithub_leran/paiqu/testpaqu/codinguser_gnucash-android/diff3/0ff839d07e555b9aa5247a74f2c69d1d10a74261.txt")
# 0a134d1b59bc398a9f5cfca48e1d44ca3dd1839f.txt
e.getinfofromtxt("F:/LM/pygithub_leran/paiqu/testpaqu/codinguser_gnucash-android/diff3/0a134d1b59bc398a9f5cfca48e1d44ca3dd1839f.txt")


def function(y=["+","-"]):
    add=[]
    sub=[]
    other=[]
    for sentence in y:
        if sentence.startswith("+"):
            add.append(sentence)
        elif sentence.startswith("-"):
            sub.append(sentence)
        else:
            other.append(sentence)
    print add

    dealadd = []
    dealsub = []
    print sub
    print other
    for sentence in add:
        for word in sentence.split():
            dealadd.append(word)
    for sentence in sub:
        for word in sentence.split():
            # print "*",word,"*"
            # tempsmalarword= model.most_similar(word,topn=10)
            # sword=[]

            dealsub.append(word)
            # for sw in tempsmalarword:
            #     sword.append(sw[0])
            # print  sword
    print dictionary.doc2bow(dealadd)
    print dictionary.doc2bow(dealsub)
    pass

for k, kv in e.diffdata.items():
    print k
    if k.endswith("xml"):
        print "pass"
    else:
        for x, y in kv.items():
            print x, y
            function(y)




