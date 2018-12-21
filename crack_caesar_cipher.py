#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module allows the user to crack cipher encryption without knowing the encryption key.
There are only 25 possible results we need to consider because if we shift characters any more than 26 would
simply be reiterating cases we have already considered. Technically, there are 26 caesar ciphers, but the cipher key
of 0 is useless and can be simply disregarded. To make sense of the resulting ciphers, we will use a dictionary (enchant)
to assist us.

``Examples:``
    $ python crack_caesar_cipher.py --help
    $ python crack_caesar_cipher.py -i ./encrypted_text -o ./decrypted_text

``Author:`` Kevin Ma

``Date:``   2018-12-21

``Version:`` 1.0.0
"""
import enchant
import click

from caesar_encryption import encrypt


@click.command()
@click.option(
    '--input_file', '-i',
    type=click.File('r'),
    required=True
)
@click.option(
    '--output_file', '-o',
    type=click.File('w'),
    required=True
)
def crack_caesar(input_file, output_file):
    """This function reads encrypted text from an input file and iterates over the 25 possible
    caesar ciphers to determine the most likely decrypted plaintext message and caesar cipher
    key used to encrypt the text. For each caesar cipher, the number of valid english words are
    determined by checking against a dictionary provided by the `pyenchant` module. The most
    likely plaintext and key are determined by the caesar cipher containing the highest number of
    valid english words.
    """
    ciphertext = input_file.read()
    en_dict = enchant.Dict('en_US')
    max_num_valid_words = 0
    for key in range(1, 26):
        plaintext = encrypt(ciphertext, -key)
        num_valid_words = 0
        for word in plaintext.split(' '):
            if en_dict.check(word):
                num_valid_words += 1
        if num_valid_words > max_num_valid_words:
            max_num_valid_words = num_valid_words
            best_plaintext = plaintext
            best_key = key
    click.echo(f'The most likely encryption key is {best_key}')
    output_file.write(best_plaintext)


if __name__ == "__main__":
    crack_caesar()
