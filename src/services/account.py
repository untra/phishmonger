import os
import subprocess
import json

#new_person = account.Account({'phone': 2145426078 , 'fname':'John','lname':'Travolta','is_modo_terms_agree':1})


class Account:

    def __init__(self, post_data):
        self.phone = post_data['phone']
        response = self.initilize_account(post_data)
        self.account = response['account_id']
        self.fname = response['first_name']
        self.lname = response['last_name']
        self.member_since_date = response['member_since_date']


    def initilize_account(self, post_data):
        os.environ['ACCOUNT'] = ''
        os.environ['API'] = '/YiiModo/api_v2/people/register'

        POST_DATA = ''
        for key in post_data:
            POST_DATA+= key + '=' + str(post_data[key]) + '&'

        POST_DATA = POST_DATA[:-1]
        os.environ['POST_DATA'] = POST_DATA

        command ="API=/YiiModo/api_v2/people/register" + " && ACCOUNT=''" + " && POST_DATA=" + str(POST_DATA) + " && ./api_caller.sh"

        # json = os.system(command)
        json_str = subprocess.check_output(command, shell=True)
        json_dict = json.loads(json_str)['response_data']

        return json_dict
