import warnings
warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt
import re
import numpy as np
import pandas as pd
import gensim
import nltk

from nltk.stem.snowball import SnowballStemmer

from gensim.corpora import Dictionary, MmCorpus
from gensim.models import ldamodel

from sklearn.cluster import KMeans
from sklearn.manifold import MDS
from sklearn.decomposition import PCA


def load_dataset(filename):
    file = open(filename, 'r')

    acc_names = []
    tweets = []

    for line in file:
        line = line.strip()
        parts = line.split(',')
        acc_names.append(parts[0])
        tweets.append(parts[-1])

    return acc_names, tweets

# config variables
num_topics=10

# pre-processing:
# 1. lowercasing
# 2. stopword removal
# 3. stemming

stemmer = SnowballStemmer("english")
stopwords = nltk.corpus.stopwords.words('english')

def preprocess(text):

    # tokenizing and lowercasing
    tokens = [word.lower() for word in text.split()]
    filtered_tokens = []

    # buat yang bukan terdiri dari alfabet, dan merupakan stopword
    for token in tokens:
        if re.search('[a-zA-Z]', token) and (token not in stopwords):
            filtered_tokens.append(token)

    # lakukan stemming dengan snowball stemmer
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems

# Kita load dokumen data, dan lakukan preprocessing terhadap data
acc_names, tweets = load_dataset("input.txt")

# Lakukan pre-process untuk setiap tweet pada koleksi "tweets" kita
# Gunakan List Comprehension untuk mempermudah hidup kita
tweets = [preprocess(tweet) for tweet in tweets]


# membuat term dictionary dari korpus kita, dimana setiap kata unik akan diberikan sebuah index
dictionary = Dictionary(tweets)

# buang term yang:
# 1. muncul di kurang dari 2 dokumen
# 2. muncul di lebih dari 0.9*(total_dok) dokumen
# dictionary.filter_extremes(no_below=1, no_above=0.1)

# ubah dictionary menjadi object bag-of-words reference
# ingat bahwa dalama LDA, dokumen diasumsikan dengan bag-of-words model
corpus = [dictionary.doc2bow(tweet) for tweet in tweets]
#with open("output.txt", "a") as a:
#a.writelines(tweets)
print (', '.join(map(str,tweets)))
#print (filtered_sentence)
#print (str(tweets)[1:-1])
#print(*tweets, sep = ', ')
##
### Run the LDA !
##lda = ldamodel.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, random_state=1, iterations=5000)
##
### tampilkan topic matrix
##topics_matrix = lda.show_topics(formatted=False)
##
##for topic_no, topic_words in topics_matrix:
##
##    print ('topic number: {}'.format(topic_no))
##
##    # default: top-10 kata yang paling tinggi probabilitasnya
##    for word, prob in topic_words:
##        print (word, prob)
##
##### bentuk terlebih dahulu vektor dokumen/tweet
##### vektor tweet/dokumen = vektor probabilitas terhadap masing-masing topik
####tweet_vectors = []
####for tweet in tweets:
####    probs = [prob for (_,prob) in lda.get_document_topics(dictionary.doc2bow(tweet))]
####    tweet_vectors.append(probs)
####tweet_vectors = np.array(tweet_vectors)
##
### kita set banyaknya cluster = banyaknya topik
##num_clusters = num_topics
##
### gunakan algoritma K-Means, dan lakukan clustering !
##km = KMeans(n_clusters=num_clusters)
##km.fit(word,prob)
##
### jika kita ingin melihat indeks cluster untuk setiap tweet/dokumen
##clusters = km.labels_.tolist()
##
##print (clusters)
##
### untuk setiap cluster center, kita sort argumen/index berdasarkan nilai probabilitasnya
### karena index/argumen adalah id topik.
###
### jadi, secara intuisi, ini adalah cara untuk mencari topik major yang dibicarakan di sebuah cluster
### nantinya, wakil kata cluster akan diambil dari 2 topik major di setiap cluster
###
### ::-1 artinya reverse list
##
##order_centroids = km.cluster_centers_.argsort()[:, ::-1]
##
##cluster_names = {}
##for i in range(num_clusters):
##    print ("cluster %d words:" % i)
##    
##    # ambil 2 topik major untuk setiap cluster
##    topic_words = []
##    for ind in order_centroids[i, :1]:
##        topic_words += [dictionary.get(word_id) for (word_id, prob) in lda.get_topic_terms(ind, topn=2)]
##    
##    #cluster_names[i] = ','.join(topic_words)
##
##    #print (cluster_names[i])
##
##    print (','.join(map(str,topic_words)))
##
