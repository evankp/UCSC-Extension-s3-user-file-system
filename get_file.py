import argparse

import user_functions
import file_operations


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Command to download a file from a user's bucket")

    parser.add_argument('username', help='Username for the user.')
    parser.add_argument('password', help='Password for the user.')
    parser.add_argument('key', help='Key of the file on the s3 bucket.')
    parser.add_argument('local_path', help='Location to save the file to.')

    args = parser.parse_args()

    user_functions.check_info(args.username, args.password)
    print('Downloading files...')
    file_operations.download_file(args.username, args.key, args.local_path)
    print('Downloaded Files.')
