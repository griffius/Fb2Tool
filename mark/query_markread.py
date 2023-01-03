create_table_query = '''
                    CREATE TABLE "books" (
						"id"	INTEGER UNIQUE,
						"author"	VARCHAR,
						"title"	VARCHAR,
						"status"	VARCHAR,
						"operation"	VARCHAR(40),
						"date"	VARCHAR(10),
						PRIMARY KEY("id" AUTOINCREMENT)
					);
                '''
add_records_query = '''
	INSERT INTO books (author, title, status, operation, date) VALUES(?, ?, ?, ?, ?);
'''
select_all_query = '''
    SELECT author, title, status, operation, date FROM books;
'''

find_start_date_query = '''
SELECT date FROM books WHERE title like " + ? + " AND status like "Начал";
'''