import sqlite3
from PyQt5.QtSql import QSqlQuery
import os

path_to_books = r'd:\Books\FINAL'
db = 'd:/libraly.db'


def create_base():
	conn = sqlite3.connect(db)
	cur = conn.cursor()
	cur.execute("""CREATE TABLE books(
	id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
	filename VARCHAR(150) NOT NULL,
	path VARCHAR(150),
	checkread VARCHAR(5) NOT NULL
	)""")
	conn.commit()
	return conn


def read_base(base):
	conn = sqlite3.connect(base)
	return conn


def check_data():
	files, inbase = [], []
	query = QSqlQuery()
	query.exec("""SELECT filename FROM books""")
	while query.next():
		filename_in_base = query.value(0)
		inbase.append(filename_in_base)
	for book in os.listdir(path_to_books):
		filename = os.path.basename(book)
		files.append(filename)
	needs = list(set(inbase) ^ set(files))
	return needs


def add_data():
	array = []  # массив с данными (список списков (предположительно?)
	conn = read_base(db)
	cur = conn.cursor()
	cur.executemany("""
	INSERT INTO books (
	filename,
	path,
	checkread
	)
	VALUES (?, ?, ?)
	""", (array))


# Пересмотреть???
def get_data():
	data = []
	data1 = []
	data2 = []
	for book in os.listdir(path_to_books):
		filename = os.path.basename(book)
		path = os.path.join(path_to_books, book)
		data.append(filename)
		data1.append(path)
		data2.append('Non check')
		zipped_values = zip(data, data1, data2)
	zipped_list = list(zipped_values)
	return zipped_list


def main():
	if not os.path.exists(db):
		conn = create_base()
	else:
		conn = read_base(db)
	if check_data():
		add_data()
	else:
		# возможно, выводим в программу?
		print('list1=list2')
	conn.close()


if __name__ == '__main__':
	main()
