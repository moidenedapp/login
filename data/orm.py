
import psycopg2
from psycopg2.extras import RealDictCursor
import datetime
from dotenv import load_dotenv
import os


class ORM():
    _table_name = None
    _exclude_fields = ['created_at', 'updated_at', 'update_at', 'id']

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


    @classmethod
    def _get_connection(cls):
        return psycopg2.connect(
            dbname   = os.environ.get('DB_NAME'),
            user     = os.environ.get('DB_USER'),
            password = os.environ.get('DB_PASSWORD'),
            host     = os.environ.get('DB_HOST'),
            port     = os.environ.get('DB_PORT') 
        )    
    
    
    @classmethod
    def find(cls, **kwargs):
        conn = cls._get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                where_clause = ' AND '.join([f"{key} = %s" for key in kwargs])
                query = f"SELECT * FROM {cls._table_name or cls.__name__.lower()} WHERE {where_clause}"   
                cur.execute(query, tuple(kwargs.values()))
                result = cur.fetchone()
                ins = cls(**result) if result else None
                return ins
        finally:
            conn.close()

    
    @classmethod
    def all(cls, **kwargs)-> list:
        conn = cls._get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:                
                query = f"SELECT * FROM {cls._table_name or cls.__name__.lower()}"   
                cur.execute(query, tuple(kwargs.values()))
                result = cur.fetchall()
                return [] if not result else [cls(**row) for row in result]
        finally:
            conn.close()



    def save(self):
        conn = self._get_connection()
        try:
            with conn.cursor() as cur:
               attributes = { k: v for k, v in self.__dict__.items() if k not in self._exclude_fields }
               if hasattr(self, 'id'):
                   set_clause = ", ".join([f"{key} = %s" for key in attributes if key != 'id'])
                   query = f"UPDATE {self._table_name or self.__class__.__name__.lower()} SET {set_clause} WHERE id = %s" 
                   cur.execute(query, tuple(attributes.values()) + (self.id,))
                   conn.commit()
               else:
                    columns = ", ".join(attributes.keys())
                    placeholders = ", ".join(["%s"] * len(attributes))
                    query = f"INSERT INTO {self._table_name or self.__class__.__name__.lower()} ({columns}) VALUES ({placeholders}) RETURNING id"
                    cur.execute(query, tuple(attributes.values()))
                    self.id = cur.fetchone()[0]
                    conn.commit()
        finally:
            conn.close()

        
    def delete(self):
        if not hasattr(self, 'id') or not self.id:
            raise ValueError("Cannot delete unsaved record")
        conn = self._get_connection()
        try:
            with conn.cursor() as cur:
                query = f"DELETE FROM {self._table_name or self.__class__.__name__.lower()} WHERE id = %s"
                cur.execute(query, (self.id,))
                conn.commit()
        finally:
            conn.close()

         

