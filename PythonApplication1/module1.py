import numpy as np
import pandas as pd
import json
import glob

#Gensim   - Models
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel

#spacy    Models
import spacy
import nltk
from nltk.corpus import stopwords


#ignore filter warnings
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

#english stopwords
stopwords = stopwords.words("english")
def remove_stopwords(texts):
    return [" ".join([word for word in simple_preprocess(str(doc)) 
             if word not in stopwords]) for doc in texts]

#read data from CSV
data = pd.read_csv (r'testData.csv')


# clean the data, turn words into  roots

def sent_to_words(sentences):
    for sentence in sentences:
        # deacc=True removes punctuations
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))


def lemmatization(texts, allowed_postags=["NOUN", "ADJ", "VERB", "ADV"]):
    nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])
    texts_out = []
    for text in texts:
        doc = nlp(text)  #words in final form
        new_text = []
        for token in doc:
            if token.pos_ in allowed_postags:
                new_text.append(token.lemma_)
        final = " ".join(new_text)
        texts_out.append(final)
        print(texts_out)
    return (texts_out)



# Load the regular expression library
import re

# Remove punctuation
data['paper_text_processed'] = \
data['content'].map(lambda x: re.sub('[,\/.!?]', '', x))

# Convert the titles to lowercase
data['paper_text_processed'] = \
data['paper_text_processed'].map(lambda x: x.lower())
print(data)

data_words = list(data['paper_text_processed'].values)
data_words=remove_stopwords(data_words)
#data_words2=list(data_words2)






#data_words=["institution","academic","respecting"]
lemmatized_texts  = lemmatization(data_words) 
print (lemmatized_texts[0][0:90])





#lowercase and de-tokenize
def gen_words(texts):
    final = []
    for text in texts:
        new = gensim.utils.simple_preprocess(text, deacc=True)
        final.append(new)
    return (final)

data_words = gen_words(lemmatized_texts)
print (data_words)

#gives id and number of occurencies to every word
id2word = corpora.Dictionary(data_words)
corpus = []
for text in data_words:
    new = id2word.doc2bow(text)
    corpus.append(new)

print (corpus)


#from pprint import pprint
## number of topics
#num_topics = 10
## Build LDA model
#lda_model = gensim.models.LdaMulticore(corpus=corpus,
#                                       id2word=id2word,
#                                       num_topics=num_topics)
## Print the Keyword in the 10 topics
#pprint(lda_model.print_topics())
#doc_lda = lda_model[corpus]




