import requests

def get_response(q):
  
  return requests.get(f'https://newsapi.org/v2/everything?q={q}&from=2021-10-21&sortBy=publishedAt&apiKey=c90cc5c1426844ceaad1d1cb3af6dec7').json()

def display_articles(articles):

  num = len(articles)
  if len(articles) > 5:
    print("Showing top 5 results\n\n------------------------------\n")
    num = 5

  for x in range(num):

    print(articles[x]['title'], "by", articles[x]['author'])
    print("Article from", articles[x]['source']['name'], "\n")

    print(articles[x]['description'])
    print("Read more on", articles[x]['url'], "\n\n------------------------------\n")

def get_input():

  response = get_response(input("Query (e.g. Tesla): "))

  if response['status'] == 'ok':

    print(f"\n{response['totalResults']} total results.")

    display_articles(response['articles'])

print("News - API from www.newsapi.org")

get_input()