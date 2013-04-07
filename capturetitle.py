#!/usr/bin/env python
#coding:utf-8

import urllib2  
import thread
import MySQLdb
from bs4 import BeautifulSoup


conn = MySQLdb.connect(host="localhost",
                    user="root",
                    password="root",
                    db="movie")
def gethtml(url):
    content = urllib2.urlopen(url).read()
    return content

def save(page,url):
    data = gethtml(url)
    soup = BeautifulSoup(data)

# x = conn.cursor()
# try:
#     x.execute('''insert into movie values (%s, %s) ''', ())
#     conn.commit()
# except:
#     conn.rollback()

# conn.close()

page = 254
url = "http://bbs.bt5156.com/forumdisplay.php?fid=44&page="
for i in range(page):
    thread.start_new_thread(save,(i,url+str(i)))