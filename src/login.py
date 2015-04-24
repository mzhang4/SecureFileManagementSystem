#!/usr/bin/python

import hashlib
import sys
import MySQLdb as mdb
import os.path
import subprocess
import commands

class login:
	def __init__(self, con):
		self.id = 0
		self.user = raw_input("USER NAME: ")
		self.password = raw_input("PASSWORD: ")
		self.key = ""
		self.p = 0
		self.IV = ""
		self.con = con

	def login(self):
		cur = self.con.cursor()

		select_user = ("SELECT * FROM `USER` WHERE `NAME` = %s")
		data_user = [self.user]
		cur.execute(select_user, data_user)
		rows = cur.fetchall()
		
		check = commands.getoutput("[ -f /Volumes/important\ files/keys/%s.key ] && echo \"Y\" || echo \"N\""%self.user)

		if len(rows)<1:
			print "Wrong USER NAME"
			return 0
		elif rows[0][3]==hashlib.sha224(self.password+str(rows[0][2])).digest():
			if check == "Y":
				self.key = commands.getoutput("cat /Volumes/important\ files/keys/%s.key"%self.user)
			else:
				print "NEED TO PLUGIN YOUR KEY"
				return 0
			self.id = rows[0][0]
			self.p = rows[0][4]
			if self.key == rows[0][5]:
				self.IV = rows[0][6]
				self.loginSuccess()
				return 1
			else:
				print "WRONG KEY"
		else:
			print "Wrong PASSWORD"
			return 0

	def loginSuccess(self):
		print "1. SFM-List"
		print "2. SFM-Display"
		print "3. SFM-Add"
		print "4. SFM-Del"
		print "5. SFM-Check"

		i = 6
		if self.p == 1 :
			print str(i) + ". CREATE USER"
			i = i + 1

		print str(i) + ". EXIT"

		print "0. INQUIRY"

	def getID(self):
		return self.id

	def getUser(self):
		return self.user

	def getPW(self):
		return self.password

	def getKey(self):
		return self.key

	def getP(self):
		return self.p

	def getIV(self):
		return self.IV