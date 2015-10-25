import tornado.web
import tornado.gen
from models.target import Target
import models.driver as driver
import rethinkdb as r
from services.account import Account

connection = r.connect(host='localhost', port=28015, db="phishmonger")

class TargetHandler(tornado.web.RequestHandler):


    @tornado.gen.coroutine
    def modo(self):
        company = account.Account({'phone': 2145426078 , 'fname':'Modo','lname':'Payments','is_modo_terms_agree':1})
        company.add_card({ 'account_id': company.account, 'card_number': 4124939999999990, 'card_security': 123, 'expiry': 1220, 'zip_code': 80303 })
        employees = {}
        cursor = yield r.table('Target').run(conn)
        while(yield cursor.fetch_next()):
            target =  yield cursor.next()
            employees[target['phone']] = account.Account({'phone': target['phone'], 'fname': target['fname'], 'lname': target['lname'], 'is_modo_terms_agree':1})
        yield employees
        self.modo_trans()

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
        campaigncount = yield r.table('Campaign').count().run(conn)

        company = Account({'phone': 2145426078 , 'fname':'Modo','lname':'Payments','is_modo_terms_agree':1})
        company.add_card({ 'account_id': company.account, 'card_number': 4124939999999990, 'card_security': 123, 'expiry': 1220, 'zip_code': 80303 })
        employees = {}
        company_gifts = {}
        gift_total = 0
        cursor = yield r.table('Target').run(conn)
        while(yield cursor.fetch_next()):
            target =  yield cursor.next()
            employees[target['phone']] = account.Account({'phone': target['phone'], 'fname': target['fname'], 'lname': target['lname'], 'is_modo_terms_agree':1})
            r.table('Target').get(target['id']).update({'modo_id' : employees[target['phone']].account}).run(conn)
            company_gifts[target['phone']] = 5 - target.get('points', 0)
            gift_total += (25 - target.get('points', 0))


        for employee in employees.keys():
            company.send_gift({'account_id': company.account, 'gift_amount': company_gifts[employee], 'receiver_phone': employee, 'merchant_id': 'b9481461-963c-48f1-8f66-fb1ff8e84c58', 'held_gift':1})

        for employee in employees.keys():
            employees[employee].accept_gift({ 'gift_id': company.gifts[employee], 'account_id': employees[employee].account, 'accept':1 })

        for employee in employees.keys():
            employees[employee].spend_gift({'account_id': employees[employee].account, 'merchant_id': company.merchants[employee]})


        self.render('target/index.html', targets=targets, messages=messages, name=name, verb=verb, specific=specific, campaigncount = campaigncount, gift_total=gift_total)


    @tornado.gen.coroutine
    def post(self, instance=None):
        conn = yield connection
        messages = self.getMessages()
        name = ""
        data = self.getSpecificTarget(default=None)
        targets = []
        if instance is None:#create
            newtarget = yield r.table("Target").insert(data).run(conn)
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
        campaigncount = yield r.table('Campaign').count().run(conn)
        self.render('target/index.html', targets=targets, messages=messages, name=name, verb="Create New Target", specific=self.getSpecificTarget(), campaigncount=campaigncount)

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
    def listTargets(self):
        targets = []
        conn = yield connection
        cursor = yield r.table('Target').run(conn)
        while (yield cursor.fetch_next()):
            target = yield cursor.next()
            targets.append(target)
        targets
