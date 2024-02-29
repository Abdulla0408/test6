import psycopg2
class DataBase:
    def __init__(self):
        self.database = psycopg2.connect(
            database='kun_uz',
            user='postgres',
            password='1',
            host='localhost'
        )

    def manager(self, sql, *args,
                fetchone:bool=False,
                fetchall:bool=False,
                fetchmany:bool=False,
                commit:bool=False):
        with self.database as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    result = db.commit()
                elif fetchone:
                    result = cursor.fetchone()
                elif fetchall:
                    result = cursor.fetchall()
                elif fetchmany:
                    result = cursor.fetchmany()
            return result
    def create_table_categories(self):
        sql = '''CREATE TABLE IF NOT EXISTS categories(
            categorie_id INTEGER GENERATED ALWAYS AS IDNETITY PRIMARY KEY,
        )'''
        self.manager(sql, commit = True)

    def create_table_articles(self):
        sql = '''CREATE TABLE IF NOT EXISTS articles(
            articel_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            article_name VARCHAR,
            content TEXT,
            created TIMESTAMP DEFAULT NOW(),
            views INTEGER
        )'''
        self.manager(self, sql)