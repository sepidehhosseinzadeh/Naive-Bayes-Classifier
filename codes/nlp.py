from wiki import Wiki
from wikipedia import Wikipedia
from wiki2plain import Wiki2Plain
import sys
sys.path.append('/home/sepideh/pywikibot/') 
import pywikibot
import urllib2
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
import re
import string
import pdb


path = '/home/sepideh/Desktop/Tasks_Interview/news360/data/'
categories = ['natural causes', 'suicide', 'accident', 'homicide']
documents = []
doc_words = [] 
for category in categories: 
    data_file = pd.read_csv(path+category+'.csv')
    for i in range(len(data_file.iloc[:,0])):
        url = data_file.iloc[i,0]

        # pdb.set_trace() 
        # extract words
        #req = urllib2.Request(url)
        #response = urllib2.urlopen(req)
        #raw = response.read().decode('utf8')
        #tokens = word_tokenize(raw)
        #words = nltk.Text(tokens)
        lang = 'simple'
        wiki = Wiki(lang)
        wikipedia = Wikipedia(lang)
 
      
        # get a list of wikipedia links
            
        site = pywikibot.Site("wikidata", "wikidata")
        repo = site.data_repository()
        item = pywikibot.ItemPage(repo, u"Q42")
        item.get()
        links = item.sitelinks
        
        for j in range(len(links)):
            pdb.set_trace()
            raw = wikipedia.article(links[j])
       
        if raw:
            wiki2plain = Wiki2Plain(raw)
            content = wiki2plain.text

        pdb.set_trace()
        
        documents.append((words, category))
        doc_words.extend(words)
        
pdb.set_trace()
all_words = nltk.FreqDist(str(w).lower() for w in doc_words)
word_features = list(all_words)[:2000] # [_document-classify-all-words]

def document_features(document): # [_document-classify-extractor]
    document_words = set(document) # [_document-classify-set]
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features


featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)


print(nltk.classify.accuracy(classifier, test_set))







