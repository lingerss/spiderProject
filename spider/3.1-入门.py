import json
import urllib.request
response=urllib.request.urlopen('file:///D:/study-tools//code//spiderProject//spider//resources//json.json')
jsonString=response.read()
jsonObject=json.loads(jsonString.decode())
jsonObject['employees']
jsonObject['employees'][0]
jsonObject['employees'][0]['lastName']

