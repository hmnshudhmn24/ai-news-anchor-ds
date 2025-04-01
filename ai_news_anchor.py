import requests
import pyttsx3
from newspaper import Article
from bs4 import BeautifulSoup
from transformers import pipeline
import time

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speech rate
engine.setProperty('volume', 1.0)  # Volume level

# Load summarization model
summarizer = pipeline("summarization")

# News API configuration (Use a valid API key)
NEWS_API_KEY = "your_news_api_key"
NEWS_API_URL = "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + NEWS_API_KEY

def get_news():
    response = requests.get(NEWS_API_URL)
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get("articles", [])
        return articles[:5]  # Get top 5 articles
    else:
        print("Error fetching news")
        return []

def extract_article_content(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

def summarize_text(text):
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def main():
    print("Fetching latest news...")
    news_articles = get_news()
    
    if not news_articles:
        print("No news found.")
        return
    
    for idx, article in enumerate(news_articles):
        print(f"\nNews {idx + 1}: {article['title']}")
        speak_text(f"News {idx + 1}: {article['title']}")
        
        content = extract_article_content(article['url'])
        summary = summarize_text(content)
        
        print(f"Summary: {summary}")
        speak_text(summary)
        time.sleep(2)

if __name__ == "__main__":
    main()
