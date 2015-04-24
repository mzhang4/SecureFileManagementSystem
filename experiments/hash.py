#!/usr/bin/python

import hashlib

password = 'kitty'
hashValue = hashlib.sha256(password).digest()

print hashValue