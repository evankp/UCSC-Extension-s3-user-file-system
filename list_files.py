# -*- coding: utf-8 -*-

import boto3
import argparse
import user_functions

PREFIX = 'ucsc-evankp'

s3 = boto3.client('s3', region_name='us-west-2')
""" :type: pyboto3.s3 """


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="List a user's files.")

    parser.add_argument('username', help='Username of the user.')
    parser.add_argument('password', help='Password to authenticate user before listing.')

    args = parser.parse_args()

    user_functions.check_info(args.username, args.password)

    list_objects = s3.list_objects_v2(Bucket=f'{PREFIX}-{args.username}')

    if 'Contents' not in list_objects:
        print('No files')
        exit(0)

    files = [file['Key'] for file in list_objects['Contents']]

    for file in files:
        print(file)
