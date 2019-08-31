# -*- coding: utf-8 -*-

import argparse

import user_functions
import file_operations


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Command to download a file from a user's bucket",
                                     usage='get_file.py [-h] username password key local-file-path')

    parser.add_argument('username', help='Username for the user.')
    parser.add_argument('password', help='Password for the user.')
    parser.add_argument('files', help='Must wrap each in quotes for spaces.', nargs='+', metavar='key local-file-path')

    args = parser.parse_args()

    if len(args.files) > 2:
        print('Invalid command. Files with spaces must be wrapped in quotes. '
              'Usage: upload_file.py [-h] username password key local-path')
        exit(1)

    user_functions.check_info(args.username, args.password)
    print('Downloading files...')
    file_operations.download_file(args.username, args.files[0], args.files[1])
    print('Downloaded Files.')
