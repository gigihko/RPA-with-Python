import requests

r = requests.get('https://newsapi.org/v2/everything?qInTitle=united%20states&from=2024-2-01&to=2024-2-18&sortBy=popularity&language=en&apiKey=2c42bbaf32384d13b6f0556529844652')

content = r.json()

articles = content['articles']
print(type(articles))

for article in articles:
    print('TITLE\n', article['title'], '\nDESCRIPTION\n', article['description'])