import os
import subprocess
import json

# Examples:
# person1 = account.Account({'phone': 2145426078 , 'fname':'John','lname':'Travolta','is_modo_terms_agree':1})
# person2 = account.Account({'phone': 2145426087 , 'fname':'Samuel','lname':'Jackson','is_modo_terms_agree':1})
# person3 = account.Account({'phone': 2145426187 , 'fname':'Harvey','lname':'Keitel','is_modo_terms_agree':1})
#
# person1.add_card({ 'account_id': person1.account, 'card_number': 4124939999999990, 'card_security': 123, 'expiry': 1220, 'zip_code': 80303 })
#
# person1.send_gift({'account_id': person1.account, 'gift_amount': 25, 'receiver_phone': person2.phone, 'merchant_id': 'b9481461-963c-48f1-8f66-fb1ff8e84c58', 'held_gift':1})
# person1.send_gift({'account_id': person1.account, 'gift_amount': 15, 'receiver_phone': person3.phone, 'merchant_id': 'b9481461-963c-48f1-8f66-fb1ff8e84c58', 'held_gift':1})
#
# person2.accept_gift({ 'gift_id': person1.gifts[person2.phone], 'account_id': person2.account, 'accept':1 })
# person3.accept_gift({ 'gift_id': person1.gifts[person3.phone], 'account_id': person3.account, 'accept':1 })
#
# person2.spend_gift({'account_id': person2.account, 'merchant_id': person1.merchants[person2.phone]})
# person3.spend_gift({'account_id': person3.account, 'merchant_id': person1.merchants[person3.phone]})
#
# person2.transaction_history({'account_id': person2.account})
# person2.transaction_history({'account_id': person3.account})

class Account:

    def __init__(self, post_data):
        self.phone = post_data['phone']
        response = self.initilize_account(post_data)
        self.account = response['account_id']
        self.fname = response['first_name']
        self.lname = response['last_name']
        self.member_since_date = response['member_since_date']
        self.gifts = {}
        self.merchants = {}


    def initilize_account(self, post_data):
        os.environ['ACCOUNT'] = ''
        os.environ['API'] = '/YiiModo/api_v2/people/register'

        POST_DATA = ''
        for key in post_data:
            POST_DATA+= key + '=' + str(post_data[key]) + '&'

        POST_DATA = POST_DATA[:-1]
        os.environ['POST_DATA'] = POST_DATA

        command ="API=/YiiModo/api_v2/people/register" + " && ACCOUNT=''" + " && POST_DATA=" + str(POST_DATA) + " && ./services/api_caller.sh"
        # command = "ls"
        # json = os.system(command)
        json_str = subprocess.check_output(command, shell=True)
        json_dict = json.loads(json_str)['response_data']

        return json_dict


    def add_card(self, post_data):
        os.environ['ACCOUNT'] = ''
        os.environ['API'] = '/YiiModo/api_v2/card/add'

        POST_DATA = ''
        for key in post_data:
            POST_DATA+= key + '=' + str(post_data[key]) + '&'

        POST_DATA = POST_DATA[:-1]
        os.environ['POST_DATA'] = POST_DATA

        command ="API=/YiiModo/api_v2/card/add" + " && ACCOUNT=''" + " && POST_DATA=" + str(POST_DATA) + " && ./services/api_caller.sh"

        # json = os.system(command)
        json_str = subprocess.check_output(command, shell=True)
        # json_dict = json.loads(json_str)['response_data']
        #
        # return json_dict


    def send_gift(self, post_data):
        os.environ['ACCOUNT'] = self.account
        os.environ['API'] = '/YiiModo/api_v2/gift/send'

        POST_DATA = ''
        for key in post_data:
            POST_DATA+= key + '=' + str(post_data[key]) + '&'

        POST_DATA = POST_DATA[:-1]
        os.environ['POST_DATA'] = POST_DATA

        command ="API=/YiiModo/api_v2/gift/send" + " && ACCOUNT=''" + " && POST_DATA=" + str(POST_DATA) + " && ./services/api_caller.sh"

        # json = os.system(command)
        json_str = subprocess.check_output(command, shell=True)
        print "+++++++++++++++"
        print json_str
        json_dict = json.loads(json_str)['response_data']

        self.gifts[post_data['receiver_phone']] = json_dict['gift_id']
        self.merchants[post_data['receiver_phone']] = post_data['merchant_id']

        # return json_dict

    def accept_gift(self, post_data):
        os.environ['ACCOUNT'] = self.account
        os.environ['API'] = '/YiiModo/api_v2/gift/accept'

        POST_DATA = ''
        for key in post_data:
            POST_DATA+= key + '=' + str(post_data[key]) + '&'

        POST_DATA = POST_DATA[:-1]
        os.environ['POST_DATA'] = POST_DATA

        command ="API=/YiiModo/api_v2/gift/accept" + " && ACCOUNT=''" + " && POST_DATA=" + str(POST_DATA) + " && ./services/api_caller.sh"

        # json = os.system(command)
        json_str = subprocess.check_output(command, shell=True)
        json_dict = json.loads(json_str)['response_data']


        return json_dict

    def spend_gift(self, post_data):
        os.environ['ACCOUNT'] = self.account
        os.environ['API'] = '/YiiModo/api_v2/location/visit'

        POST_DATA = ''
        for key in post_data:
            POST_DATA+= key + '=' + str(post_data[key]) + '&'

        POST_DATA = POST_DATA[:-1]
        os.environ['POST_DATA'] = POST_DATA

        command ="API=/YiiModo/api_v2/location/visit" + " && ACCOUNT=''" + " && POST_DATA=" + str(POST_DATA) + " && ./services/api_caller.sh"

        # json = os.system(command)
        json_str = subprocess.check_output(command, shell=True)
        json_dict = json.loads(json_str)['response_data']

        return json_dict

    def transaction_history(self, post_data):
        os.environ['ACCOUNT'] = self.account
        os.environ['API'] = '/YiiModo/api_v2/transaction/history'

        POST_DATA = ''
        for key in post_data:
            POST_DATA+= key + '=' + str(post_data[key]) + '&'

        POST_DATA = POST_DATA[:-1]
        os.environ['POST_DATA'] = POST_DATA

        command ="API=/YiiModo/api_v2/transaction/history" + " && ACCOUNT=''" + " && POST_DATA=" + str(POST_DATA) + " && ./services/api_caller.sh"

        # json = os.system(command)
        json_str = subprocess.check_output(command, shell=True)
        print '+++++++++++TRANSACTION HISTORY++++++++++++'
        print json_str
        json_dict = json.loads(json_str)['response_data']


        return json_dict
