#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides functionality to encrypt or decrypt a plaintext using the
    Caesarian Cipher.

``Author:`` Kevin Ma

``Date:`` 2018-12-18

``Version:`` 1.0.0
"""


def encrypt(plaintext, key):
    """This function encrypts/decrypts the plaintext using the key provided to ciphertext
    using the Caesarian Cipher method. To decrypt text, simply provide the opposite key
    used to encrypt the text (e.g. provide -key if key was used to encrypt the plaintext).

    ``Args:``
        plaintext (str): The text to be encrypted.
        key (int): The number of characters to shift the characters in the plaintext.

    ``Returns:``
        str: The encrypted/decrypted text (depending on the key passed in as an arg).
    """
    ciphertext = ''
    for character in plaintext:
        if character.isalpha():
            number = ord(character)
            number += key
            if character.isupper():
                if number > ord('Z'):
                    number -= 26
                elif number < ord('A'):
                    number += 26
            elif character.islower():
                if number > ord('z'):
                    number -= 26
                elif number < ord('a'):
                    number += 26
            character = chr(number)
        ciphertext += character

    return ciphertext
