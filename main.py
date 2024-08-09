import io

import psycopg

dsn = {
    'dbname': 'movies_database',
    'user': 'app',
    'password': '11eddi11',
    'host': 'localhost',
    'port': 5432,
    'options': '-c search_path=content',
}
data = 'sqlite_to_postgres/db.sqlite'