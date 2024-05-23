import json
from generation_llama2_13b import caching_news_mechanism
from web_scraping import scrape


def lambda_handler(event, context):
    scraping_result = scrape()
    summarized_news = caching_news_mechanism(scraping_result)

    return {
        'statusCode': 200,
        'body': json.dumps(summarized_news),
    }
