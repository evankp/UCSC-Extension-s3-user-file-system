# -*- coding: utf-8 -*-

import argparse
import boto3
import file_operations
import os

s3 = boto3.client('s3', region_name='us-west-2')
""" :type: pyboto3.s3 """

PREFIX = 'ucsc-evankp'


def check_user_info(user, password):
    buckets = [bucket['Name'].replace(f'{PREFIX}-', '') for bucket in s3.list_buckets()['Buckets'] if bucket['Name'].startswith(PREFIX)]

    if not all(bucket in buckets for bucket in ['users', user]):
        print('Please execute create_user.py first')
        exit(1)

    file_operations.download_file('users', 'users.yaml')
    users = file_operations.read_config()

    if password != users[user]['password']:
        print('Password does not match')
        os.remove('users.yaml')
        exit(1)

    os.remove('users.yaml')
    return True


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description="Uploads file to user's bucket, user has to have been created with create_user.py")
    # parser.add_argument('username', help='Username of the user')
    # parser.add_argument('password', help='Password of the user')
    # parser.add_argument('file_key', help='Key of the file in the bucket. Must wrap in quotes for spaces. ')
    # parser.add_argument('local_file', help='Local path of the file on system. Must wrap in quotes for spaces.')
    #
    # args = parser.parse_args()

    check_user_info('kemp', 'pass124')
