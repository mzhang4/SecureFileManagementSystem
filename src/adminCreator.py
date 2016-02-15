#!/usr/bin/python

from keyGenerator import keyGenerator
from conDB import conDB

import sys
import MySQLdb as mdb
import random
import hashlib

if __name__ == "__main__":
	con = mdb.connect('localhost', 'CS8120', '8224074zms', 'CS8120')

	user = raw_input("ADMIN NAME: ")
	password = raw_input("PASSWORD: ")
	spw = raw_input("PASSWORD SECOND TIME: ")

	if password != spw:
		print "WRONG PASSWORD"
	else:
		con = conDB().conDB()
		with con:
			cur = con.cursor()

			insert_user = ("INSERT INTO `USER` (`NAME`, `SALT`, `PASSWORD`, `PRIVILEGE`, `KEY`, `IV`) VALUES (%s, %s, %s, %s, %s, %s);")
			salt = int(random.uniform(1000, 9999))
			kg = keyGenerator()
			kg.gen()
			key = kg.getKey()
			iv = kg.getIV()

			insert_data = (user, salt,  hashlib.sha224(password+str(salt)).digest(), 1, key, IV)
			cur.execute(insert_user, insert_data)

		print "CREATE SUCCESS"