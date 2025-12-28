import requests 

query = input("What type of news are you intrested today?")
api = "88e6e24f25254275a9058daf900b273a"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-11-28&sortBy=publishedAt&apiKey={api}"

print(url)
r = requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index +1, article["title"], article["url"] )
    print("\n---------------------------------\n")
