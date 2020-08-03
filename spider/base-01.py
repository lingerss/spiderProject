'''

内容说明：
1、通过URL获取数据。
2、通过BeautifulSoup解析数据
3、解析数据形式：
（1）解析完整的数据标签（tag）<a></a>
 (2)解析数据的标签内容（tag.string）<a>大家好</a>，内容为：大家好
 (3)解析数据的标签名称（a）
 (4)解析数据的标签类型、标签内容类型(type(a),type(a.string))
 (5)解析数据标签的属性（基本属性：attrs,特殊的如：attrs['class']）
 (6)遍历某个标签(for i in bs.find_all('a')或者find_all(class='title'))
 (7)解析标签父标签(bs.a.parent)
 (8)输出所有的标签(for i in bs.find_all(True))
 (9)解析标签的儿子节点的数量/内容(bs.a.contents; bs.a.contents[1])
 
'''
import requests
from bs4 import BeautifulSoup
#1、第一步获取数据
target='http://python123.io/ws/demo.html'
req=requests.get(url=target)
html=req.text
bs=BeautifulSoup(html,"html.parser")
print(bs.prettify())
'''
Tag
Name
Atrributes
NavigableString
Comment
'''
#2、第二步解析beautifulSoup中获取的html的标签数据
print(bs.title)#获取HTML标题
print(bs.a)#获取HTML的a标签的信息(bs.a),默认获取第一个a标签
print(bs.a.name)#获取a标签的名字
print(bs.a.parent.name)#a标签的父标签的名字
print(bs.a.parent.parent.name)#a标签的父标签的父标签的名字

#3、解析beautifulSoup中获取的html的标签属性数据
print('a标签类型是：',type(bs.a))#查看a标签的类型
print('第一个a标签的属性是：',bs.a.attrs)#获取a标签的所有属性
print('a标签的属性类型是：',type(bs.a.attrs))#a标签的属性类型
print('a标签的class属性是:',bs.a.attrs['class'])#a标签的class属性
print('a标签的href属性是：',bs.a.attrs['href'])#a标签的href属性

#4、解析beautifulSoup中获取的html的标签内容数据
print('第一个a标签的内容：',bs.a.string)#a标签的非属性字符串信息
print('a标签的非属性字符串的类型是：',type(bs.a.string))#查看string字符串类型
print('第一个P标签的内容是：',bs.p.string)#P标签的字符串信息

#介绍一下find_all()方法
'''
find_all(name,attrs,recursive,string,**kwargs)

name:对标签名称的检索字符串
attrs：对标签属性值的检索字符串，可标注属性检索
recursive:是否对子孙全部检索，默认true
string:<>...</>中字符串区域的检索字符串

'''
print('所有a标签的内容：',bs.find_all('a'))#使用find_all方法通过标签名称查找a标签，返回的是一个列表类型
print('a标签和b标签的内容',bs.find_all(['a','b']))#把a标签和b标签作为一个列表传递，可以一次找到a标签和b标签

for t in bs.find_all('a'):#for循环遍历所有a标签，并把返回列表中的内容赋给t
    print('t的值是：',t)#link得到的是标签对象
    print('t的值是：',type(t))
    print('a标签中的href属性是：',t.get('href'))#获取a标签中的url链接

for i in bs.find_all(True):
    print('标签名称：',i.name)
print(bs.head)#head标签
print(bs.head.contents)#head标签的儿子标签，contents返回的是列表类型
print(bs.body.contents)#body标签的儿子标签

print(len(bs.body.contents))#获得body标签儿子节点的数量
print(bs.body.contents[1])#通过列表索引获取第一个节点的内容
print(type(bs))

