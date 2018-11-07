#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from photos import *

# Get list of all Google Photos albums
get_albums()
album_id = "AIcl5Br1e9_2x1l7NIOFVC2QrOqhCeEULW9OK9" \
           "fWCm9MsvzJDeZcszmFhntItkoFb3Y3bldiqnQy"

# Get list all of the photos in Google Photos album
ptoto_ids = get_photos_by_album_id(album_id)

# Download photos from Google Photos by ids
download_photos_by_ids(ptoto_ids)
