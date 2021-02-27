"""
Functions for text cleaning of raw transcript

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from collections import Counter

from sklearn.feature_extraction import text 
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans
from sklearn.pipeline import make_pipeline

from sklearn.decomposition import NMF
from sklearn.preprocessing import normalize

from wordcloud import WordCloud

from gensim import matutils, models
import scipy.sparse

import re
import string

import nltk
from nltk import pos_tag
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer

# Preparation for topic modeling
# Handle words to remove
add_stop_words = ['like','youre','ive','im','really','id','ve','just','dont','didnt','thi','wa',
                  'say','know','make','people']

boring_words = ['say','like','just','dont','don','im',
                'ive','youll','youve','things','thing','youre','right','really','lot',
                'make','know','people','way','day','class',
                'little', 'maybe','niagara','university','dartmouth','woman', 'womens', 'men','wellesley',
                'shirtwaist','scripps','aidan','tuskegee','dr','colleges', 'guy', 'dave',
                'arts','montgomery','girls', 'musicians',
                'sisters','kind',
                #'parents','parent','family','friends','hearts', # added on 02/24/2021

                
                ]

import pickle
with open("../dump/common_words.txt", "rb") as f:   # Unpickling
    common_words = pickle.load(f)
    
add_stop_words = add_stop_words + common_words + boring_words
stop_words = text.ENGLISH_STOP_WORDS.union(add_stop_words)



def tfidf_dtm(df,column_name,add_stop_words=[]):
    """
    Input: corpus (Ex: speech_clean_2, 'transcript')
    Output: Document-Term Matrix (rows: documents, columns: words)
    
    """
    tfidf = TfidfVectorizer(stop_words=stop_words)
    data_tfidf = tfidf.fit_transform(df[column_name])

    tfidf_dtm = pd.DataFrame(data_tfidf.toarray(), columns=tfidf.get_feature_names())
    tfidf_dtm.index = df.index
    
    return tfidf_dtm


def remove_names(sentence):
    sentence_list = sentence.split()
    tagged_sentence = nltk.tag.pos_tag(sentence_list)
    edited_sentence = [word for word,tag in tagged_sentence if tag != 'NNP' and tag != 'NNPS']
    return ' '.join(edited_sentence)

def clean_text_1(text):
    text = text.lower()
    text = re.sub('commencement speech transcript','',text)
    text = re.sub('\[.*?\]','',text)
    text = re.sub('[%s]' % re.escape(string.punctuation),'',text)
    text = re.sub('\w*\d\w*','',text)
    text = re.sub('[-]','',text)
    text = re.sub('[–’“”…]','',text)
    text = re.sub('\xa0','',text)
    text = re.sub('\n','',text)
    text = re.sub('\r','',text)
    return text


def lemmaSentence(text):
    wordnet_lemmatizer = WordNetLemmatizer()
    token_words=word_tokenize(text)
    token_words
    lemma_sentence=[]
    for word in token_words:
        lemma_sentence.append(wordnet_lemmatizer.lemmatize(word, pos="v"))
        lemma_sentence.append(" ")
    return "".join(lemma_sentence)


def nouns(text):
    '''Given a string of text, tokenize the text and pull out only the nouns.'''
    is_noun = lambda pos: pos[:2] == 'NN'
    tokenized = word_tokenize(text)
    all_nouns = [word for (word, pos) in pos_tag(tokenized) if is_noun(pos)] 
    return ' '.join(all_nouns)


def wash(df,column_name):
    """
    Given the df and column_name, will perform three steps of cleaning
    (remove names, basic clean, lemmatization) and return the df.
    
    """
    
    # Remove names
    df[column_name] = df[column_name].apply(remove_names)

    # Basic cleaning
    df[column_name] = df[column_name].apply(lambda x: clean_text_1(x))

    # Lemmatization
    df[column_name] = df[column_name].apply(lambda x: lemmaSentence(x))

    # Choose only nouns
    df['nouns'] = df[column_name].apply(nouns)
    
    
    return df


