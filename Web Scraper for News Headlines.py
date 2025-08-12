import requests
from bs4 import BeautifulSoup
import re

def scrape_headlines(url):
    """
    Fetches headlines from a given URL.
    """
    try:
        # Use requests to send a GET request to the URL[cite: 1].
        # A GET request is used to retrieve data from a specified resource.
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful (HTTP status code 200)[cite: 7].
        response.raise_for_status()

        # Parse the HTML content using BeautifulSoup.
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all h2 tags, as they often contain headlines.
        # The find_all() method is used to find all occurrences of a tag.
        headline_elements = soup.find_all('h2')

        headlines = []
        for element in headline_elements:
            # The .text attribute returns the text content of an element.
            headline_text = element.get_text(strip=True)
            if headline_text:
                headlines.append(headline_text)

        return headlines
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def save_headlines_to_file(headlines, filename):
    """
    Saves a list of headlines to a text file.
    """
    if headlines:
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                for headline in headlines:
                    f.write(headline + '\n')
            print(f"Successfully saved {len(headlines)} headlines to {filename}")
        except IOError as e:
            print(f"Error writing to file: {e}")

if __name__ == "__main__":
    # Example URL (replace with the news website you want to scrape)
    news_url = 'https://www.bbc.com/news'
    
    print(f"Scraping headlines from: {news_url}")
    scraped_headlines = scrape_headlines(news_url)

    if scraped_headlines:
        output_file = 'headlines.txt'
        save_headlines_to_file(scraped_headlines, output_file)
    else:
        print("No headlines were scraped.")