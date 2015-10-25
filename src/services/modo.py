import os

def modoCall(account,api,post_data):
    os.environ['ACCOUNT'] = str(account)
    os.environ['API'] = '/YiiModo/api_v2' + str(api)

    POST_DATA = ''
    for key in post_data:
        POST_DATA+= key + '=' + str(post_data[key]) + '&'

    POST_DATA = POST_DATA[:-1]
    os.environ['POST_DATA'] = POST_DATA

    command ="API=" + str(api) + " && ACCOUNT=" + str(account) + " && POST_DATA=" + str(POST_DATA) + " && ./api_caller.sh"

    os.system(command)

def main():
    modoCall('','/people/register',{'phone': 2145426078 ,'is_modo_terms_agree':1})

if __name__ == "__main__":
    main()
