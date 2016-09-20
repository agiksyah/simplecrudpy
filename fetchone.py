#!/usr/bin/python

import MySQLdb as db
import sys

kon = db.connect('localhost', 'root', '', 'crudpy');
cur = kon.cursor()
try:
	sql = "SELECT * from `user` WHERE `id` = '%s'" % ('1')
	cur.execute(sql)
	user = cur.fetchone()
	print "Name : %s" %user[1]
except:
print "Select Failed"
        
if kon:    
kon.close()
