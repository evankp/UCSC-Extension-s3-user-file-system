# -*- coding: utf-8 -*-

import boto3
import argparse

import user_functions

s3 = boto3.client('s3', region_name='us-west-2')
""" :type: pyboto3.s3 """

PREFIX = 'ucsc-evankp'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Deletes a file from the user's bucket")

    parser.add_argument('username', help='Username for the user.')
    parser.add_argument('password', help='Password for the user.')
    parser.add_argument('keys', nargs=argparse.REMAINDER, help='Key(s) of the file to delete, can be multiple files'
                                                               ' separated by a space')

    args = parser.parse_args()

    user_functions.check_info(args.username, args.password)

    objects_to_delete = [{'Key': file} for file in args.keys]
    response = s3.delete_objects(Bucket=f'{PREFIX}-{args.username}', Delete={'Objects': objects_to_delete})

    for item in response['Deleted']:
        print(f"Deleted {item['Key']}")
