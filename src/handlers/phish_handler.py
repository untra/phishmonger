import tornado.web
class PhishHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('phish/office.html')
