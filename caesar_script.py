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

``Version:`` 1.2.0
"""
import click

from caesar_encryption import encrypt


@click.command()
# nargs denotes how many words expected for this argument
# -1 allows us to provide any number of words
@click.argument('text', nargs=-1)
@click.option('--key', '-k', default=1, help='The amount to shift by')
@click.option('--decrypt/--encrypt', '-d/-e', help='The action to invoke on the text')
def caesar(text, key, decrypt):
    """This function uses the click module to parse the
    arguments passed in from the command line and encrypts/decrypts
    the message using the `encrypt` function from the `caesar_encryption`
    module. Error and handling and usage (e.g. --help) is automatically
    generated for us.
    """
    text_string = ' '.join(text)
    if decrypt:
        key = -key
    ciphertext = encrypt(text_string, key)
    click.echo(ciphertext)


if __name__ == "__main__":
    caesar()
