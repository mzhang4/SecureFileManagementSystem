#!/usr/bin/python

import sys
import login
import random
import hashlib
from keyGenerator import keyGenerator
from Crypto.Cipher import AES
import commands

class SFM:
	def __init__(self, id, p, key, con, IV):
		self.id = id
		self.p = p
		self.key = key
		self.con = con
		self.IV = IV

	def operate(self):
		if self.p==1:
			operation = raw_input("Enter(0-7): ")
		else:
			operation = raw_input("Enter(0-6): ")

		r = 1

		if operation=='0':
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
			r = self.operate()
		elif operation=='1':
			self.SFMList()
		elif operation=='2':
			self.SFMDisplay()
		elif operation=='3':
			self.SFMADD()
		elif operation=='4':
			self.SFMDEL()
		elif operation=='5':
			self.SFMCheck()
		elif operation=='6' and self.p==1:
			self.AddUser()
		elif operation=='6' and self.p==0:
			r = 0
		elif operation=='7' and self.p==1:
			r = 0
		else:
			print "WRONG OPERATION"

		return r

	def SFMList(self):
		cur = self.con.cursor()
		if self.p==0:
			select_file = ("SELECT * FROM `FILE` WHERE `USER_ID` = %s")
			data_file = [self.id]
			cur.execute(select_file, data_file)
		else:
			select_file = ("SELECT * FROM `FILE`")
			cur.execute(select_file)

		rows = cur.fetchall()
		if len(rows)==0:
			if self.p==0:
				print "NO FILE OWNED BY YOU"
			else:
				print "NO FILE IN THE SYSTEM"
		elif self.p==0:
			i = 1
			for r in rows:
				print str(i) + ". " + r[2]
				i = i + 1
		else:
			i = 1
			for r in rows:
				print '%s. %6s %5s'%(str(i), r[2], r[1])
				i = i + 1

	def SFMDisplay(self):
		cur = self.con.cursor()
		fileName = raw_input("FILE NAME: ")
		if self.p==1:
			id = raw_input("USER ID: ")
			# TO DO needs to query the DATABASE
			select_user = ("SELECT * FROM `USER` WHERE `ID` = %s")
			data_user = [id]
			cur.execute(select_user, data_user)
			rows = cur.fetchall()

			if len(rows)==0:
				print "USER NOT EXIST"
				return
			else:
				key = rows[0][5]
				IV = rows[0][6]
		else:
			id = self.id
			key = self.key
			IV = self.IV

		select_file = ("SELECT * FROM `FILE` WHERE `USER_ID` = %s and NAME = %s")
		data_file = (id, fileName)
		cur.execute(select_file, data_file)
		rows = cur.fetchall()

		if len(rows)==0:
			print "NOT EXIST"
		else:
			mode = AES.MODE_CBC
			print "Key is: " + str(key)
			decryptor = AES.new(key, mode, IV=IV)
			plain = decryptor.decrypt(rows[0][3])
			print "CONTENT:"
			print plain

	def SFMADD(self):
		mode = AES.MODE_CBC
		encryptor = AES.new(self.key, mode, IV=self.IV)

		fileName = raw_input("FILE NAME: ")
			
		cur = self.con.cursor()
		select_file = ("SELECT * FROM `FILE` WHERE USER_ID = %s and NAME = %s")
		data_file = (self.id, fileName)
		cur.execute(select_file, data_file)
		rows = cur.fetchall()

		if len(rows)>0:
			print "ALREADY EXIST"
			return

		print "ENTER TEXT AND END BY TYPING QUIT"

		text = ""
		run = True
		while run:
			line = sys.stdin.readline().rstrip('\n')
			if line == 'quit':
					run = False
			else:
				text = text + line + '\n'

		if len(text) % 16 != 0:
			text += ' ' * (16 - len(text) % 16)

		add_file = ("INSERT INTO `FILE` (`USER_ID`, `NAME`, `CONTENT`) VALUES (%s, %s, %s);")
		data_file = (self.id, fileName, encryptor.encrypt(text))
		cur.execute(add_file, data_file)
		self.con.commit()

		print "ADD SUCCESS"

	def SFMDEL(self):
		fileName = raw_input("FILE NAME: ")
		if self.p==1:
			id = raw_input("USER ID: ")

		cur = self.con.cursor()
		delete_file = ("DELETE FROM `FILE` WHERE `USER_ID` = %s and `NAME` = %s")
		data_file = (id, fileName)
		rows = cur.execute(delete_file, data_file)
		self.con.commit()

		if rows==0:
			print "NO FILE Name " + fileName + "\n"
		else:
			print "DELETE SUCCESS"

	def SFMCheck(self):
		mode = AES.MODE_CBC
		encryptor = AES.new(self.key, mode, IV=self.IV)

		fileName = raw_input("FILE NAME: ")
		print "ENTER TEXT AND END BY TYPING QUIT"

		text = ""
		run = True
		while run:
			line = sys.stdin.readline().rstrip('\n')
			if line == 'quit':
				run = False
			else:
				text = text + line + '\n'

		if len(text) % 16 != 0:
			text += ' ' * (16 - len(text) % 16)

		cur = self.con.cursor()
		if self.p==0:
			select_file = ("SELECT * FROM `FILE` WHERE `USER_ID` = %s and `NAME` = %s and `CONTENT` = %s")
			data_file = (self.id, fileName, encryptor.encrypt(text))	
		else:
			select_file = ("SELECT * FROM `FILE` WHERE `NAME` =  %s and `CONTENT` = %s")
			data_file = (fileName, encryptor.encrypt(text))

		rows = cur.execute(select_file, data_file)

		if rows==0:
			print "NO FILE WITH INPUT NAME AND CONTENT"
		else:
			print "THE FILE IS IN THE SYSTEM"

	def AddUser(self):
		user = raw_input("USER NAME: ")
		password = raw_input("PASSWORD: ")
		spw = raw_input("PASSWORD SECOND TIME: ")

		if password != spw:
			print "WRONG PASSWORD"
			return
		
		cur = self.con.cursor()
		select_user = ("SELECT * FROM `USER` WHERE `NAME` = %s")
		data_user = [user]
		rows = cur.execute(select_user, data_user)

		if rows!=0:
			print "ALREADY EXIST"
			return

		check = commands.getoutput("[ -d /Volumes/important\ files/keys ] && echo \"Y\" || echo \"N\"")
		if check=="N":
			print "PLUG IN YOU KEY DEVICE"
			return

		insert_user = ("INSERT INTO `USER` (`NAME`, `SALT`, `PASSWORD`, `KEY`, `IV`) VALUES (%s, %s, %s, %s, %s);")
		salt = int(random.uniform(1000, 9999))
		kg = keyGenerator()
		kg.gen()
		key = kg.getKey()
		IV = kg.getIV()
		commands.getoutput("echo \"%s\">/Volumes/important\ files/keys/%s.key"%(key,user))
		insert_data = (user, salt,  hashlib.sha224(password+str(salt)).digest(), key, IV)
		cur.execute(insert_user, insert_data)
		self.con.commit()

		print "CREATE SUCCESS"
