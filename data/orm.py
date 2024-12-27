import psycopg2
from psycopg2.extras import RealDictCursor
import datetime

class ORM():
    _table_name = None
    _excluded_fields = ['created_at', 'updated_at']

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def _get_connection(cls, self):
        return psycopg2.connect(
            dbname   = 'postgres',  
            user     = 'postgres',    
            password = 'hgyjump15',
            host     = 'localhost',
            port     = '5432'
     )
            


    @classmethod   
    def find (cls, **kwargs):
        conn = cls._get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                where_clause = 'AND' .join([f"{key} = %s" for key in kwargs()])
                query = f"SELECT * FROM {cls._table_name or cls.__name__.lower} WHERE {where_clause}"
                cur.execute(query, tuple(kwargs.values()))
                return cur.fetchone()
                ins = cls(**result) if result else None
                return ins
        finally:
            conn.close()


    def save(self):
        conn = self._get_connection()
        try:
            with conn.cursor() as cur:
              attributes = { k: v for k, v in self.__dict__.items() if not k.startswith('_') }
              if hasattr(self, 'id'):
                  set_clause = ", ".join([f"{key} = %s" for key in attributes if key != 'id'])
                  query = f"UPDATE {self._table_name or self.__class__.__name__.lower()} SET {set_clause} WHERE id = %s"
                  cur.execute(query, tuple(attributes.values()) + (self.id,))

                  print(query)
                  print(tuple(attributes.values()) + (self.id,))

                  cur.execute(query, tuple(attributes.values()) + (self.id,))
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
            raise ValueError("Can't delete unsaved record")
        conn = self._get_connection()
        try:
            with conn.cursor() as cur:
                query = f"DELETE FROM {self._table_name or self.__class__.__name__.lower()} WHERE id = %s"
                cur.execute(query, (self.id,))
                conn.commit()
        finally:
            conn.close()


