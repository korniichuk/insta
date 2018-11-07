#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from os.path import basename, exists, isfile

import boto3

def upload_file(file_abs_path, bucket_name, key_name=None):
    """Upload file to Amazon S3 bucket. If no `key_name`, file name used as
       `key_name` (example: `file_abs_path` is '/tmp/example.mp3' and `key_name`
       is None, that `key_name` is 'example.mp3').
    Input:
        file_abs_path -- file abs path (required | type: str);
        bucket_name -- Amazon S3 bucket name (required | type: str);
        key_name -- Amazon S3 bucket dst file abs path (not required |
                    type: str).
    """

    if not key_name:
        key_name = basename(file_abs_path)
    # Let's use Amazon S3
    s3 = boto3.client('s3')
    if exists(file_abs_path) and isfile(file_abs_path):
        # Upload file to Amazon S3 bucket
        try:
            s3.upload_file(file_abs_path, bucket_name, key_name)
        except Exception as exception:
            return 1
    else:
        return 1

# Example. Upload '/tmp/example.mp3' file to Amazon S3 'examplebucket' bucket as
# 'example.mp3' file
#upload_file('/tmp/example.mp3', 'examplebucket')

# Example. Upload '/tmp/example.mp3' file to Amazon S3 'examplebucket' bucket as
# 'new.mp3' file
#upload_file('/tmp/example.mp3', 'examplebucket', 'new.mp3')
