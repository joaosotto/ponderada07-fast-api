import psycopg2
import os 
from dotenv import load_dotenv
load_dotenv

class UserRepository():
     
    def __init__(self):
        database_url = os.getenv('DATABASE_URL')
        self.conn = psycopg2.connect(database_url)

    def GetAllUsers(self):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM user")
            users = cursor.fetchall() # retorna lista de usuários {[id: 1, nome: 'joao']}
            return users
        
    def PostUser(self, userData):

        params = {
            userData['name'],
            userData['email'],
            userData['password'], 
            userData['admin'], 
        }

        query = "INSERT INTO user (name, email, password, admin) VALUES (%s, %s, %s, %s) RETURNING id;"

        with self.conn.cursor() as cursor:
            cursor.execute(query, params) 
            response = cursor.fetchone()[0]
            self.conn.commit()  # Confirma as alterações no banco de dados
            return response 

        
    # def UpdateUser(userId, userData):

    # def DeleteUser(userId): 