import boto3
import yaml

s3res = boto3.resource('s3', region_name='us-west-2')
PREFIX = 'ucsc-evankp'


def download_file(bucket, key, location=None):
    if not location:
        location = key

    s3res.Bucket(f'{PREFIX}-{bucket}').download_file(key, location)


def upload_file(bucket, local_file, key=None):
    if key is None:
        key = local_file

    try:
        s3res.Bucket(f'{PREFIX}-{bucket}').upload_file(local_file, key)
    except FileNotFoundError:
        print('File not found on system.')
        exit(1)


def read_config():
    with open('users.yaml', 'r') as stream:
        try:
            data = yaml.safe_load(stream)

            if data is None:
                data = {}

            return data
        except yaml.YAMLError as err:
            print(err)