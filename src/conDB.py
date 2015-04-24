#!/usr/bin/python

import MySQLdb as mdb

class conDB:
	def __init__(self):
		self.host = 'localhost'
		self.user = 'CS8120'
		self.pw = '8224074zms'
		self.db = 'CS8120'

	def conDB(self):
		con = mdb.connect(self.host, self.user, self.pw, self.db)
		return con