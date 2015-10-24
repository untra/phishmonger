import tornado.web
import tornado.gen
from models.target import Target
import models.driver as driver
import rethinkdb as r

connection = r.connect(host='localhost', port=28015)
db = "phishmonger"

class TargetHandler(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    def get(self):
        targets = yield self.listTargets()
        if targets is None:
            targets = []
        self.render('target/index.html', targets=targets)

    @tornado.gen.coroutine
    def listTargets(self):
        conn = yield connection
        conn.use("phishmonger")
        yield Target().get(conn)
