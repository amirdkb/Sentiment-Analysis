import pandas as pd 
import time
import numpy as np 
from gensim.corpora import Dictionary
from sklearn.preprocessing import LabelEncoder


def doc_preprocess(data) :
    with open('stopwords.txt', 'r') as file:
        stopwords = file.read().rstrip()   #read the stop words file
    df = pd.read_csv(data,encoding='latin-1')
    #remove all non-letter characters
    df['review'] = (df['review'].str.replace('[^a-zA-Z]', ' ',regex=True)).str.lower()
    #remove the short words (length ≤ 2) 
    df['review'] = df['review'].str.findall('\w{3,}').str.join(' ')
    #remove all stop words
    df['review'] = df['review'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stopwords)]))
    df['review'] = df['review'].str.split()
    #tokenize the data and convert the text to word sequences
    # max_len = (df['review'].str.len()).max()
    max_len = 878
    for index , list in enumerate(df.review) :
        rng = max_len - len(list)
        for i in range(rng):
            list.append('0')  #padding
        df.review[index]= list
    doc = df.review 
    dic = Dictionary(doc)
    for i ,row in enumerate(df.review) :
        df.review[i] = dic.doc2idx(row)
    #label encoding
    le = LabelEncoder()
    df.sentiment =le.fit_transform(df.sentiment)
    x = df['review']
    y = df['sentiment']

    return np.asarray(x.to_list()) , np.asarray(y.to_list())

