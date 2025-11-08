thonimport json
from extractors.google_news_parser import GoogleNewsParser
from outputs.exporters import export_to_json
from config.settings import SETTINGS

def run_scraper():
    # Initialize the scraper with settings from the config
    news_parser = GoogleNewsParser(SETTINGS)
    
    # Extract articles based on the settings
    articles = news_parser.scrape_news()
    
    # Export the data to JSON
    export_to_json(articles, SETTINGS['output_file'])

if __name__ == "__main__":
    run_scraper()