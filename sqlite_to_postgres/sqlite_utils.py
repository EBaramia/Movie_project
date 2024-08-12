import sqlite3
from typing import Type, List

from config import SQLITE_DB
from dotenv import load_dotenv


load_dotenv()


# Функция для извлечения данных из SQLite
def fetch_data_from_sqlite(table_name: str, dataclass_type: Type, batch_size: int = 100) -> List:
    sqlite_db = SQLITE_DB
    data = []

    with sqlite3.connect(sqlite_db) as conn:
        cursor = conn.cursor()

        field_names = dataclass_type.sqlite_field_names()
        sqlite_columns = ', '.join(field_names.values())
        cursor.execute(f"SELECT {sqlite_columns} FROM {table_name}")

        while True:
            rows = cursor.fetchmany(batch_size)
            if not rows:
                break
            
            data.extend([
                dataclass_type(**{
                    postgres_field: row[idx] for idx, postgres_field in enumerate(field_names.keys())
                }) for row in rows
            ])
    
    return data
