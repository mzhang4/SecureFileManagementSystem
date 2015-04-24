#!/usr/bin/python

import sys

print "Please enter the text..."

text = ""
for line in sys.stdin:
  text = text + line

fileName = raw_input("Please enter the file name...\n")
f = open(fileName, 'w')
f.write(text)