import requests

client_id = {"클라이언트 id"}
client_secret = {"클라이언트 암호"}

keyword = '파이썬'

url = 'https://openapi.naver.com/v1/search/news.json'
# https://redfox.tistory.com
headers = {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret':client_secret}

params = {'query':keyword, 'display':2, 'start':1, 'sort':'date'}

r = requests.get(url, params = params, headers = headers)

j = r.json()
print(j)