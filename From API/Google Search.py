from requests import get
from textwrap import fill
from format_num import format_num

query = input("Query: ").replace(" ", "+")
search_type = input("Search type (Search, Images, News): ").lower()
if search_type not in ["images", "news"]:
    search_type = "search"
print("Connecting to https://api.goog.io/...")
response = get(
    f"https://api.goog.io/v1/{search_type}/q={query}",
    headers={'apikey': '1922fec2-2a05-4566-9b10-d386da861864'}
).json()

if search_type == "search":
    for item in response['results']:
        print("\n")
        print(item['title'])
        print(item['link'])
        print(fill(item['description']))
    print(f"\n{format_num(response['total'])} results in {round(response['ts'], 2)} seconds.")
elif search_type == "images":
    for item in response['image_results']:
        print("\n")
        print(item['link']['title'])
        print("Image:", item['image']['src'])
        print("Page:", item['link']['href'])
else:
    for item in response['entries']:
        print("\n")
        print(item['title'])
        print("Published", item['published'])
        print(item['link'])
