#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module allows users to enter in the key to for the cipher encryption/decryption,
the action to encrypt/decrypt (encrypt is the default action), and the message to encrypt/decrypt.

``Examples:``
    $ python caesar_script.py --help
    $ python caesar_script.py --key 23 my secret message
    $ python caesar_script.py --key 23 --encrypt my secret message
    $ python caesar_script.py -k 23 -e my secret message
    $ python caesar_script.py -d -k 23 jv pbzobq jbppxdb

``Author:`` Kevin Ma

``Date:`` 2018-12-21

``Version:`` 2.0.0
"""
import click

from caesar_encryption import encrypt


@click.command()
@click.option(
    '--input_file', '-i',
    type=click.File('r'),
    help='File containing text you want to encrypt/decrypt. '
    'If not provided, a prompt will allow you to enter the input text.'
)
@click.option(
    '--output_file', '-o',
    type=click.File('w'),
    help='File where the encrypted/decrypted text will be written to. '
    'If not provided, the output will be printed to the stdout.'
)
@click.option('--key', '-k', default=1, help='The amount to shift by')
@click.option('--decrypt/--encrypt', '-d/-e', help='The action to invoke on the text')
def caesar(input_file, output_file, key, decrypt):
    """This function uses the click module to parse the
    arguments passed in from the command line and encrypts/decrypts
    the message using the `encrypt` function from the `caesar_encryption`
    module. Error and handling and usage (e.g. --help) is automatically
    generated for us.
    """
    if input_file:
        text = input_file.read()
    else:
        # if user wants to encrypt text, we don't want to have this show up in the command history
        text = click.prompt('Please enter a text', hide_input=not decrypt)

    if decrypt:
        key = -key

    ciphertext = encrypt(text, key)

    if output_file:
        output_file.write(ciphertext)
    else:
        click.echo(ciphertext)


if __name__ == "__main__":
    caesar()
