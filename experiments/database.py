#!/usr/bin/python

import MySQLdb as mdb

con = mdb.connect('localhost', 'CS8120', '8224074zms', 'CS8120')

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM USER")

    rows = cur.fetchall()

    for row in rows:
        print row[1]