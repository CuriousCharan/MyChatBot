import requests


def NewsFromGoogle():
    # Google news from newsapi
    main_url = " https://newsapi.org/v1/articles?source=google-news&sortBy=top&apikey=94e093be7d6d45afab7b0d09d9e8f8d1"

    l_news = ""
    # fetching data in json format
    open_google_page = requests.get(main_url).json()

    # getting all articles in a string article
    article = open_google_page["articles"]

    # empty list which will
    # contain all trending news
    results = []

    for ar in article:
        results.append(ar["title"])

    for i in article:
        l_news+= ("Title: " + i['title'] + "\n" +
              "Description: " + i['description'] + "\n" +
              "URL: " + i['url'] + "\n")


    return l_news

message = NewsFromGoogle()