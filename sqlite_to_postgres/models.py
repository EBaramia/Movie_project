from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Optional
import uuid


@dataclass
class FilmWork:
    title: str
    type: str
    description: Optional[str] = None
    creation_date: Optional[date] = None
    rating: float = field(default=0.0)
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    created: datetime = field(default_factory=datetime.now)
    modified: datetime = field(default_factory=datetime.now)

    @classmethod
    def sqlite_field_names(cls):
        return {
            'id': 'id',
            'title': 'title',
            'description': 'description',
            'creation_date': 'creation_date',
            'rating': 'rating',
            'type': 'type',
            'created': 'created_at',  # SQLite поле
            'modified': 'updated_at',  # SQLite поле
        }


@dataclass
class Person:
    full_name: str
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    created: datetime = field(default_factory=datetime.now)
    modified: datetime = field(default_factory=datetime.now)

    @classmethod
    def sqlite_field_names(cls):
        return {
            'id': 'id',
            'full_name': 'full_name',
            'created': 'created_at',
            'modified': 'updated_at',
        }


@dataclass
class Genre:
    name: str
    description: Optional[str] = None
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    created: datetime = field(default_factory=datetime.now)
    modified: datetime = field(default_factory=datetime.now)

    @classmethod
    def sqlite_field_names(cls):
        return {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'created': 'created_at',
            'modified': 'updated_at',
        }


@dataclass
class PersonFilmWork:
    person_id: uuid.UUID
    film_work_id: uuid.UUID
    role: Optional[str] = None
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    created: datetime = field(default_factory=datetime.now)

    @classmethod
    def sqlite_field_names(cls):
        return {
            'id': 'id',
            'person_id': 'person_id',
            'film_work_id': 'film_work_id',
            'role': 'role',
            'created': 'created_at',
        }


@dataclass
class GenreFilmWork:
    genre_id: uuid.UUID
    film_work_id: uuid.UUID
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    created: datetime = field(default_factory=datetime.now)

    @classmethod
    def sqlite_field_names(cls):
        return {
            'id': 'id',
            'genre_id': 'genre_id',
            'film_work_id': 'film_work_id',
            'created': 'created_at',
        }