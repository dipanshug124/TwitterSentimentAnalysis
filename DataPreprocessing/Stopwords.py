# %%
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))

## Creating a list of custom stopwords
new_words = ["using", "show", "result", "large", "also","iv", "one", "two", "new",
             "previously", "shown","covid","twitter","situation","la","corona","pic",
             "com","http","bit","ly","india","people","nan'","nan","html'","html'","nan","html '"]

stop_words = stop_words.union(new_words)

def remove_stopwords(text):
    text_sp = [words for words in text if words not in stop_words]
    return text_sp

def remove_stopwords_apply(Series):
    Series = Series.apply(lambda x: remove_stopwords(x))
    return Series