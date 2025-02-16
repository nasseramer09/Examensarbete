import mysql.connector
class DataBaseConnection:

    @staticmethod
    def get_db_connection():
        
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="uppdragshanteraren_db")
            
        return connection


      

