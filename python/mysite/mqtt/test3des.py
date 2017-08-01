#!/usr/bin/env python
# -*- coding: utf-8 -*-

from M2Crypto.EVP import Cipher

def encrypt_3des(key, text):
    encryptor = Cipher(alg='des_ede3_ecb', key=key, op=1, iv='\0'*16)
    s = encryptor.update(text)
    return s+ encryptor.final()

def decrypt_3des(key, text):
    decryptor = Cipher(alg='des_ede3_ecb', key=key, op=0, iv='\0'*16)
    s= decryptor.update(text)
    return s + decryptor.final()


if __name__ == "__main__":
    key = '12345678abcdefgh12345678'
    text = 'value'
    encrypt_text = encrypt_3des(key, text)
    assert decrypt_3des(key, encrypt_text) == text
