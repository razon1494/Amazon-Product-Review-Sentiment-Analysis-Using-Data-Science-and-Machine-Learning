import pandas as pd
from langdetect import detect

data = pd.read_csv('my_reviews.csv')  # Assume you saved your data

def preprocess(data):
    english_reviews = []
    for index, row in data.iterrows(): 
        review_text = row['review']  

        # Basic (current) cleaning 
        review_text = review_text.lower()  

        if detect(review_text) == 'en':
           english_reviews.append(review_text)

    return english_reviews

cleaned_reviews = preprocess(data.copy()) 
print(cleaned_reviews[:5])  # View few sample results
