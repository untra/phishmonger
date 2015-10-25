import tornado.web
import tornado.gen
from models.campaign import Campaign
import models.driver as driver
import rethinkdb as r
import datetime

connection = r.connect(host='localhost', port=28015, db="phishmonger")

class CampaignsHandler(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    def get(self, instance=None):
        conn = yield connection
        messages = self.getMessages()
        name = ""
        verb = "Create New Campaign"
        specific = self.getSpecificCampaign()
        campaigns = []
        if instance is None:#index
            cursor = yield r.table('Campaign').run(conn)
            while (yield cursor.fetch_next()):
                campaign = yield cursor.next()
                campaigns.append(campaign)
        else:#read
            campaigns = yield self.getCampaign(instance)
            specific = campaigns[0]
            name = "{0} {1}".format(campaigns[0].fname, campaigns[1].lname)
            verb = "Update Campaign {0}".format(name)
        if campaigns is None:
            messages.append('No Campaigns to Display!')
            campaigns = []
        self.render('campaigns/index.html', campaigns=campaigns, messages=messages, name=name, verb=verb, specific=specific)


    @tornado.gen.coroutine
    def post(self, instance=None):
        conn = yield connection
        messages = self.getMessages()
        name = ""
        data = self.getSpecificCampaign(default=None)
        data = {k: v for k, v in data.items() if v}
        campaigns = []
        if instance is None:#create
            yield self.newCampaign(data)
            cursor = yield r.table('Campaign').run(conn)
            while (yield cursor.fetch_next()):
                campaign = yield cursor.next()
                campaigns.append(campaign)
            messages.append("Successfully created campaign {0} {1}!".format(data['fname'], data['lname']))
        else:#update
            campaigns = yield self.getCampaign(instance)
            name = "{0} {1}".format(campaigns[0].fname, campaigns[1].lname)
            messages.append("Successfully updated campaign {0} {1}!".format(data['fname'], data['lname']))
        if campaigns is None:
            messages.append('No Campaigns to Display!')
            campaigns = []
        self.render('campaign/index.html', campaigns=campaigns, messages=messages, name=name, verb="Create New Campaign", specific=self.getSpecificCampaign())

    def getSpecificCampaign(self, default=''):
        return {
        'name' : self.get_argument('name',default,strip = True),
        'date_started' : self.get_argument('lname',default,strip = True),
        'targets' : self.get_argument('email',default,strip = True),
        }

    # def delete(self, instance=None):
    #     campaigns = yield self.listCampaigns()
    #     if campaigns is None:
    #         campaigns = []
    #     self.render('campaign/index.html', campaigns=campaigns)

    def getMessages(self):
        messages = []
        return messages

    @tornado.gen.coroutine
    def getCampaign(self, id):
        conn = yield connection
        Campaign().get(conn, {'id':id})


    def launchCampaign(self, campaign, targets):
        now = datetime.datetime.now().strftime('%a %b %d %H:%M:%S %Y')
        name = data['name']
        data['date_started'] = now


    @tornado.gen.coroutine
    def newCampaign(self, data):
        conn = yield connection
        Campaign().insertOne(conn, data)

    @tornado.gen.coroutine
    def listCampaigns(self):
        campaigns = []
        conn = yield connection
        cursor = yield r.table('Campaign').run(conn)
        while (yield cursor.fetch_next()):
            campaign = yield cursor.next()
            campaigns.append(campaign)
        campaigns
