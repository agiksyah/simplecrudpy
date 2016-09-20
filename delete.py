#!/usr/bin/python

import MySQLdb as db
import sys

kon = db.connect('localhost', 'root', '', 'crudpy');
cur = kon.cursor()
 
sql = "DELETE FROM `user` WHERE `id` = '%s'" % ("6")

try:
	cur.execute(sql)
	kon.commit()
	print "Delete Success"
	print cur._last_executed
except:
   kon.rollback()
   print "Delete Failed"
   print cur._last_executed
	   
       
if kon:    
	kon.close()