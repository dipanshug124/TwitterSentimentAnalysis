# %%
import string

def remove_punc(text):
    text_nopunct = "".join([char for char in text if char not in string.punctuation]) #Removing punctuations in the text
    return text_nopunct

def remove_punc_apply(Series):
    Series = Series.apply(lambda x: remove_punc(x))
    return Series