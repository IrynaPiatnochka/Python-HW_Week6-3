
import mysql.connector
from mysql.connector import Error

db_name = 'library_system'
user = 'root'
host = 'localhost'

def db_connection():
    try:
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            host=host
        )

        if conn.is_connected():
            print("Connection to MySQL database successful!")
            return conn
    except Error as e:
        print(f"Error: {e}")
        return None