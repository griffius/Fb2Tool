import sqlite3 as sq
from .config_mark import config_path
import os
from .query_markread import create_table_query

def init_database():
	if not os.path.exists(os.path.join(config_path, 'status.db')):
		create_base_and_table()
	conn = sq.connect(os.path.join(config_path, 'status.db'))
	return conn

def create_base_and_table():
	conn = sq.connect(os.path.join(config_path, 'status.db'))
	cur = conn.cursor()
	cur.execute(create_table_query)
	conn.commit()

def add_records(conn, query, values):
	cur = conn.cursor()
	cur.executemany(query, values)
	conn.commit()
