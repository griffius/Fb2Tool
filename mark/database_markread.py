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

def check_exists(conn, query, value):
	cur = conn.cursor()
	info = cur.execute(query, value).fetchone()
	if info is None:
		return False
	else:
		return True

def get_all_data(conn, query, value=None):
	cur = conn.cursor()
	if value:
		info = cur.execute(query, [value])
	else:
		info = cur.execute(query)
	return info

def get_exists_year(conn, query):
	cur = conn.cursor()
	info = cur.execute(query)
	return info