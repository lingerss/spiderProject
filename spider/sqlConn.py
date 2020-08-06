#1、建立数据库连接utf8不是utf-8
import pymysql
def getConnection(host,user,password,database,encode):
    conn=pymysql.connect(host=host,user=user,password=password,database=database,charset=encode)
    return conn
#2、添加多条数据的操作
def addManyData(conn,sql,data):
    cursor=conn.cursor()#获取光标
    #(1)定义执行的sql语句，如：
    #sql="insert into userinfo(user,pwd)values(%s.%s);"
    #(2)定义传入的参数。如：
    #data=[('july','147'),('june','258'),('marin','369')]
    #(3)执行sql语句
    cursor.executemany(sql,data)
    #(4)涉及写操作要注意提交
    cursor.commit()
    #关闭连接
    cursor.close()
    conn.close()
#3、添加单条数据的操作
def addSingleData(conn,sql,data):
  cursor=conn.cursor()#获取光标
  #sql='insert into userinfo(user,pwd) values(%s,%s);'
  #name='wuli'
  #pwd='123456789'
  #cursor.execute(sql,[name,pwd])
  cursor.execute(sql,data)
  conn.commit()
  cursor.close()
  conn.close()
#4、获取最新插入数据(最后一条)
def getLastUpdatedData(conn,sql,data):
    cursor=conn.cursor()
    #sql='insert into userinfo(user,pwd) values(%s,%s);'
    #name='wuli'
    #pwd='123456789'
    #cursor.execute(sql,[name,pwd])
    cursor.execute(sql,data)
    conn.commit()
    last_id=cursor.lastrowid
    print('最后一条数据的ID是：',last_id)
    cursor.close()
    conn.close()
#5、删除操作
def deleteData(conn,sql,data):
    cursor=conn.cursor()
    #sql="delete from userinfo where user=%s;"
    #name="june"
    #拼接执行sql语句
    # cursor.execute(sql,[name])
    cursor.execute(sql,data)
    conn.commit()
    cursor.close()
    conn.close()
#6、更改数据
def updateData(conn,sql,data):
    # 获取一个光标
    cursor = conn.cursor()
    # 定义将要执行的SQL语句，例如：
    #sql = "update userinfo set pwd=%s where user=%s;"
    #cursor.execute(sql, ["july", "july"])
    cursor.execute(sql, data)
    #涉及写操作注意要提交
    conn.commit()
    # 关闭连接
    cursor.close ()
    conn.close ()
#7、查询数据
def queryData(conn,sql,data):
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 返回字典数据类型
    #定义要执行的sql
    #sql="select user,pwd from userinfo;"
    #拼接并执行sql语句
    cursor.execute(sql)
    #取到查询的结果
    ret1=cursor.fetchone()#取一条
    ret2=cursor.fetchmany(3)#取三条
    ret3=cursor.fetchone()#取一条
    cursor.close()
    conn.close()
    print(ret1)
    print(ret2)
    print(ret3)
    #可以获取指定数量的数据
    cursor.fetchmany(3)
    #光标按绝对位置移动1
    cursor.scroll(1,mode="absolute")
    #光标按照相对位置(当前位置)移动加1
    cursor.scroll(1,mode="relative")
#8、数据回滚
def rollbackData(conn):
    cursor=conn.cursor()
    #定义要执行的sql语句
    sql1="insert into userinfo(user,pwd)values(%s,%s);"
    sql2="insert into hobby(id,hobby)values(%s,%s);"
    user="july1"
    pwd="july1"
    id="我是错误的id" #id="3"
    hobby="打游戏"
    try:
        cursor.execute(sql1,[user,pwd])
        print(sql1)
        cursor.execute(sql2,[id,hobby])
        conn.commit()
    except Exception as e:
        print(str(e))
        #有异常就回滚
        conn.rollback()
    cursor.close()
    conn.close()

