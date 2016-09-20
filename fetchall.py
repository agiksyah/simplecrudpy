#!/usr/bin/python

import MySQLdb as db
import sys

kon = db.connect('localhost', 'root', '', 'crudpy');
cur = kon.cursor()

try:
	sql = "SELECT * FROM `user`"
	cur.execute(sql)
	user = cur.fetchall()

	for val in user:
		print "Name : %s" %val[1]
		
except:
	print "Select Failed"
	
if kon:    
	kon.close()