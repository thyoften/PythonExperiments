import os
import getpass
import cx_Oracle

username = input('username? ')
password = getpass.getpass('password? ')

connection = cx_Oracle.connect(
    user=username,
    password=password,
    dsn='localhost/XEPDB1')

cursor = connection.cursor()

cursor.execute("select 'hello world' from dual");

print(cursor.fetchone()[0])

cursor.close()
connection.close()


