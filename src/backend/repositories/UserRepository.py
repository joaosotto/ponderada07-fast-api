import psycopg2
import os
from dotenv import load_dotenv

dotenv_path = os.path.join('src', '.env')
load_dotenv(dotenv_path)

class UserRepository:
     
    def __init__(self):
        database_url = os.getenv('DATABASE_URL')
        print(database_url)
        self.conn = psycopg2.connect(database_url)  # Use self.conn to make it accessible throughout the class

    def get_all_users(self):
        """Fetches all users from the database and returns them as a list of tuples."""
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users")  # Assuming the table is named 'users'
            users = cursor.fetchall()  # Returns an array of user tuples
            return users
        
    def post_user(self, user_data):
        """Inserts a new user into the database and returns the new user's ID."""
        params = (
            user_data['name'],
            user_data['email'],
            user_data['password'],
            user_data['admin'],
        )

        query = "INSERT INTO users (name, email, password, admin) VALUES (%s, %s, %s, %s) RETURNING id;"

        with self.conn.cursor() as cursor:
            cursor.execute(query, params)
            user_id = cursor.fetchone()[0]  # Fetch the first column of the first record
            self.conn.commit() 
            return user_id

        
    # def UpdateUser(userId, userData):

    

    # def DeleteUser(userId): 