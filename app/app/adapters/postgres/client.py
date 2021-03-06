import os
import psycopg2 as psycopg
from psycopg2.extras import RealDictCursor


class Database():
    def __init__(self):
        self.HOST = "172.21.0.1"
        self.USER = os.environ.get("POSTGRES_USER")
        self.PASSWORD = os.environ.get("POSTGRES_PASSWORD")
        self.DATABASE = os.environ.get("POSTGRES_DATABASE")
        self.PORT = os.environ.get("POSTGRES_PORT")
        self.conn = psycopg.connect("host={} dbname={} user={} password={} port={}".format(self.HOST, self.DATABASE, self.USER, self.PASSWORD, self.PORT))
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
