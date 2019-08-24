import boto3

s3res = boto3.resource('s3', region_name='us-west-2')


def download_file(bucket, key, location=None):
    if not location:
        location = key

    s3res.Bucket(bucket).download_file(key, location)
