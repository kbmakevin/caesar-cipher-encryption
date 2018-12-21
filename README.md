# caesar-cipher-encryption

## install required packages
`$ pip install -r ./requirements.txt`

## run the encryption/decryption script
    $ python caesar_script.py --help
    $ python caesar_script.py --key 23 my secret message
    $ python caesar_script.py --key 23 --encrypt my secret message
    $ python caesar_script.py -k 23 -e my secret message
    $ python caesar_script.py -d -k 23 jv pbzobq jbppxdb

## run the caesar cipher cracking script
    $ python crack_caesar_cipher.py --help
    $ python crack_caesar_cipher.py -i ./encrypted_text -o ./decrypted_text
