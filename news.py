import requests

API_KEYS = 'eee994c3c9ae488c8774193384ae14e7'

def news():
    url = f"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey={API_KEYS}"
    news = requests.get(url).json()

    article = news['articles']

    news_dict = {}

    for i, arti in enumerate(article, start=1):
        news_name = arti['source']['name']
        news_title = arti['title']

        if i in news_dict:
            news_dict[i]['name'].append(news_name)
            news_dict[i]['title'].append(news_title)
        else:
            news_dict[i] = {'name': [news_name], 'title': [news_title]}

    return news_dict

# news_data = news()

# # Print the dictionary
# for key, value in list(news_data.items())[:5]:
#     print(key)
#     print(value['name'][0])
#     print(value['title'][0])
#     print('-' * 30)
