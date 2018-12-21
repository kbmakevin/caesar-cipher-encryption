#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module allows users to enter in the key to for the cipher encryption/decryption,
the action to encrypt/decrypt (encrypt is the default action), and the message to encrypt/decrypt.

``Examples:``
    $ python caesar_script.py --key 23 my secret message
    $ python caesar_script.py --key 23 --encrypt my secret message
    $ python caesar_script.py -k 23 -e my secret message
    $ python caesar_script.py -d -k 23 jv pbzobq jbppxdb

``Author:`` Kevin Ma

``Date:`` 2018-12-21

``Version:`` 1.1.0
"""
import argparse

from caesar_encryption import encrypt


def caesar():
    """This function uses the argparse module to parse the
    arguments passed in from the command line and encrypts/decrypts
    the message using the `encrypt` function from the `caesar_encryption`
    module. Error and handling and usage (e.g. --help|-h) is automatically
    generated for us since we are using the python std lib argparse.
    """
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-e', '--encrypt', action='store_true')
    group.add_argument('-d', '--decrypt', action='store_true')

    parser.add_argument('text', nargs='*')
    parser.add_argument('-k', '--key', type=int, default=1)

    args = parser.parse_args()

    text_string = ' '.join(args.text)
    key = args.key

    if args.decrypt:
        key = -key

    ciphertext = encrypt(text_string, key)
    print(ciphertext)


if __name__ == "__main__":
    caesar()
