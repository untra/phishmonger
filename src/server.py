import subprocess
import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import logging
from tornado import ioloop, gen
from tornado.concurrent import Future, chain_future
from tornado.options import define, options
from config.config import application
import models.driver as driver
import rethinkdb as r
connection = r.connect(host='localhost', port=28015, db="phishmonger")


#Sends the new user joined alerts to all subscribers who subscribed
@tornado.gen.coroutine
def update_responses():
    while True:
        try:
            print 'fdsa'
            conn = yield connection
            feed = yield r.table("Response").changes().run(conn)

            while (yield feed.fetch_next()):
                response_change = yield feed.next()
                print 'response CCHHAANGGEE'
                print response_change
        except:
            pass

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    print "Listening for connections on... localhost:{0}".format(options.port)
    driver.init()
    tornado.ioloop.IOLoop.current().add_callback(update_responses)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
