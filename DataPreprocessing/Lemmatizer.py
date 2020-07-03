import nltk

wn = nltk.WordNetLemmatizer()

def lemmatizing(tokenized_text):
    text = [wn.lemmatize(word) for word in tokenized_text]
    return text

def lemmatizing_apply(Series):
    Series = Series.apply(lambda x: lemmatizing(x))
    return Series
