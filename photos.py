#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

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

def get_albums():
    """Get list of all Google Photos albums (first 50)"""

    service = setup_api()
    result = service.albums().list(pageSize=50).execute()
    albums = result.get('albums', [])
    if not albums:
        print('No albums found.')
    else:
        print('Your Google Photos albums:')
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
        print('Your Google Photos media items:')
        for item in items:
            print("'{0}' media item. Media item id: {1}".format(
                    item['filename'], item['id']))

# Example. Get list of all Google Photos albums (first 50)
#get_albums()

# Example. Get list of all Google Photos media items (first 100)
#get_media_items()
