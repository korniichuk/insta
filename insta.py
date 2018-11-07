#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from photos import *
from s3 import upload_file

# Get list of all Google Photos albums
get_albums()
album_id = "AIcl5Br1e9_2x1l7NIOFVC2QrOqhCeEULW9OK9" \
           "fWCm9MsvzJDeZcszmFhntItkoFb3Y3bldiqnQy"

# Get list all of the photos in Google Photos album
ptoto_ids = get_photos_by_album_id(album_id)

# Download photos from Google Photos by ids
filenames = download_photos_by_ids(ptoto_ids)

# Upload all photos to Amazon S3 bucket
bucket_name = 'photos.insta'
length = len(filenames)
for i, filename in enumerate(filenames):
    sys.stdout.write('\r')
    sys.stdout.write('uploading: %s/%s' % (i+1, length))
    sys.stdout.flush()
    upload_file(filename, bucket_name)
sys.stdout.write('\n')
sys.stdout.flush()
