import requests
from bs4 import BeautifulSoup

def extract_news_headlines(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the elements containing news headlines
        headlines = soup.find_all('h2', class_='headline')
        
        # Extract and print the headlines
        for headline in headlines:
            print(headline.text.strip())
    else:
        print("Failed to retrieve data from the website.")

if __name__ == "__main__":
    # URL of the website containing news headlines
    url = "https://example.com/news"
    
    # Call the function to extract news headlines
    extract_news_headlines(url)

