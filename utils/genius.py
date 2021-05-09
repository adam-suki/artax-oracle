import json
import requests
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

base = "https://api.genius.com"

def get_cat():
    with open('genius.txt') as f:
        client_access_token = f.readline()
    return client_access_token

def get_json(path, params=None, headers=None):
    '''Send request and get response in json format.'''
    
    client_access_token = get_cat()

    # Generate request URL
    requrl = '/'.join([base, path])
    token = "Bearer {}".format(client_access_token)
    if headers:
        headers['Authorization'] = token
    else:
        headers = {"Authorization": token}

    # Get response object from querying genius api
    response = requests.get(url=requrl, params=params, headers=headers)
    response.raise_for_status()
    return response.json()