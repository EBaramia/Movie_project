import logging
from sqlite_utils import fetch_data_from_sqlite
from postgres_utils import save_data_to_postgres
from models import FilmWork, Person, Genre, PersonFilmWork, GenreFilmWork


def migrate_all_tables():
    tables_classes = {
        "film_work": FilmWork,
        "person": Person,
        "genre": Genre,
        "person_film_work": PersonFilmWork,
        "genre_film_work": GenreFilmWork
    }

    for table_name, table_class in tables_classes.items():
        logging.info(f"Fetching data from {table_name}...")
        data = fetch_data_from_sqlite(table_name, table_class)
        logging.info(f"Saving data to {table_name}..")
        save_data_to_postgres(data, table_name)


if __name__ == '__main__':
    migrate_all_tables()