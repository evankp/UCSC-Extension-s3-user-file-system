# -*- coding: utf-8 -*-

import boto3
import sys

PREFIX = 'ucsc-evankp-v2'
s3 = boto3.client('s3')
""" :type: pyboto3.s3 """


def delete_objects(bucket):
    get_objects = s3.list_objects_v2(Bucket=bucket)

    if 'Contents' in get_objects:
        keys_to_delete = [{'Key': aws_object['Key']} for aws_object in get_objects['Contents']]

        s3.delete_objects(Bucket=bucket, Delete={'Objects': keys_to_delete})


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Please provide bucket name')
        exit(1)

    if len(sys.argv) > 2:
        for bucket in sys.argv[1:]:
            delete_objects(f'{PREFIX}-{bucket}')
            s3.delete_bucket(Bucket=f'{PREFIX}-{bucket}')

        print('Deleted Buckets')
        exit(0)

    delete_objects(f'{PREFIX}-{sys.argv[1]}')

    s3.delete_bucket(Bucket=f'{PREFIX}-{sys.argv[1]}')
    print('Deleted Bucket')
