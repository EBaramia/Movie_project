CREATE SCHEMA content;


-- Creating tables

CREATE TABLE IF NOT EXISTS content.film_work (
    id uuid PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    creation_date DATE,
    rating FLOAT check(rating >= 0 and rating <=100),
    type TEXT not null,
    created timestamp with time zone,
    modified timestamp with time zone
);

create table if not exists content.person (
    id uuid PRIMARY KEY,
    full_name varchar(255) not null,
    created timestamp with time zone,
    modified timestamp with time zone
);

create table if not exists content.person_film_work (
    id uuid PRIMARY KEY,
    person_id uuid,
    film_work_id uuid,
    role varchar(125),
    created timestamp with time zone,

    foreign key (person_id) references content.person(id),
    foreign key (film_work_id) references content.film_work(id),

    constraint unique_person_film_role unique (film_work_id, person_id, role)
);

create table if not exists content.genre (
    id uuid PRIMARY KEY,
    name varchar(225) not null,
    description text,
    created timestamp with time zone,
    modified timestamp with time zone
);

create table if not exists content.genre_film_work (
    id uuid PRIMARY KEY,
    genre_id uuid,
    film_work_id uuid,
    created timestamp with time zone,

    foreign key (genre_id) references content.genre(id),
    foreign key (film_work_id) references content.film_work(id),

    constraint unique_film_work_genre unique (film_work_id, genre_id)
);


-- Creating indexes

CREATE INDEX film_work_creation_date_idx ON content.film_work(creation_date);
CREATE UNIQUE INDEX film_work_person_idx ON content.person_film_work (film_work_id, person_id);