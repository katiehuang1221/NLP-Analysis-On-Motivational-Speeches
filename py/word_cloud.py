"""
Generating Word Cloud
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud
from sklearn.feature_extraction import text 
from sklearn.feature_extraction.text import CountVectorizer


def cv_dtm(df,column_name):
    """
    Input: corpus (Ex: speech_clean_2, 'transcript')
    Output: Document-Term Matrix (rows: documents, columns: words)
    
    """
    
    cv = CountVectorizer(stop_words='english')
    data_cv = cv.fit_transform(df[column_name])

    data_dtm = pd.DataFrame(data_cv.toarray(), columns=cv.get_feature_names())
    data_dtm.index = df.index
    
    return data_dtm



def show_word_cloud(df, column_name, add_stop_words, collocation_threshold = 30):
    """
    Input: df, column_name (Ex:speech_clean_2.transcript)
    Output: show Word Cloud of first 16 speeches
    
    """

    # Reset the output dimensions
    plt.rcParams['figure.figsize'] = [20, 8]

    stop_words = text.ENGLISH_STOP_WORDS.union(add_stop_words)
    wc = WordCloud(stopwords=stop_words, background_color="white", colormap="Dark2",
                       max_font_size=150, random_state=42,
                       collocation_threshold = collocation_threshold)

    for index, speech in enumerate(df[column_name].iloc[:16]):
        wc.generate(speech)
        plt.subplot(4, 4, index+1)
        plt.imshow(wc, interpolation="bilinear")
        plt.axis("off")
        
    plt.show()