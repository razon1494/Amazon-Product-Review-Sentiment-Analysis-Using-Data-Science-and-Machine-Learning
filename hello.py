import pandas as pd
import re
from langdetect import detect
def load_and_clean(file_path):
    encodings = ['utf-8', 'ISO-8859-1']  # Encodings to try

    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file: 
                lines = file.readlines()  

            good_data = []
            inconsistent_lines = []

            for line in lines:
                if re.match(r"__label__\d+\s+(.*)", line): 
                    parts = line.split(maxsplit=1)

                    # Trimming Spaces 
                    parts[0] = parts[0].strip()  # Trim label
                    parts[1] = parts[1].strip()  # Trim review

                    # Lenient Cleaning (for now)
                    # clean_review = parts[1].lower()
                    parts[1] = parts[1].lower()
                    clean_review = re.sub(r"[^\w\s\-'\?!]", "", parts[1]) 
                    parts[1] = clean_review
                    good_data.append(parts) 
                else:
                    inconsistent_lines.append(line)


            df = pd.DataFrame(good_data, columns=['label', 'review'])
            return df, inconsistent_lines

        except UnicodeDecodeError:
            print(f"UnicodeDecodeError with encoding: {encoding}. Trying the next one...")
            continue  # Try the next encoding

    # If all encodings fail:
    raise Exception("Failed to find a suitable encoding. Check your data source.")

data, inconsistent_lines = load_and_clean('reviews.txt')
print(data.head())
data.to_csv('my_reviews.csv')
# Print a few sample inconsistent lines 
print("Sample Inconsistent Lines:")
print(inconsistent_lines[:5])  

