# Project 4: <br/> NLP - What they talk about when they talk about...Graduating
An analysis of Commencement speeches in the U.S.


###### Metis Weeks 6.5, 7, and 8

## Introduction

Every year, colleges or universities invite noted speakers such as tech leaders, politicians, famous writers, influential people in academia or entertainment etc. to address the graduating class. Through natural language processing, this project analyzes these heartening and poignant speeches, identifying both their common traits and what makes them stand out.

## Objective

Learn from successful leaders in different fields about giving an inspirational or motivational speech. Three aspects are discussed:
* **WHAT?**  ➜ Speech topics and trend of topic over the years
* **WHO?**  ➜ Distribution of topics compared among audiences from different locations
* **HOW?**  ➜ Evoluation of sentiment throughout the speech compared among spkearers with different professions

## Findings

### 1. Trend of topics over the years
From topic modeling based on all speeches, 8 topics are identified:
* Family & Friends
* Women's voice
* New generation & Nation
* Tech & Business
* Hardship
* Sportsmanship
* Arts & Science
* Dream

The percent stacked area chart below shows the trend of topic over the years. Each color represents a topic.

![alt text](https://github.com/katiehuang1221/onl_ds5_project_4/blob/main/img/topic_trend_legend_white.png)

**Observations**: Family & Friends is always a popular topic in the past 2 decades. However, Women's voice only starts appearing in the late 2000s. In 2004, New generation & Nation has the largest portion. Tech & Business increases in 2005 but is then replaced by Hardship in 2008. The latter two may be related to the presidential election in 2004 or the global financial crisis in 2007-2008. However, the sample size (400+ speech transcripts) is rather small for drawing any solid conclusions.



### 2. Topic distribution

> **A. Different audicne (based on region)**
> 
> ![alt text](https://github.com/katiehuang1221/onl_ds5_project_4/blob/main/img/topic_region_perc.png)
>
> **Observations**: At first glance, West and East regions have similar topic distribution with West having slighly larger portions for Hardship and Nation. There are more talks about Sports (sportsmanship) and Arts & Science in the East. Interestingly, while West and East have comparable portion for Women's voice, it is nonexistent in Central region.


  <br/>
  <br/>
  
  
> **B. Different speaker (based on speaker profession)**
> ![alt text](https://github.com/katiehuang1221/onl_ds5_project_4/blob/main/img/topic_profession.png)
> 
> **Observations**: For artists and athletes, the speech topics are less diversified. Artists talk a lot about arts and hardship and athletes talk mostly about sports (not surprising). While speakers in academia and politics both have a large portion with topic of New generation and nation, the context is a little different. The former talks about new generation in terms of knowledge, and the latter is about country and history. Speakers in the entertainment industry tend to share stories and advice (included in the topic of Family & Friends). Among all professions, more (percentage wise) speakers in the publishing industry (including writers, journalists, etc) address Women's voice. And close to half of the speakers in tech or business (47%) have Dream as their speech topic.

  <br/>
  <br/>


### 3. Sentiment Analysis
![alt text](https://github.com/katiehuang1221/onl_ds5_project_4/blob/main/img/sent_profession_1x4.png)

Above comparison among different speaker profession shows that speakers in entertainment and tech industry tend to remain positive throughout the speech. However, the evolution of sentiment in speeches from laywers, doctors, or academic researchers shows a different pattern. They may start with a positive opening and ending, but become less positive or even negative in the middle of the speech.

  <br/>
  <br/>


### 4. Network Analysis

A network of speakers is constructed based on the overlap of words used in their speeches. It shows the relation between the speeches/speakers from another perspective other than the conventional bag of words topic modeling.

![alt text](https://github.com/katiehuang1221/onl_ds5_project_4/blob/main/img/network.png)




---

### Data Source

 * Transcripts:
   * [Graduation Wisdom](https://www.graduationwisdom.com/archive/archive000.htm)
   * [Charlie Harrington, FloyHub](https://www.floydhub.com/whatrocks/datasets/commencement)
 * Speaker info and institute info:
   * Google


### Features

<ins>*Speech*</ins>
  - Year
  - Transcript length
  - Transcript bag of words

<ins>*Speaker*</ins>
  - Profession
  - Year born
  - Age when giving the speech

<ins>*Institute*</ins>
  - Latitude, longitude (decimal degrees)
  - Region (East, Central, West of the U.S.)
  
  
 


### Skills

 * `numpy`, `pandas`
 * `scikit-learn`
 * `gensim`, `nltk`, `textblob`
 * `matplotlib`, `seaborn`
 * `networkx`, `textnets`


### Analysis
*Model detailss can be found in link to Jupyter Notebooks:*

#### Topic Models

 * **[NMF](https://github.com/katiehuang1221/onl_ds5_project_4/blob/main/notebook/05_topic_modeling_refine.ipynb)** 
    * Non-Negstive Matrix Factorization: `sklearn.decomposition.NMF`
    * with TF-IDF (Term Frequency - Inverse Document Frequency): `sklearn.feature_extraction.text.TfidfVectorizer`
 * **[LDA](https://github.com/katiehuang1221/onl_ds5_project_4/blob/main/notebook/04_topic_modeling_1.ipynb)**
    * Latent Dirichlet Allocation: `gensim.models.LdaModel`
    * with CountVectorizer: `sklearn.feature_extraction.text.CountVectorizer`

 * **[K-means](https://github.com/katiehuang1221/onl_ds5_project_4/blob/main/notebook/04_topic_modeling_2.ipynb)**
    * Speech clustering
    * Pipline: `sklearn.decomposition.TruncatedSVD`,`sklearn.cluster.KMeans`
 

 
#### Sentiment Analysis

 * **[VADER](https://github.com/katiehuang1221/onl_ds5_project_4/blob/main/notebook/07_sentiment_analysis_refine.ipynb)**
    - Valence Aware Dictionary for Sentiment Reasoning: `nltk.sentiment.vader`
    - Polarity scores: negative, neutral, positive, compound
 * **[TextBlob](https://github.com/katiehuang1221/onl_ds5_project_4/blob/main/notebook/07_sentiment_analysis.ipynb)**
    - `textblob.TextBlob`
    - Polarity (negative ⟷ positive)
    - Subjectivity (facts ⟷ opinions)

 * **[NRC Emotional Lexicon](https://github.com/katiehuang1221/onl_ds5_project_4/blob/main/notebook/08_emotion.ipynb)**
    - `nrclex.NRCLex`
    - NRC emotion dictionary: positive, joy, anticipation, trust, surprise, negative, fear, anger, sadness, disgust
    

 
#### Visualization

 * LDA topic modeling: [pyLDAvis](https://github.com/katiehuang1221/onl_ds5_project_4/blob/main/notebook/10_VIZ_topic_pyLDAvis.ipynb)
 * Network analysis: [networkx, textnets](https://github.com/katiehuang1221/onl_ds5_project_4/blob/main/notebook/09_VIZ_speaker_word.ipynb)

