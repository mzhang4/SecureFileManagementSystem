#!/usr/bin/python

import string
import random

class keyGenerator:
	def __init__(self):
		self.key = ''
		self.IV = ''
	
	def gen(self):
		allowed_chars = ''.join((string.lowercase, string.uppercase, string.digits))
		self.key = ''.join(random.choice(allowed_chars) for _ in range(16))
		self.IV = 16 * '\x00'

	def getKey(self):
		return self.key

	def getIV(self):
		return self.IV
