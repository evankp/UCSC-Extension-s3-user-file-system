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
        description="Uploads file to user's bucket, user has to have been created with create_user.py",
        usage='upload_file.py [-h] username password key local-file-path'
    )
    parser.add_argument('username', help='Username of the user')
    parser.add_argument('password', help='Password of the user')
    parser.add_argument('files', help='Must wrap each in quotes for spaces.', nargs='+', metavar='key local-file-path')
    # parser.add_argument('local_file', help='Local path of the file on system. Must wrap in quotes for spaces.')

    args = parser.parse_args()

    if len(args.files) > 2:
        print('Invalid command. Files with spaces must be wrapped in quotes. '
              'Usage: upload_file.py [-h] username password key local-path')
        exit(1)

    user_functions.check_info(args.username, args.password)
    print('Uploading file...')
    file_operations.upload_file(args.username, args.files[1], args.files[0])
    print('File Upload')
