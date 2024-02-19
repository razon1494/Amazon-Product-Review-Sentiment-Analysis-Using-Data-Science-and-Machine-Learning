import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords  # For optional refinement 
from nltk.tokenize import word_tokenize  

# ---------------------- Data Loading -----------------------
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# ---------------------- Language Filtering -----------------------
from langdetect import detect

def preprocess(data):
    english_reviews = []
    for index, row in data.iterrows(): 
        review_text = row['review']  

        # Basic (current) cleaning 
        review_text = review_text.lower()  

        if detect(review_text) == 'en':
           english_reviews.append(review_text)

    return english_reviews

# ---------------------- Feature-Opinion Extraction (NLP) --------------------
def extract_feature_opinion_nlp(query):
    tokens = word_tokenize(query)  
    tagged_tokens = nltk.pos_tag(tokens) 

    feature = None  # Initialize in case a feature isn't found
    opinion = None  # Initialize in case an opinion isn't found

    for word, tag in tagged_tokens:
        if 'NN' in tag:   
            feature = word
        if 'JJ' in tag: 
            opinion = word

    return feature, opinion

# ---------------------- Sentiment with VADER ---------------------
# nltk.download('vader_lexicon')  # Ensure you have the lexicon downloaded
# nltk.download('stopwords')      # For optional stopwords use
# nltk.download('punkt')          # For required tokenization

sia = SentimentIntensityAnalyzer() 

# Customize stopwords as needed for your product review domain
custom_stopwords = ['and', 'of', 'the', 'to']  # Expand upon this
all_stopwords = stopwords.words('english') + custom_stopwords

# ----------------------- Example Usage -------------------------
data = load_data('my_reviews.csv')  # Update with your file path
cleaned_reviews = preprocess(data.copy()) 

# Sample Query to demonstrate
query = "[phone screen: issues]" 
feature, opinion = extract_feature_opinion_nlp(query)

if feature is not None and opinion is not None:  # Ensure an opinion existed 
    # Preprocess (remove stopwords etc.) if desired
    opinion_words = word_tokenize(opinion.lower())  
    opinion_filtered = [w for w in opinion_words if w not in all_stopwords]
    opinion = ' '.join(opinion_filtered) 

    sentiment_score = sia.polarity_scores(opinion)['compound']  
    print(f"Query: {query}")
    print(f"Feature: {feature}, Opinion: {opinion}, Sentiment Score: {sentiment_score}")
else:  
    print(f"Query: {query} - Unable to calculate sentiment (Either feature or opinion was missing)")


# Now integrate query parsing, extraction, and scoring in a loop over cleaned_reviews 
