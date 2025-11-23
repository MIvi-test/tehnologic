import requests

r = requests.get("https://dfedorov.spb.ru/python3/sport.txt")
r.encoding = 'cp1251'
r = r.headers
print(r)

