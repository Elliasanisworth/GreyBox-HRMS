import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_mysql_connection():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE")
        )
        if conn.is_connected():
            return conn
    except mysql.connector.Error as e:
        print(f"🚨 MySQL Connection Error: {e}")
        return None

# A helper to run queries and return results as a list of dictionaries
def query_history(sql_query):
    conn = get_mysql_connection()
    if not conn:
        return []
    
    cursor = conn.cursor(dictionary=True) # returns data as {'column': value}
    cursor.execute(sql_query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result