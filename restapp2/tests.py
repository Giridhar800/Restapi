from django.test import TestCase
import requests

# Create your tests here.
URL = "http://127.0.0.1:8000/empall"
r = requests.get(url=URL)
emp_data = r.json()
print(emp_data)
