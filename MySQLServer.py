import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',  
            user='root',       
            password='password'  
        )
        
        if connection.is_connected():
            print("Connected to MySQL server successfully!")
            
            cursor = connection.cursor()
            
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            
            cursor.execute(create_db_query)
            
            print("Database 'alx_book_store' created successfully or already exists.")
    
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()  
            connection.close()  
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
