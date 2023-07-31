import collections
from utils import *


articles_db = load_data("data/clean.json")
category_map = collections.defaultdict(set)
url2category = {}

# Organize urls into categories
for article in articles_db:
    cur = article["category"]
    category_map[cur].add(article["url"])

# Create URL-to-category mapping
for i, article in enumerate(articles_db):
    category = article["category"]
    url = article["url"]
    url2category[url] = category

user_profile = load_data("data/user.json")
history = set(user_profile["readingHistory"])

# Process user interested categories
interested = []
for read in history:
    if read in url2category:
        category = url2category[read]
        interested.append(category)

# Recommend articles
rec_list = []
for c in interested:
    rec_list.extend(category_map[c])

# Remove articles that user have read
output = []
for article in rec_list:
    if article not in history:
        output.append(article)
# print(len(rec_list), len(output))