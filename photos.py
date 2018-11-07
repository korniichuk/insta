#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import requests
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

def download_photos_by_ids(ids=[]):
    """Download photos from Google Photos by ids"""

    output = []

    service = setup_api()
    for _id in ids:
        result = service.mediaItems().get(mediaItemId=_id).execute()
        url = result['baseUrl']
        r = requests.get(url)
        if r.status_code == 200:
            with open(result['filename'], 'wb') as f:
                for chunk in r.iter_content(1024*2014):
                    f.write(chunk)
            output.append(result['filename'])
        else:
            return 1
    return output

def get_albums():
    """Get list of all Google Photos albums (first 50)"""

    service = setup_api()
    result = service.albums().list(pageSize=50).execute()
    albums = result.get('albums', [])
    if not albums:
        print('No albums found.')
    else:
        print('Your albums in Google Photos:')
        for album in albums:
            print("'{0}' album. Album id: {1}".format(album['title'],
                                                      album['id']))

def get_media_items():
    """Get list of all Google Photos media items (first 100)"""

    service = setup_api()
    result = service.mediaItems().list(pageSize=100).execute()
    items = result.get('mediaItems', [])
    if not items:
        print('No media items found.')
    else:
        print('Your media items in Google Photos:')
        for item in items:
            print("'{0}' media item. Media item id: {1}".format(
                    item['filename'], item['id']))

def get_photos_by_album_id(album_id):
    """Get list all of the photos in Google Photos album (first 100)"""

    output = []

    service = setup_api()
    body = {'albumId': album_id, 'pageSize': 100}
    result = service.mediaItems().search(body=body).execute()
    items = result.get('mediaItems', [])
    if not items:
        print('No media items found.')
    else:
        photos = []
        for item in items:
            if 'photo' in item['mediaMetadata']:
                photos.append(item)
    if not photos:
        print('No photos found.')
    else:
        print('Your photos in Google Photos:')
        for photo in photos:
            print("'{0}' photo. Photo id: {1}".format(
                    photo['filename'], photo['id']))
            output.append(photo['id'])
    return output

def setup_api():
    """Setup the Google Photos API"""

    SCOPES = 'https://www.googleapis.com/auth/photoslibrary.readonly'
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('photoslibrary', 'v1', http=creds.authorize(Http()))
    return service

# Example. Get list of all Google Photos albums (first 50)
#get_albums()

# Example. Get list of all Google Photos media items (first 100)
#get_media_items()

# Example. Get list all of the photos in Google Photos album (first 100) by
# 'AIcl5Br1e9_2x1l7NIOFVC2QrOqhCeEULW9OK9fWCm9MsvzJDeZcszmFhntItkoFb3Y3bldiqnQy'
# album id
#album_id = "AIcl5Br1e9_2x1l7NIOFVC2QrOqhCeEULW9OK9" \
#           "fWCm9MsvzJDeZcszmFhntItkoFb3Y3bldiqnQy"
#get_photos_by_album_id(album_id)

# Example.
#album_id = "AIcl5Br1e9_2x1l7NIOFVC2QrOqhCeEULW9OK9" \
#           "fWCm9MsvzJDeZcszmFhntItkoFb3Y3bldiqnQy"
#photo_ids = get_photos_by_album_id(album_id)
#download_photos_by_ids(photo_ids)
