thonimport requests
from datetime import datetime

class GoogleNewsParser:
    def __init__(self, settings):
        self.keywords = settings['keywords']
        self.region_language = settings['region_language']
        self.timeframe = settings['timeframe']
        self.api_url = "https://newsapi.org/v2/everything"
        self.api_key = settings['api_key']
    
    def scrape_news(self):
        # Make a request to the Google News API
        params = {
            'q': self.keywords,
            'language': self.region_language.split(":")[1],
            'from': datetime.now().strftime('%Y-%m-%d'),
            'to': datetime.now().strftime('%Y-%m-%d'),
            'apiKey': self.api_key
        }
        response = requests.get(self.api_url, params=params)
        
        if response.status_code != 200:
            raise Exception("Failed to fetch news from Google News API")
        
        articles = response.json().get("articles", [])
        return self._parse_articles(articles)
    
    def _parse_articles(self, articles):
        parsed_articles = []
        for article in articles:
            parsed_article = {
                'title': article.get('title'),
                'source': article.get('source', {}).get('name'),
                'url': article.get('url'),
                'description': article.get('description'),
                'publishedAt': article.get('publishedAt'),
                'publishedTimestamp': int(datetime.strptime(article.get('publishedAt'), '%Y-%m-%dT%H:%M:%S.%fZ').timestamp() * 1000),
                'image': article.get('urlToImage'),
                'metadata': {
                    'scrapeTimestamp': datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                    'language': self.region_language.split(":")[1],
                    'region': self.region_language.split(":")[0],
                    'keyword': self.keywords,
                    'timeframe': self.timeframe
                }
            }
            parsed_articles.append(parsed_article)
        return parsed_articles