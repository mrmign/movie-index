#!/usr/bin/env python
#coding=utf-8

import urllib2  
import thread
import MySQLdb
from bs4 import BeautifulSoup


conn = MySQLdb.connect(host="localhost",
                    user="root",
                    passwd="root",
                    db="movie",
                    charset="utf8")
# conn = MySQLdb.connect("localhost", "root", "root", "movie")
def gethtml(url):
    # print url
    content = urllib2.urlopen(url).read()
    return content

def save(page,url):
    data = gethtml(url)
    # print data
    soup = BeautifulSoup(data)
    # ths = soup.find_all("th",class_="lock")
    # ths = soup.select("th > a")
    ths = soup.select(".lock")
    x = conn.cursor()
    for th in ths:
        a = th.find_all("a")[0]
        # print a
        url = "http://bbs.bt5156.com/" + a.get("href")
        title = a.get_text()
        try:
            sql = 'insert into movie(title, url, page) values ("%s", "%s", "%d") ' % (title, url, page)
            # print sql
            x.execute(sql)
            conn.commit()
        except:
            conn.rollback()
    print "done--", page

    



page = 253
url = "http://bbs.bt5156.com/forumdisplay.php?fid=44&page="
# url = "file:///home/kevin/Desktop/252.html"
for i in range(20, 22):
    # try:
    #     thread.start_new_thread(save,(i,url+str(i)))
    # except:
    #     print "something wrong"
    save(i, url+str(i))
conn.close()