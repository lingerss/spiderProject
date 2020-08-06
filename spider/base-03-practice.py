'''
python中实现HTTP请求的三种方式：
1：urllib2/urllib。
2：httplib/urllib。
3: Requests。
'''
'''
1：urllib2/urllib实现
urllib2和urllib是Python中的两个内置模块，要实现HTTP功能，实现方式是以urllib2为主，urllib为辅
python2中urllib2.urlopen()，而python3中是urllib.request.urlopen()

User-Agent：有些服务器或Proxy会通过该值来判断是否是浏览器发出的请求。
Content-Type：在使用REST接口时，服务器会检查该值，用来确定HTTP Body中的内容该怎样解析。在使用服务器提供的RESTful或SOAP服务时，Content-Type设置错误会导致服务器拒绝服务。常见的取值有：application/xml（在XML RPC，如RESTful/SOAP调用时使用）、application/json（在JSON RPC调用时使用）、application/x-www-form-urlencoded（浏览器提交Web表单时使用）。
Referer：服务器有时候会检查防盗链。
'''
import urllib.request
#演绎的get请求
response=urllib.request.urlopen('http://www.zhihu.com')
html=response.read()
print(html)
#或者如下方式先请求后响应
# 请求
request=urllib.request.Request('http://www.zhihu.com')
# 响应
response = urllib.request.urlopen(request)
html=response.read()

#演示的post请求;带请求头header的响应
import urllib
url = 'http://www.xxxxxx.com/login'

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
referer='http://www.xxxxxx.com/'
#方案一
postdata = {'username' : 'qiye','password' : 'qiye_pass'}
header={'User-Agent':user_agent,'Referer':referer}
data = urllib.parse.urlencode(postdata)#数据编码
req = urllib.request.Request(url, data,header)#请求
response = urllib.request.urlopen(req)#响应
html = response.read()
#方案二
req1 = urllib.request.Request(url, data)#请求
req1.add_header('User-Agent',user_agent)
req1.add_header('Referer',referer)
response = urllib.request.urlopen(req1)#响应
html = response.read()

#对cookie的处理
import urllib
# import cookielib已经改成了from http import cookiejar
from http import cookiejar

cookie = cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
response = opener.open('http://www.zhihu.com')
for item in cookie:
    print (item.name+':'+item.value)
#自己添加cookie
import  urllib.request
opener = urllib.request.build_opener()
opener.addheaders.append( ( 'Cookie', 'email=' + "xxxxxxx@163.com" ) )
req = urllib.request.Request( "http://www.zhihu.com/" )
response = opener.open(req)
print(response.headers)
retdata = response.read()
#Timeout设置超时
#在Python2.6之前的版本，urllib2的API并没有暴露Timeout的设置，要设置Timeout值，只能更改Socket的全局Timeout值,示例如下：

import urllib.request
import socket
socket.setdefaulttimeout(10) #10秒钟后超时
urllib.request.socket.setdefaulttimeout(10) #另一种方式

#在Python2.6及新的版本中，urlopen函数提供了对Timeout的设置，示例如下:
import urllib.request
request=urllib.request.Request('http://www.zhihu.com')
response = urllib.request.urlopen(request,timeout=2)
html=response.read()
print(html)

#获取HTTP响应码
import urllib.request
try:
    response = urllib.request.urlopen('http://www.google.com')
    print(response)
except urllib.request.HTTPError as e:
    if hasattr(e, 'code'):
        print ('Error code:',e.code)
#urllib2默认情况下会针对HTTP 3XX返回码自动进行重定向动作。
# 要检测是否发生了重定向动作，只要检查一下Response的URL和Request的URL是否一致就可以了，示例如下：
import urllib
response = urllib.request.urlopen('http://www.zhihu.cn')
isRedirected = response.geturl() == 'http://www.zhihu.cn'
#如果不想自动重定向，可以自定义HTTPRedirectHandler类，示例如下：
import urllib
class RedirectHandler(urllib.request.HTTPRedirectHandler):
    def http_error_301(self, req, fp, code, msg, headers):
        pass
    def http_error_302(self, req, fp, code, msg, headers):
        result = urllib.request.HTTPRedirectHandler.http_error_301(self, req, fp, code, 
        msg, headers)
        result.status = code
        result.newurl = result.geturl()
        return result
opener = urllib.request.build_opener(RedirectHandler)
opener.open('http://www.zhihu.cn')
# Proxy的设置
#在做爬虫开发中，必不可少地会用到代理。urllib2默认会使用环境变量http_proxy来设置HTTP Proxy。
# 但是我们一般不采用这种方式，而是使用ProxyHandler在程序中动态设置代理，示例代码如下：
import urllib
proxy = urllib.request.ProxyHandler({'http': '127.0.0.1:8087'})
opener = urllib.request.build_opener([proxy,])
urllib.request.install_opener(opener)
response = urllib.request.urlopen('http://www.zhihu.com/')
print (response.read())
#这里要注意的一个细节，使用urllib2.install_opener()会设置urllib2的全局opener，
# 之后所有的HTTP访问都会使用这个代理。这样使用会很方便，但不能做更细粒度的控制，比如想在程序中使用两个不同的Proxy设置，这种场景在爬虫中很常见。
# 比较好的做法是不使用install_opener去更改全局的设置，而只是直接调用opener的open方法代替全局的urlopen方法，修改如下：
import urllib
proxy = urllib.request.ProxyHandler({'http': '127.0.0.1:8087'})
opener = urllib.request.build_opener(proxy,)
response = opener.open("http://www.zhihu.com/")
print (response.read())

