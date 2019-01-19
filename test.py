import requests
import json
import urllib3


api_token = '8hkk65zbrm2232ah2gccgd9p '
api_url_base = 'https://chmurka.egnyte.com/pubapi/v1/'

headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}

def get_account_info():
    api_url = '{0}account'.format(api_url_base)
    response = requests.get(api_url, headers=headers)

    if response.status_code >= 500:
        print('[!] [{0}] Server Error'.format(response.status_code))
        return None
    elif response.status_code == 404:
        print('[!] [{0}] URL not found: [{1}]'.format(response.status_code,api_url))
        return None  
    elif response.status_code == 401:
        print('[!] [{0}] Authentication Failed'.format(response.status_code))
        return None
    elif response.status_code == 400:
        print('[!] [{0}] Bad Request'.format(response.status_code))
        return None
    elif response.status_code >= 300:
        print('[!] [{0}] Unexpected Redirect'.format(response.status_code))
        return None
    elif response.status_code == 200:
        ssh_keys = json.loads(response.content.decode('utf-8'))
        return ssh_keys
    else:
        print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))
        return None


account_info = get_account_info()

if account_info is not None:
    print("Here's your info: ")
    for k, v in account_info['account'].items():
        print('{0}:{1}'.format(k, v))

else:
    print('[!] Request Failed')

