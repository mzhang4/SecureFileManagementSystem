#!/usr/bin/python

import sys
import getch

sys.stdin = open('/dev/tty', 'r')
if __name__ == "__main__":
	print "first time"
	text = ""
	for line in sys.stdin:
		text = text + line
	print text

	print "second time"
	text = ""
	for line in sys.stdin:
		text = text + line
	print text

	print "third time" + getch.getch()

	for line in sys.stdin:
		text = text + line
	print text
