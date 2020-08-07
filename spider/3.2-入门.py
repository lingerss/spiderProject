#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas
import pymysql
import json
import urllib.request
#编码是utf8不是utf-8
conn=pymysql.connect(host="localhost",user="root",password="root123",database="web",charset="utf8")
ips=pandas.read_sql(
   """
   SELECT ip FROM (
            SELECT remote_Addr ip FROM t_web_visit_log GROUP BY remote_Addr
        ) a WHERE ip NOT IN (SELECT ip FROM t_dim_ip_info);
    """,con=conn)
print(ips)
#cursor=conn.cursor;cursor.execute(sql)
while ips.size!=0:
    ipInfos = []
    for ip in ips.ip:
        print("get ip:%s" % (ip))
        try:            
            response = urllib.request.urlopen('http://ip.taobao.com/service/getIpInfo.php?ip=%s' % (ip))
            jsonString = response.read()
            jsonObject = json.loads(jsonString.decode())
            
            if jsonObject['code']==0:
                country = jsonObject['data']['country']
                area = jsonObject['data']['area']
                region = jsonObject['data']['country']
                city = jsonObject['data']['city']
                isp = jsonObject['data']['isp']
                
                ipInfos = ipInfos + [(ip, country, area, region, city, isp)]

            if len(ipInfos)==100:
                cursor = conn.cursor()
                sql = """
                    insert into t_dim_ip_info 
                        values(%s, %s, %s, %s, %s, %s);
                """
                print(sql)
                cursor.executemany(sql, ipInfos)
                cursor.close()
                ipInfos = []
        except Exception as e:
            print(e)

    ips = pandas.read_sql(
        """
            SELECT ip FROM (
                SELECT remote_Addr ip FROM t_web_visit_log GROUP BY remote_Addr
            ) a WHERE ip NOT IN (SELECT ip FROM t_dim_ip_info);
        """, 
        con=conn
    )

conn.close()
