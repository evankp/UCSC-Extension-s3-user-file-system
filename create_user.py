# -*- coding: utf-8 -*-

import boto3
import argparse
import yaml
import os

import file_operations

s3 = boto3.client('s3', region_name='us-west-2')
""" :type: pyboto3.s3 """

PREFIX = 'ucsc-evankp-v2'


def init_buckets(user):
    all_buckets = s3.list_buckets()['Buckets']
    required_buckets = [f'{PREFIX}-users', f'{PREFIX}-{user}']

    # Get list of buckets for this assignment
    project_buckets = [bucket['Name'] for bucket in all_buckets if bucket['Name'].startswith(PREFIX)]

    # Checks if all the required buckets exist and if not, creates them and adds to function list output
    for bucket in required_buckets:
        if bucket not in project_buckets:
            s3.create_bucket(Bucket=bucket,
                             ACL='private',
                             CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})

            project_buckets.append(bucket)

    # Create an empty user.yaml file in users bucket if not in there.
    if 'Contents' not in s3.list_objects_v2(Bucket=f'{PREFIX}-users', Prefix='users.yaml'):
        f = open('users.yaml', 'w')
        f.close()

        file_operations.upload_file('users', 'users.yaml')
        os.remove('users.yaml')

    return project_buckets


def create_user(username, password, email):
    file_operations.download_file('users', 'users.yaml')
    users = file_operations.read_config()

    users[username] = {
        'password': password,
        'email': email
    }

    with open('users.yaml', 'w') as stream:
        yaml.dump(users, stream, default_flow_style=False)

    file_operations.upload_file('users', 'users.yaml')
    os.remove('users.yaml')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Command line to create user in a AWS bucket system.')

    parser.add_argument('username', help='Username for the new user')
    parser.add_argument('password', help='Password for new user')
    parser.add_argument('email', help='Email for the new user')

    args = parser.parse_args()

    print('Creating user...')
    init_buckets(args.username)
    create_user(args.username, args.password, args.email)
    print('Created User')
