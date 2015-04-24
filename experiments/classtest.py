#!/usr/bin/python

class test:
	def __init__(self, i):
		 self.i = i
	def add(self, x):
		self.i = self.i + x
	def getX(self):
		self.add(5)
		return self.i

if __name__ == "__main__":
	t = test(5)
	t.add(10)
	print t.getX()

