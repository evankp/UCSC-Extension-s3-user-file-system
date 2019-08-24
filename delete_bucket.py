# -*- coding: utf-8 -*-

import boto3
import sys

PREFIX = 'ucsc-evankp'
s3 = boto3.client('s3')
""" :type: pyboto3.s3 """

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Please provide bucket name')
        exit(1)

    if len(sys.argv) > 2:
        for bucket in sys.argv[1:]:
            s3.delete_bucket(Bucket=f'{PREFIX}-{bucket}')

        exit(0)

    s3.delete_bucket(Bucket=f'{PREFIX}-{sys.argv[1]}')
