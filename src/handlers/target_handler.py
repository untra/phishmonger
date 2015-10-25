import tornado.web
import tornado.gen
from models.target import Target
import models.driver as driver
import rethinkdb as r

connection = r.connect(host='localhost', port=28015, db="phishmonger")

class TargetHandler(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    def get(self, instance=None):
        conn = yield connection
        messages = self.getMessages()
        name = ""
        verb = "Create New Target"
        specific = self.getSpecificTarget()
        targets = []
        if instance is None:#index
            cursor = yield r.table('Target').run(conn)
            while (yield cursor.fetch_next()):
                target = yield cursor.next()
                targets.append(target)
        else:#read
            targets = yield self.getTarget(instance)
            specific = targets[0]
            name = "{0} {1}".format(targets[0].fname, targets[1].lname)
            verb = "Update Target {0}".format(name)
        if targets is None:
            messages.append('No Targets to Display!')
            targets = []
        self.render('target/index.html', targets=targets, messages=messages, name=name, verb=verb, specific=specific)


    @tornado.gen.coroutine
    def post(self, instance=None):
        conn = yield connection
        messages = self.getMessages()
        name = ""
        data = self.getSpecificTarget(default=None)
        data = {k: v for k, v in data.items() if v}
        targets = []
        if instance is None:#create
            yield self.newTarget(data)
            cursor = yield r.table('Target').run(conn)
            while (yield cursor.fetch_next()):
                target = yield cursor.next()
                targets.append(target)
            messages.append("Successfully created target {0} {1}!".format(data['fname'], data['lname']))
        else:#update
            targets = yield self.getTarget(instance)
            name = "{0} {1}".format(targets[0].fname, targets[1].lname)
            messages.append("Successfully updated target {0} {1}!".format(data['fname'], data['lname']))
        if targets is None:
            messages.append('No Targets to Display!')
            targets = []
        self.render('target/index.html', targets=targets, messages=messages, name=name, verb="Create New Target", specific=self.getSpecificTarget())

    def getSpecificTarget(self, default=''):
        return {
        'fname' : self.get_argument('fname',default,strip = True),
        'lname' : self.get_argument('lname',default,strip = True),
        'email' : self.get_argument('email',default,strip = True),
        'group' : self.get_argument('group',default,strip = True),
        'phone' : self.get_argument('phone',default,strip = True),
        }

    # def delete(self, instance=None):
    #     targets = yield self.listTargets()
    #     if targets is None:
    #         targets = []
    #     self.render('target/index.html', targets=targets)

    def getMessages(self):
        messages = []
        return messages

    @tornado.gen.coroutine
    def getTarget(self, id):
        conn = yield connection
        Target().get(conn, {'id':id})

    @tornado.gen.coroutine
    def newTarget(self, data):
        conn = yield connection
        Target().insertOne(conn, data)

    @tornado.gen.coroutine
    def listTargets(self):
        targets = []
        conn = yield connection
        cursor = yield r.table('Target').run(conn)
        while (yield cursor.fetch_next()):
            target = yield cursor.next()
            targets.append(target)
        targets
