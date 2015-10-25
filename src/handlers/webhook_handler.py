import tornado.web
class WebhookHandler(tornado.web.RequestHandler):

    def post(self):
        event = self.get_argument('event',None)
        timestamp = self.get_argument('timestamp',None)
        recipient = self.get_argument('recipient',None)
        print event
        print timestamp
        print recipient
