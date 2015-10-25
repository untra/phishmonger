import tornado.web
import tornado.gen
import rethinkdb as r

connection = r.connect(host='localhost', port=28015, db="phishmonger")

class WebhookHandler(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    def post(self):
        conn = yield connection
        event = self.get_argument('event',None)
        recipient = self.get_argument('recipient',None)
        if event == 'delivered':
            yield r.table("Response").update({'status' : 1})
        if event == 'opened':
            yield r.table("Response").update({'status' : 2})
        if event == 'clicked':
            yield r.table("Response").update({'status' : 3})

        print event
        print recipient
