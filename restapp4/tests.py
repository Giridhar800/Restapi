from django.test import TestCase
import requests
import json

# Create your tests here.
URL =" http://127.0.0.1:8000/trainer/"

def get_record(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
        jsondata = json.dumps(data)
        headers = {'content-type': 'application/json'}
        r = requests.get(url=URL, headers=headers, data=jsondata)
        data = r.json()
        print(data)
# get_record(1)

def post_record():
    data = {
        'name': 'sunil1',
        'address': 'kadapa',
        'mail': 'sunil1@gmail.com',
        'age': '22'
    }
    jsondata = json.dumps(data)
    headers = {'content-type': 'application/json'}
    r = requests.post(url=URL, headers=headers, data=jsondata)
    data = r.json()
    print(data)
# post_record()

def update_record():
    data = {
        'id': 1,
        'name': 'giri11',
        'address': 'kadapa',
        'mail': 'Giri11@gmail.com',
        'age': '22'
    }
    jsondata = json.dumps(data)
    headers = {'content-type': 'application/json'}
    r = requests.put(url=URL, headers=headers, data=jsondata)
    data = r.json()
    print(data)
# update_record()

def delete_record(id=None):

    data = {'id':1}
    jsondata = json.dumps(data)
    headers = {'content-type': 'application/json'}
    r = requests.delete(url=URL, headers=headers, data=jsondata)
    data = r.json()
    print(data)
delete_record()





