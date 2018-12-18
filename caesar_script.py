#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module allows users to enter in the key to for the cipher encryption/decryption, the action to encrypt/decrypt (encrypt is the default action), and the message to encrypt/decrypt.

``Examples:``
    $ python caesar_script.py --key 23 my secret message
    $ python caesar_script.py --key 23 --encrypt my secret message
    $ python caesar_script.py -k 23 -e my secret message
    $ python caesar_script.py -d -k 23 jv pbzobq jbppxdb

``Author:`` Kevin Ma

``Date:`` 2018-12-18

``Version:`` 1.0.0
"""
import sys

from caesar_encryption import encrypt


def caesar():
    key = 1
    is_decrypt = False
    is_error = False

    for idx, arg in enumerate(sys.argv):
        if arg in ['--key', '-k'] and len(sys.argv) > idx+1:
            key = int(sys.argv[idx+1])
            del sys.argv[idx]  # the --key or k
            del sys.argv[idx]  # the actual key arg
            break

    # cannot ensure order of args, so we look for key first and after consuming the args
    # we loop through args again to identify the encrpyt/decrypt flag
    for idx, arg in enumerate(sys.argv):
        if arg in ['--encrypt', '-e']:
            del sys.argv[idx]
            break

        elif arg in ['--decrypt', '-d']:
            is_decrypt = True
            del sys.argv[idx]
            break

    # to decrypt caesarian cipher, simply use the opposite of the key
    if is_decrypt:
        key = -key

    if len(sys.argv) == 1:
        # this would mean we simply have ['caesar_scripy.py'] in argsv, there is no msg to encrypt or decrypt!
        is_error = True
    else:
        for arg in sys.argv:
            if arg.startswith('-'):
                # we have already consumed all expected flags, the only remaining arg
                # should be the msg to encrypt/decrypt!
                is_error = True

    if is_error:
        print(
            'Usage: python {} [ --key|k <key> ] [ --encrypt|decrypt|e|d ] <text>'.format(sys.argv[0]))
    else:
        print(encrypt(' '.join(sys.argv[1:]), key))


if __name__ == "__main__":
    caesar()
