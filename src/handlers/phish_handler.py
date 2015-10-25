import tornado.web
from tornado.concurrent import Future
import rethinkdb as r
connection = r.connect(host='localhost', port=28015, db="phishmonger")
class PhishHandler(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    def get(self, response_id=None):
        if response_id is not None:
            conn = yield connection
            update = yield r.table("Response").get(response_id).update({'status' : 3}).run(conn)
        self.render('phish/office.html')

    @tornado.gen.coroutine
    def post(self, response_id=None):
        issue = self.get_argument('issue')
        response_id = self.get_argument('response_id', response_id)
        print("Wow " + issue)
        conn = yield connection
        print 'beee'
        if issue == 'username_press':
            update = yield r.table("Response").get(response_id).update({"points": (r.row["points"]+1).default(0)}).run(conn)
            print update
        if issue == 'password_press':
            update = yield r.table("Response").get(response_id).update({"points": (r.row["points"]+1).default(0)}).run(conn)
            print update
        if issue == 'submit':
            update = yield r.table("Response").get(response_id).update({'status' : 4}).run(conn)
