# %%
import nltk

ps = nltk.PorterStemmer()

def stemming(tokenized_text):
    text = [ps.stem(word) for word in tokenized_text]
    return text

def stemming_apply(Series):
    Series = Series.apply(lambda x: stemming(x))
    return Series