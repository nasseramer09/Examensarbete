import hashlib
import flask 
from db.connectionToDataBase import DataBaseConnection

class AuthenticationServices():

    @staticmethod
    def createAcount(firstName:str, lastName:str, userName:str , password:int, role:str):
        conn = DataBaseConnection.get_db_connection()
        cursor = conn.cursor()
        hashed_password=hashlib.sha256(password.encode()).hexdigest()
        cursor.execute(
            """
            INSERT INTO users (first_name, last_name, username, password_hash, role)
            VALUES (%s, %s, %s, %s, %s)
            """, (firstName, lastName, userName, hashed_password, role)
        )

        conn.commit()
        cursor.close()
        conn.close()
        print("User has being created successfully ")
        

    @staticmethod
    def login(userName:str, password:int):
        conn = DataBaseConnection.get_db_connection()
        cursor=conn.cursor(dictionary=True)

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        cursor.execute(
            " SELECT * FROM users WHERE username = %s AND password_hash = %s",
            (userName, hashed_password)
        )

        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user and hashlib.sha256(password.encode()).hexdigest()==user['password']:
            return {"message": "Success", "role":user['role']}
        else:
            return{"message":"Wrong username or password "}
        