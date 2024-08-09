import psycopg
from dataclasses import fields
from typing import List

import psycopg.rows

from config import POSTGRES_DB


# Функция для записи данных в postgres
def save_data_to_postgres(data: List, table_name: str):

    # Подключаемся к postgres
    dsn = POSTGRES_DB

    with psycopg.connect(**dsn, row_factory=psycopg.rows.dict_row, cursor_factory=psycopg.ClientCursor) as conn:
        with conn.cursor() as cursor:
            
            # Очищаем таблицу перед миграцией
            cursor.execute(f"TRUNCATE {table_name} CASCADE")

            if data:
                colum_names = [field.name for field in fields(data[0])]
                colum_names_str = ', '.join(colum_names)
                col_count = ', '.join(['%s'] * len(colum_names))

                if table_name == 'person_film_work':
                    conflict_columns = 'person_id, film_work_id'
                else:
                    conflict_columns = 'id'  

                insert_query = f"""
                INSERT INTO {table_name} ({colum_names_str})
                VALUES ({col_count})
                ON CONFLICT ({conflict_columns}) DO NOTHING
                """

                data_to_insert = [tuple(getattr(item, field.name) for field in fields(data[0])) for item in data]

                cursor.executemany(insert_query, data_to_insert)
        
        conn.commit()
