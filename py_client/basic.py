import requests
import json

# endpoint = "https://httpbin.org/status/200/"
endpoint = "http://localhost:8000/api/"

#Aplication progrraming Interface => API
get_response = requests.post(endpoint, json={ "title": "Nome" ,"content": "Gabriel" }) 
print(get_response.json())
# print(get_response)



#DIFERENES BETWEEN HTTP REQUEST AND REST API HTTP REQUEST
# HTTP Request --> Returns a HTML 
# REST API HTTP Request --> returns JSON (xml)