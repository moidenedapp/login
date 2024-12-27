import psycopg2

from .models import User, Permission


class DBException(Exception):
    pass


class DB():
    db_params = None
    connection = None

    def __init__(self, db_params):
        self.db_params = db_params


    def connect(self):
        self.connection = psycopg2.connect(**self.db_params)
        return self
    

    def tuple_to_user(self, data):
        user = User()
        user.id = data[0]
        user.name = data[1]
        user.lastname = data[2]
        user.email = data[3]
        user.password = data[4]
        user.role = data[5]
        user.created_at = data[6]
        user.updated_at = data[7]
        return user
        

    def get_user(self, id):
        query = "SELECT id, name, lastname, email, password, role_id, created_at, update_at FROM users WHERE id = %s"
        cursor = self.connection.cursor()
        cursor.execute(query, (str(id)))
        result = cursor.fetchone()
        if not result:
            raise DBException("User not found")
        self.connection.close()
        return self.tuple_to_user(result)      
    

    def get_user_by_email(self, email):
        query = "SELECT  id, name, lastname, email, password, role_id, created_at, update_at FROM users WHERE email = %s"
        cursor = self.connection.cursor()
        cursor.execute(query, (email, ))
        result = cursor.fetchone()
        if not result:
            raise DBException("User not found")
        self.connection.close()
        return self.tuple_to_user(result)      


    def get_users(self):
        query = "SELECT  id, name, lastname, email, password, role_id, created_at, update_at FROM users"
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        if not result:
            raise DBException("User not found")
        self.connection.close()
        return [self.tuple_to_user(row) for row in result]      


