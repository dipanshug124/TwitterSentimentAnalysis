# %%
from textblob import TextBlob

# Create a function to get subjectivity
def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity

# Create a function to get polarity
def getPolarity(text):
    return TextBlob(text).sentiment.polarity

# #Create two new columns
# df_clean['Subjectivity'] = df_clean['Tweets'].apply(getSubjectivity)
# df_clean['Polarity'] = df_clean['Tweets'].apply(getPolarity)

def getAnalysis(score):
    if score < 0:
        return 'Negative'
    elif score ==0:
        return 'Neutral'
    else:
        return 'Positive'
