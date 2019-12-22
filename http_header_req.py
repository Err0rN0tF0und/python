import urllib

url = "http://www.nostarch.com"

headers = {}
headers['User-Agent'] = 'Googlebot'

request = urllib.Request(url,headers=headers)
response = urllib.urlopen(request)

print(response.read())
response.close()
