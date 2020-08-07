import json
import urllib.parse
import urllib.request
import math
def getJsonObject(id,page):
    dataURL='http://s.club.jd.com/productpage/p-%s-s-0-t-3-p-%s.html' % (id, page)
    headers = {
        "Host": "s.club.jd.com",
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36",
        "Referer": "http://item.jd.com/%s.html" % (id),
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Cookie": "__jdv=122270672|direct|-|none|-; _tp=oURFLGYfOUlb%2BSsEmyf6XQ%3D%3D; unick=tbkken; _pst=tbkken; TrackID=1q3JB8P-Anwjdhzb4iITB8jwEl0kkLQqHhBSJ6mEucV6MiJU2lHvzKfcCgtHxedbKGh3Q7R9rXdoOdBsj7Ym4pA; pinId=z84kP9ZopZw; pin=tbkken; ipLocation=%u5317%u4EAC; areaId=1; ipLoc-djd=1-72-2799-0; thor=5F666BD0AA88FC1B35E70FE415A3A7AD69B80CDCDB2926A2C7EF6971B3A410F431BD3C69D925C5A1C4CCB40C540D3A06054196973027CC36BDE3597422C47A2022C48FD83EF5AC1B117FA0BD416C90F807E4F627F4450B859C8113F9B483FB48A92B2F24CB05DCACBED6EEC1B174D359DB08A6CFB512F8FDB073EB7849487639; __jda=122270672.1865742098.1460359166.1465739554.1465802065.8; __jdb=122270672.3.1865742098|8.1465802065; __jdc=122270672; __jdu=1865742098"
    }
    req=urllib.request.Request(dataURL,headers=headers)
    response=urllib.request.urlopen(req)
    jsonString=response.read()
    jsonObject=json.loads(jsonString.decode("GBK"))
    return jsonObject

page=0
id=11123672
jsonObject=getJsonObject(id,page)
 #math.floor(i) 小于等于i的最大整数; math.ceil(i) 大于等于i的最小整数;
pages=math.ceil(jsonObject['productCommentSummary']['commentCount']/10)+1
contents=[]
for page in range(pages):
    jsonObject=getJsonObject(id,page)
    comments=jsonObject['comments']
    for comment in comments:
        contents.append(comment['content'])

