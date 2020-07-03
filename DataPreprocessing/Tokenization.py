# %%
#Tokenization
import re
import string

def tokenization(text):
    text_token = re.split('\W+',text) #Returns a match where the string does contain only word characters
    return text_token
def tokenization_apply(Series):
    Series = Series.apply(lambda x: tokenization(x.lower()))
    return Series