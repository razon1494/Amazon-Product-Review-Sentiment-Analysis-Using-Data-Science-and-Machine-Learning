import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# nltk.data.path.append('C:/Users/Tech Land/AppData/Roaming/nltk_data')  

sia = SentimentIntensityAnalyzer() 
sample_text = "This product is absolutely amazing!"
sentiment_scores = sia.polarity_scores(sample_text) 

print(sentiment_scores)  
