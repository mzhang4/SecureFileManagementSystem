import sys
import os.path

if __name__ == "__main__":
	filename = "../../Volumes/important\ files/keys/admin.key"
	if os.path.isfile(filename):
		print "FILE NOT EXIST"
	else:
		print "FILE THERE"
