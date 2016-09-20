#!/usr/bin/python

import MySQLdb as db
import sys

kon = db.connect('localhost', 'root', '', 'crudpy');
cur = kon.cursor()
 
sql = "INSERT INTO `user` (`id`,`name`) VALUE ('%s', '%s')" % (0, "nocturnal")

try:
	cur.execute(sql)
	kon.commit()
	print "Input success"
	print cur._last_executed
except:
   kon.rollback()
   print "Input Failed"
   print cur._last_executed
	   
       
if kon:    
	kon.close()
