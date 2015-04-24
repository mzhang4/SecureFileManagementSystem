#!/usr/bin/python

from Crypto.Cipher import AES

key = '0123456789abcdef'
IV = 16 * '\x00'           # Initialization vector: discussed later
mode = AES.MODE_CBC
encryptor = AES.new(key, mode, IV=IV)

text = "abcd"*4 + "abcde" # Total 21 length long
if len(text) % 16 != 0:
	text += ' ' * (16 - len(text) % 16)

print "Start encrypting...\n"
ciphertext = encryptor.encrypt(text)

print "Ciphertext...\n"
print "Ciphertext:  "+ ciphertext + '\n'

print "Start decrypting...\n"
decryptor = AES.new(key, mode, IV=IV)
plain = decryptor.decrypt(ciphertext)

print "Plaintext...\n"
print "Plaintext:  " + plain + '\n'