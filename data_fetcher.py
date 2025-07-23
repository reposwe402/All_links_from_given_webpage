import requests as rq

def fetch_data(url):
    return rq.get(url)
