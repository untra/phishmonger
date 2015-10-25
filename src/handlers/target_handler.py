import tornado.web
import tornado.gen
from models.target import Target
import models.driver as driver
import rethinkdb as r

connection = r.connect(host='localhost', port=28015)
db = "phishmonger"

class TargetHandler(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    def get(self, instance=None):
        messages = self.getMessages()
        name = ""
        verb = "Create New Target"
        if instance is None:#index
            targets = yield self.listTargets()
        else:#read
            targets = yield self.getTarget(instance)
            name = "{0} {1}".format(targets[0].fname, targets[1].lname)
            verb = "Update Target {0}".format(name)
        if targets is None:
            messages.append('No Targets to Display!')
            targets = []
        self.render('target/get.html', targets=targets, messages=messages, name=name)

    def post(self, instance=None):
        messages = self.getMessages()
        name = ""
        data = {}
        data['fname'] = self.get_argument('fname',None,strip = True)
        data['lname'] = self.get_argument('lname',None,strip = True)
        data['group'] = self.get_argument('group',None,strip = True)
        data['email'] = self.get_argument('email',None,strip = True)
        data['tel'] = self.get_argument('tel','',strip = True)
        data = {k: v for k, v in data.items() if v}
        if Target.verify(data):
            if instance is None:#create
                targets = yield self.listTargets()
            else:#update
                targets = yield self.getTarget(instance)
                name = "{0} {1}".format(targets[0].fname, targets[1].lname)
        self.render('target/index.html', targets=targets)

    # def delete(self, instance=None):
    #     targets = yield self.listTargets()
    #     if targets is None:
    #         targets = []
    #     self.render('target/index.html', targets=targets)

    def getMessages(self):
        messages = []
        return messages

    @tornado.gen.coroutine
    def listTargets(self):
        conn = yield connection
        conn.use(db)
        yield Target().get(conn)

    @tornado.gen.coroutine
    def getTarget(self, id):
        conn = yield connection
        conn.use(db)
        yield Target().get(conn, {'id':id})

    @tornado.gen.coroutine
    def newTarget(self, data):
        conn = yield connection
        conn.use(db)
        yield Target().insertOne(conn, data)

    # @tornado.gen.coroutine
    # def listTargets(self):
    #     conn = yield connection
    #     conn.use(db)
    #     yield Target().get(conn)
