#!/usr/bin/python

import MySQLdb as db
import sys

kon = db.connect('localhost', 'root', '', 'crudpy');
cur = kon.cursor()
 
sql = "UPDATE user SET name = '%s' WHERE `id` = '%s'" % ('iko karambit', '2')

try:
	cur.execute(sql)
	kon.commit()
	print "Update Success"
	print cur._last_executed
except:
   kon.rollback()
   print "Update Failed"
   print cur._last_executed
	   
       
if kon:    
	kon.close()
