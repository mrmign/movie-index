#!/usr/bin/env python
#coding:utf-8

import urllib2  
import thread
import MySQLdb
from BeautifulSoup import BeautifulSoup


# conn = MySQLdb.connect(host="localhost",
#                     user="root",
#                     password="root",
#                     db="movie")
conn = MySQLdb.connect("localhost", "root", "root", "movie")
def gethtml(url):
    content = urllib2.urlopen(url).read()
    return content

def save(page,url):
    data = gethtml(url)
    print data
    soup = BeautifulSoup(data)
    # ths = soup.find_all("th",class_="lock")
    # ths = soup.select("th > a")
    ths = soup.select(".lock")
    x = conn.cursor()
    for th in ths:
        a = th.find_all("a")[0]
        url = a.get("link")
        title = a.get_text()
        try:
            x.execute('''insert into movie(title, url, page) values (%s, %s, %s) ''', (title, url, page))
            conn.commit()
        except:
            conn.rollback()

    conn.close()



page = 254
# url = "http://bbs.bt5156.com/forumdisplay.php?fid=44&page="
url = "file:///home/kevin/Desktop/252.html"
for i in range(253, page):
    # thread.start_new_thread(save,(i,url+str(i)))
    save(i, url)