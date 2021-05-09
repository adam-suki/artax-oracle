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

    requrl = '/'.join([base, path])
    token = "Bearer {}".format(client_access_token)
    if headers:
        headers['Authorization'] = token
    else:
        headers = {"Authorization": token}

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
        
def get_song_ids(artist_id):
    '''Get all the song id from an artist.'''
    current_page = 1
    next_page = True
    songs = []

    while next_page:
        path = "artists/{}/songs/".format(artist_id)
        params = {'page': current_page}
        data = get_json(path=path, params=params)

        page_songs = data['response']['songs']
        if page_songs:
            songs += page_songs
            current_page += 1
            print("Page {} finished scraping".format(current_page))
            
            # Breaking early while testing
            if current_page == 2:
                break
        else:
            next_page = False

    print("Song id were scraped from {} pages".format(current_page))
    songs = [song["id"] for song in songs
            if song["primary_artist"]["id"] == artist_id]
    return songs