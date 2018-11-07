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
    """Get list of Google Photos albums"""

    service = setup_api()
    result = service.albums().list(pageSize=10,
            fields="nextPageToken,albums(id,title)").execute()
    albums = result.get('albums', [])
    if not albums:
        print('No albums found.')
    else:
        print('Your Google Photos albums:')
        for album in albums:
            print("'{0}' album. Album id: {1}".format(album['title'],
                                                      album['id']))

# Example. Get list of Google Photos albums
#get_albums()
