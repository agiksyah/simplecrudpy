#!/usr/bin/python

import MySQLdb as db
import sys

try:
    kon = db.connect('localhost', 'root', '', 'crudpy');
    cur = kon.cursor()
    cur.execute("SELECT VERSION()")
    ver = cur.fetchone()
    print "Database version : %s" % ver
    
except db.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
finally:        
    if kon:    
        kon.close()
