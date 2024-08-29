import requests
import os
import json 
city = input("Enter the name of City\n")
url = f"http://api.weatherapi.com/v1/current.json?key=13e06fcd14364f14848201144242708&q={city}"
r = requests.get(url)
# print(r.text)

wdic = json.loads(r.text)
w = (wdic["current"]["temp_c"])
os.system(f"Say 'The current weather of the {city} is {w} degrees'")