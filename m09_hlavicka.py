from mysql.connector import connect, Error
from m09_sqlalchemy.connection_details import *

try:
    with connect(host=host, user=user, password=password) as conn:
        print(conn)
        with conn.cursor() as cursor:
            cursor.execute("CREATE DATABASE poker;")
        print("Databaze poker byla vytvorena")



except Error as e:
    print(e)