#!/usr/bin/env python
# -*- coding: utf-8 -*-


def encrypt(plaintext, key):
    ciphertext = ''
    for character in plaintext:
        if character.isalpha():
            number = ord(character)
            number += key
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
