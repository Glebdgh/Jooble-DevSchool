import json
import re
from math import cos as c
      
# in case if facing issues with pip: curl https://bootstrap.pypa.io/get-pip.py | python3
import mysql.connector  # pip3 install mysql-connector-python
import requests  
      
import time
import sys
try:
        r = requests.post('http://graph.facebook.com/')
        print("Returning a kind of token as a result of a Facebook API test call " + r.json()['error']['fbtrace_id'])
except:
        print(
            "well ok something happened with your internet connection ")
      
      
try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="user1!",
            database="hvv",
            auth_plugin="mysql_native_password"
        )
      
        mycursor = db.cursor()
        sqlBuff =  "INSERT INTO Disney(id,birth,name,species,role,sex) VALUES('10', '1','Robin Hood','cartoon','main','man')"
        mycursor.execute(sqlBuff)
        db.commit()
        mycursor.execute("select * from Disney")
        for i in mycursor:
            print(i)

        sqlBuf =  "DELETE FROM Disney WHERE id = 10"
        mycursor.execute(sqlBuf)
        db.commit()
        mycursor.execute("select * from Disney")
        for x in mycursor:
            print(x)

        sqlBu =  "UPDATE Disney SET role = 'not main' where id = 7"
        mycursor.execute(sqlBu)
        db.commit()
        mycursor.execute("select * from Disney")
        for z in mycursor:
            print(z)
        db.close()
except:
        print("something went wrong")
      
