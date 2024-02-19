import requests
from bs4 import BeautifulSoup

def scrape_reviews(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    reviews = []    
    # print(soup.find_all('div', class_='reviewText'),'k')
    review_elements = soup.find_all('div', class_='reviewText')
    for review_element in review_elements:  
         review_text = review_element.get_text().strip()
         reviews.append(review_text)
        # review_text = review.find('div', class_='review-text-content').text.strip()
        # rating = review.find('span', class_='a-icon-alt').text.strip()
        # date = review.find('span', class_='review-date').text.strip()
        # Extract other relevant metadata as needed
        # print (review_text)
        # reviews.append({
        #     'text': review_text,
        #     'rating': rating,
        #     'date': date
        # })

    return reviews

# Example usage:
url = 'https://www.amazon.com/Motorola-Stylus-Battery-Unlocked-Twilight/dp/B0CBNLS6BD/ref=sr_1_1?_encoding=UTF8&dib=eyJ2IjoiMSJ9.kfROMMDIKYnan3LoQqYNNf4XEVb0ruMr1VotmPpPfDqxGyxsbJ9qmADvxk7ppETuF8u4CRp_e7WqvGe5rz7rCOvcQ-P3ux8Cgnpu8Gge7o7DTbqt1BSTDaSYjJpmdS3Dynmv0KnkeIWS8hCgG8fqfu1UxZnpsth1LlJj66mWl4rSkEQQIuF_M0e2uAZF7tm4O3p9Bg3PDbLXm25eJ8rYe-kTO6DzjEr1DrFkX6FvP04.fBLOx3d3EyBNlyb2pyXW_u1HaQfRBTYu4J36jbtUR1A&dib_tag=se&keywords=smartphones&sr=8-1&th=1z'
reviews = scrape_reviews(url)
print(reviews,234)
