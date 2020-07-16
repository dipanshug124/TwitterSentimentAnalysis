# SBSPS-Challenge-2598-Twitter-Sentiment-Analysis  
The sentiment analysis of Indians after the extension of lockdown announcements to be analyzed with the relevant #tags on twitter and build a predictive analytics model to understand the behavior of people if the lockdown is further extended. Also develop a dashboard with visualization of people reaction to the govt announcements on lockdown extension.  

`Website Link`: [TSA](https://smartpracticeschool.github.io/SBSPS-Challenge-2598-Twitter-Sentiment-Analysis/Visualization%20Website/sap/index.html)  
`Video Explaination`: https://drive.google.com/file/d/1n9pUBTNtpbAKnvoJ0HTzufntSq60fyFa/view?usp=sharing  
`PPT Explaination`: https://drive.google.com/file/d/1ZMPTEt26YY8UiGMDeT5MknRKUEoF11lZ/view?usp=sharing  

## Objective
Twitter hosts abundant user-generated posts, which closely reflect the public’s reactions towards this pandemic with low latency.  
Collecting and analyzing different demographic data helps compare and contrast that how different groups are affected in society.  

**Libraries**
* `Numpy` :http://www.numpy.org/
* `Pandas` :http://pandas.pydata.org
* `matplotlib` :http://matplotlib.org/
* `seaborn` :https://seaborn.pydata.org
* `Datetime` :https://docs.python.org/3/library/datetime.html
* `Statistics` :https://docs.python.org/3/library/statistics.html
* `textblob` :https://textblob.readthedocs.io/en/dev/  

**Software Recommended**
* [Jupyter Notebook](http://ipython.org/notebook.html)
* [Anaconda](http://continuum.io/downloads) installed with `Python 3.8`  
* [IBM Cloud](http://cloud.ibm.com/), used IBM Watson Tone Analyzer service

## Project Miletones  
1) Data Gathering
2) Data Preprocessing
3) Analyzing Polarity and Subjectivity
4) Analyzing emotions using IBM Watson Tone Analyzer
5) Data Visualization
6) Creating Visualization Dashboard

**Data Gathering**  
Tweets are scraped using web-scraping. Scraped data is stored in JSON format and then combining each tweet, converted into .csv file. CSV file then goes for data preprocessing.  
Click [here](https://github.com/SmartPracticeschool/SBSPS-Challenge-2598-Twitter-Sentiment-Analysis/blob/master/tweet_dataset.csv) for dataset.  

**Data Preprocessing**
1) Remove Punctuations
2) Tokenizing Words
3) Stop words Removal
4) Stemming
5) Lemmatizing  
Click [here](https://github.com/SmartPracticeschool/SBSPS-Challenge-2598-Twitter-Sentiment-Analysis/tree/master/DataPreprocessing)  

**Analyzing Polarity and Subjectivity**  
Each Tweet will be subdivided according to Polarity and Subjectivity:
  Polarity: Ranges from -1 to +1, -1 being most negative and +1 being most positive comment.
  Subjectivity: Ranges from 0 to 1, w.r.t its analytics.
`TextBlob` has predefined functions and NLP models embedded in it, which makes this task efficient and smooth.  
  [Sentiments](https://github.com/SmartPracticeschool/SBSPS-Challenge-2598-Twitter-Sentiment-Analysis/tree/master/Sentiments) folder contains all files for this process.  
  [Textblob functions](https://github.com/SmartPracticeschool/SBSPS-Challenge-2598-Twitter-Sentiment-Analysis/blob/master/Sentiments/PolaritySubjectivity.py) file contains imported textblob library and functions are created.  
  [Polarity Subjectivity Analysis](https://github.com/SmartPracticeschool/SBSPS-Challenge-2598-Twitter-Sentiment-Analysis/blob/master/Sentiments/PolaritySubjectivity.py) file implement those functions on dataset.  
  [Polarity Subjectivity Dataset](https://github.com/SmartPracticeschool/SBSPS-Challenge-2598-Twitter-Sentiment-Analysis/blob/master/PolaritySubjectivity.csv) is created.  

**Analyzing tweet using IBM Watson Tone Analyzer**  
Analyzes the sentiment in the deeper way to classify and reveal the trend more comprehensively.  
This technique uses linguistic analysis to detect joy, sadness, anger, fear, analytical, tentative and also confidence tones found in text.  
  [ToneAnalyzer](https://github.com/SmartPracticeschool/SBSPS-Challenge-2598-Twitter-Sentiment-Analysis/tree/master/ToneAnalyzer) folder contains all files for this process.  
  [IBM Watson Tone Analyzer](https://github.com/SmartPracticeschool/SBSPS-Challenge-2598-Twitter-Sentiment-Analysis/blob/master/ToneAnalyzer/IBMToneAnalyzerAPI.ipynb), code for calling API from IBM Cloud Service.  
  [Dataset Creation](https://github.com/SmartPracticeschool/SBSPS-Challenge-2598-Twitter-Sentiment-Analysis/blob/master/ToneAnalyzer/SentimentDatasetCreation.ipynb), seperate dataset is created for each sentiment.  

**Data Visualization**  
Technologies used:  
1) Matplotlib  
2) Plotly  
3) Tableau  
4) Seaborn  

**Creating Visualization Dashboard**  
Stack used:  
1) HTML  
2) CSS  
3) JavaScript  
4) Tableau  
5) Bootstrap  

[Website code](https://github.com/SmartPracticeschool/SBSPS-Challenge-2598-Twitter-Sentiment-Analysis/tree/master/Visualization%20Website)  

## Summary  
You can visit [Visualization Dashboard](https://smartpracticeschool.github.io/SBSPS-Challenge-2598-Twitter-Sentiment-Analysis/Visualization%20Website/sap/index.html) for analyzing tweets. 





