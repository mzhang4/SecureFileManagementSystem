#!/usr/bin/python

from login import login
from conDB import conDB
from operations import SFM

if __name__ == "__main__":
	con = conDB().conDB()
	lg = login(con)
	s = lg.login()

	if s==1:
		id = lg.getID()
		key = lg.getKey()
		p = lg.getP()
		IV = lg.getIV()

		sfm = SFM(id, p, key, con, IV)

		while sfm.operate() == 1:
			pass