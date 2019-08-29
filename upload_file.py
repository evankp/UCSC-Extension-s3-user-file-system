# -*- coding: utf-8 -*-

import argparse
import boto3
import file_operations
import user_functions
import os

s3 = boto3.client('s3', region_name='us-west-2')
""" :type: pyboto3.s3 """


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Uploads file to user's bucket, user has to have been created with create_user.py")
    parser.add_argument('username', help='Username of the user')
    parser.add_argument('password', help='Password of the user')
    parser.add_argument('file_key', help='Key of the file in the bucket. Must wrap in quotes for spaces.')
    parser.add_argument('local_file', help='Local path of the file on system. Must wrap in quotes for spaces.')

    args = parser.parse_args()

    user_functions.check_info(args.username, args.password)
    print('Uploading file...')
    file_operations.upload_file(args.username, args.local_file, args.file_key)
    print('File Upload')
