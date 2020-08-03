from bs4 import BeautifulSoup
import requests
import bs4
bs=BeautifulSoup(open('spider/resources/x.html',encoding='utf-8'),"html.parser")
print(bs.find('body',).children)

for t in bs.find('body').children:
    if isinstance(t,bs4.element.Tag):#判断子节点是否为Tag对象，是否为标签对象
        print('body的子标签的内容是：',t)#查看t变量获得的对象内容，body的子标签为P标签，一组<p></p>表示一个对象
        print('t的类型是:',type(t))#查看t的类型
#如果要从每个t对象中获取a标签的内容，并把所有a标签都保存到一个列表中
        list=t('a')#t('a')会生成一个bs4.element.ResultSet类型的数据对象，实际上就是Tag列表
        print(list)
        print(type(list))
        print('每个P标签的第一个a标签的内容：',list[0].string)
#获取全国各个大学的排名

url = 'http://www.zuihaodaxue.com/shengyuanzhiliangpaiming2018.html'
r=requests.get(url)
r.encoding=r.apparent_encoding #转换编码,否则中文乱码或者直接r.encoding='utf-8'
html=r.text
soup=BeautifulSoup(html,'html.parser')
for tr in soup.find('thbody').children:
    if isinstance(tr,bs4.element.Tag):
        td=tr('td')
        print(td)
        t=[td[0].string,td[1].string,td[2].string,td[3].string]#把每个学校解析出来的数据放到一个列表中
        print(t)


