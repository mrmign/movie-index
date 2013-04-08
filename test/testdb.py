#!/usr/bin/evn python
# encoding=utf-8
import MySQLdb

# Open database connection
db = MySQLdb.connect(host="localhost",
                    user="root",
                    passwd="root",
                    db="movie",
                    charset="utf8")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
# sql = """INSERT INTO test(cont)
#          VALUES ('This is a test')"""
sql = 'insert into movie(title, url, page) values \
        ("超级杯奶爸/比赛计划 下载", "http://bbs.bt5156.com/viewthread.php?tid=102546&extra=page%3D253", "253")' 
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()