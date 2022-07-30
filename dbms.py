from pymysql import *
from flask import Flask,request,redirect,render_template,session
#both database connection

def connect_shop(database_name):
    return connect(host='localhost',port=3306,user='root',database='{}'.format(database_name))
    
#database 1 shopping for both

def insertTable1(database_name,table_name,type_name,type_pass,type_add, name, password, address):
    c=connect_shop(database_name)
    query="insert into {} ({},{},{}) values ('{}','{}','{}');".format( table_name, type_name, type_pass, type_add, name, password, address) 
    marker=c.cursor()
    marker.execute(query)
    c.commit()
    c.close()

#database 2 shops for shops

def insertTable2(database_name,shop_name,item_name,item_price,item_quantity):
    c=connect_shop(database_name)
    query="insert into {} (item_name,item_price,item_quantity) values ('{}',{},{});".format(shop_name,item_name,item_price,item_quantity) 
    marker=c.cursor()
    marker.execute(query)
    c.commit()
    c.close()

#database 2 shops for shops

def createTable(database_name,shop_name):
    c=connect_shop(database_name)
    query="create table {} (id int primary key auto_increment, item_name varchar(20) , item_price int , item_quantity int ) auto_increment=1;".format(shop_name)
    marker=c.cursor()
    marker.execute(query)
    c.commit()
    c.close()

#database 2 shops for both

def updateTable(database_name,shop_name,new_count,item_name): 
    c=connect_shop(database_name)
    query="update {} set item_quantity = {} where item_name = '{}' ;".format(shop_name,new_count,item_name)
    marker=c.cursor()
    marker.execute(query)
    c.commit()
    c.close()

#database 2 shops for consumer

def searchTable(database_name,item):
    shops=[]
    items=[]
    c=connect_shop(database_name)
    query="show tables;"
    marker=c.cursor()
    marker.execute(query)
    shop_name = marker.fetchall()
    for i in shop_name:
        query1="select * from {} where item_name='{}' ;".format(i[0],item)
        marker.execute(query1)
        item_name = marker.fetchall()
        if item_name:
            shops.append(i[0])
            for i in item_name:    
                items.append(i)
    c.commit()
    c.close()
    return shops,items

#database 2 shops for shops

def showTable(database_name,shop_name):
    c=connect_shop(database_name)
    query="select * from {};".format(shop_name)
    marker=c.cursor()
    marker.execute(query)
    showresult=marker.fetchall()
    c.commit()
    c.close()
    return showresult

