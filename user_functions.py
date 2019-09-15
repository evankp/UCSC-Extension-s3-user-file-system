# -*- coding: utf-8 -*-

import boto3
import file_operations
import os

PREFIX = 'ucsc-evankp-v2'
s3 = boto3.client('s3', region_name='us-west-2')
""" :type: pyboto3.s3 """


def check_info(username, password):
    buckets = [bucket['Name'].replace(f'{PREFIX}-', '') for bucket in s3.list_buckets()['Buckets'] if
               bucket['Name'].startswith(PREFIX)]

    if not all(bucket in buckets for bucket in ['users', username]):
        print('Please execute create_user.py first, as either user does not exist or bucket system is not setup.')
        exit(1)

    file_operations.download_file('users', 'users.yaml')
    users = file_operations.read_config()

    if password != users[username]['password']:
        print('Password does not match')
        os.remove('users.yaml')
        exit(1)

    os.remove('users.yaml')
    return True
