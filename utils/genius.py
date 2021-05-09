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

def search_genius(term):
    '''Search Genius API via artist name.'''
    client_access_token = get_cat()
    
    search = "/search?q="
    query = base + search + urllib.parse.quote(term.replace(' ','_'))
    request = urllib.request.Request(query)

    request.add_header("Authorization", "Bearer " + client_access_token)
    request.add_header("User-Agent", "")

    response = urllib.request.urlopen(request, timeout=3)
    raw = response.read()
    data = json.loads(raw)['response']['hits']
    return_data = response.read()
    encoding = response.info().get_content_charset('utf-8')


    for item in data:
        print('(id: ' +
              str(str(item['result']['primary_artist']['id']) +') ').ljust(10) +
              item['result']['primary_artist']['name'] + 
              ': ' + 
              item['result']['title'])