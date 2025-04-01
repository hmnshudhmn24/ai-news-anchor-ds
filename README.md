# AI News Anchor

## Overview
AI News Anchor is a Python-based project that fetches the latest news, summarizes articles using NLP, and reads them aloud using a text-to-speech engine.

## Features
- Fetches real-time news from NewsAPI
- Extracts full article content
- Summarizes articles using Hugging Face transformers
- Reads the news aloud using pyttsx3
- Supports up to 5 latest news articles

## Installation

### Prerequisites
Ensure you have Python 3.7+ installed on your system.

### Install Dependencies
Run the following command to install required packages:
```bash
pip install requests pyttsx3 newspaper3k transformers beautifulsoup4
```

## Usage
1. Get a free API key from [NewsAPI](https://newsapi.org/).
2. Replace `your_news_api_key` in the script with your actual API key.
3. Run the script:
```bash
python ai_news_anchor.py
```

## How It Works
1. Fetches top 5 news articles using NewsAPI.
2. Extracts article content from URLs.
3. Summarizes each article using a transformer model.
4. Reads the summary aloud using text-to-speech.

## Future Enhancements
- Add a GUI for user interaction
- Support multiple languages
- Improve voice synthesis using neural TTS models
