#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import requests
from fbi import getpassword

import s3
from collage import make_collage
from photos import *

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
    s3.upload_file(filename, bucket_name)
sys.stdout.write('\n')
sys.stdout.flush()

# Make photo collage
make_collage(filenames, 'insta.png', 600, 300)

# Send photo collage to grandma
path = '~/.key/insta.enc'
token = getpassword(path)
data = {'file':('insta.png', open('insta.png', 'rb'), 'png')}
params = {'initial_comment':'Hello, World!', 'title':'insta.png',
          'filename':'insta.png', 'token':token, 'channels':['#family']}
r = requests.post("https://slack.com/api/files.upload", params=params,
                  files=data)
