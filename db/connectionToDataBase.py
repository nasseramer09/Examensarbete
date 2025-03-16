import mysql.connector
import os

class DataBaseConnection:

    @staticmethod
    def get_db_connection():
        
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user= os.getenv("DB_USER", "root"),
            password= os.getenv("DB_PASSWORD",""),
            database= os.getenv("DB_NAME", "uppdragshanteraren_db")
            )
            
        return connection


      

