# -*- coding: utf-8 -*-

import boto3
import argparse
from pprint import pprint

s3 = boto3.client('s3', region_name='us-west-2')
""" :type: pyboto3.s3 """

PREFIX = 'ucsc-evankp'


def init_buckets(user='evankp'):
    all_buckets = s3.list_buckets()['Buckets']
    required_buckets = [f'{PREFIX}-users', f'{PREFIX}-{user}']

    project_buckets = [bucket['Name'] for bucket in all_buckets if bucket['Name'].startswith(PREFIX)]

    for bucket in required_buckets:
        if bucket not in project_buckets:
            s3.create_bucket(Bucket=bucket,
                             ACL='private',
                             CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})

            project_buckets.append(bucket)

    return project_buckets


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='Command line to create user in a AWS bucket system -- requires aws cli, boto3, and python 3')
    #
    # parser.add_argument('username', help='Username for the new user')
    # parser.add_argument('password', help='Password for new user')
    # parser.add_argument('email', help='Email for the new user')
    #
    # args = parser.parse_args()

    pprint(init_buckets())
