import feedparser

# Define the RSS feed URL
rss_url = 'https://rthk9.rthk.hk/rthk/news/rss/e_expressnews_efinance.xml'


def scrape(url=rss_url):
    # Parse the feed
    feed = feedparser.parse(url)

    title = []
    description = []
    raw_news_collection = []

    # Iterate over each entry in the feed and print the title
    for entry in feed.entries:
        title.append(entry.title)
        description.append(entry.description)
        raw_news_collection = title + description

    return raw_news_collection
