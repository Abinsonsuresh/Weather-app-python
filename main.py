import requests
import json

city = input("enter the name of the city: \n")

url = f"https://api.weatherapi.com/v1/current.json?key=128a94b6a2044e3e83d181409231204&q={city}"

r = requests.get(url)
# print(r.text)
wd = json.loads(r.text)
print(type(url))
temp = wd["current"]['temp_c']
print(f"The temprature at {city} is ",temp)