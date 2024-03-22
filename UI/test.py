import requests
import json
import crypto

url = 'https://localhost:8080/updatedata'
params = {'username': 'aviv', 'password': '123456',
          'data': crypto.encrypt('123456', '[{"web": "example1.com", "email": "user1@example.com", "password": "password1"},{"web": "example2.com", "email": "user2@example.com", "password": "password2"},{"web": "example3.com", "email": "user3@example.com", "password": "password3"},{"web": "example4.com", "email": "user4@example.com", "password": "password4"},{"web": "example5.com", "email": "user5@example.com", "password": "password5"}]')}


def makeRequest(url, params, method='get',password=' '):
    if method == 'get':
        r = requests.get(url, params=params)
    elif method == 'put':
        params['data'] = crypto.encrypt(password, params['data'])
        r = requests.put(url, params=params)
    elif method == 'post':
        r = requests.post(url, params=params)
    else:
        return "failed"
    response = json.loads(r.content.decode('utf-8'))
    if(response['success']):
        if(response['data'] !='[]'):
            response['data'] = crypto.decrypt('123456', response['data'])
        return response
    return 'failed'


#
# res = makeRequest(url, params, 'put')
# print(res)
# print(crypto.decrypt('123456', res.content.decode('utf-8'))
