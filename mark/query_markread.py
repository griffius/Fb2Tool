create_table_query = '''
                    CREATE TABLE "books" (
						"id"	INTEGER UNIQUE,
						"author"	VARCHAR,
						"title"	VARCHAR,
						"status" VARCHAR,
						"operation"	VARCHAR,
						"date_start"	VARCHAR,
						"date_finish"	VARCHAR,
						PRIMARY KEY("id" AUTOINCREMENT)
					);
                '''
add_records_query = '''
	INSERT INTO books (author, title, status, operation, date_start) VALUES (?, ?, ?, ?, ?);
'''
update_records_query = '''
	UPDATE books SET status=?, date_finish=? WHERE author=? AND title=?;
'''
check_exists_query = '''
	SELECT * FROM books WHERE author=? AND title=?;
'''
select_all_query = '''
    SELECT author, title, status, operation, date_start, date_finish FROM books;
'''
select_year_query = '''
    SELECT author, title, status, operation, date_start, date_finish FROM books WHERE date_finish LIKE ?;
'''
select_exists_year_query = '''
    SELECT date_finish FROM books;
'''



find_start_date_query = '''
SELECT date FROM books WHERE title like " + ? + " AND status like "Начал";
'''