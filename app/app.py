#!/usr/bin/env python
#coding=utf-8

import os

import tornado.wsgi
import tornado.web
import tornado.options
import tornado.httpserver
import tornado.ioloop
import MySQLdb
import torndb
from tornado.options import define, options
# from bae.core import const
define("port", default=8888, help="run on the given port", type=int)
define("mysql_host", default="127.0.0.1:3306", help="blog database host")
define("mysql_database", default="movie", help="blog database name")
define("mysql_user", default="root", help="blog database user")
define("mysql_password", default="root", help="blog database password")

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db
        # db = MySQLdb.connect(
        #     host = const.MYSQL_HOST,
        #     port = int(const.MYSQL_PORT),
        #     user = const.MYSQL_USER,
        #     passwd = const.MYSQL_PASS,
        #     db = "movie"
        #     )
        

class HomeHandler(BaseHandler):
    def get(self):
        firstpage = self.db.query("select * from movie where page = 1")
        self.render("home.html", movies=firstpage)

    def post(self):
        title = self.get_argument("moviename")
        res = self.db.query("""select * from movie where title like %s""", "%"+title+"%")
        self.render("home.html", movies=res)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", HomeHandler),
           
        ]
        settings = dict(
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            debug=True,
            )
        tornado.web.Application.__init__(self, handlers, **settings)

        # Have one global connection to the blog DB across all handlers
        self.db = torndb.Connection(
            host=options.mysql_host, database=options.mysql_database,
            user=options.mysql_user, password=options.mysql_password)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()