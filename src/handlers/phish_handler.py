import tornado.web
class PhishHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('phish/office.html')

    def post(self):
        issue = self.get_argument('issue')
        print("Wow " + issue)
