from django.test import TestCase
import requests
import json

# Create your tests here.
URL = " http://127.0.0.1:8000/emp/"
def get_record(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
        jsondata = json.dumps(data)
        r = requests.get(url=URL, data=jsondata)
        data = r.json()
        print(data)
get_record()

def post_record():
    data = {'name': 'Giri3',
            'address': 'kadapa',
            'mail': 'Giri@gmail.com',
            'age': 24
            }
    jsondata = json.dumps(data)
    r = requests.post(url=URL, data=jsondata)
    data = r.json()
    print(data)
# post_record()

def updated_record():
    data = {'id': 2,
            'name': 'giri2',
            'address': 'kadapa',
            'mail': 'venkey@gmail.com',
            'age': 24
            }
    jsondata = json.dumps(data)
    r = requests.put(url=URL, data=jsondata)
    data = r.json()
    print(data)
# updated_record()

def delete_data():
    data = {'id': 8}
    jsondata = json.dumps(data)
    r = requests.delete(url=URL, data=jsondata)
    data = r.json()
    print(data)
# delete_data()
