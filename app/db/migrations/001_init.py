from yoyo import step

__depends__ = {}


steps = [
    step("""
        drop table if exists observation;
        drop table if exists species;
        drop table if exists genus;
    """),
    step("""
        create table genus
        (
            id      serial
                primary key,
            caption varchar(255) not null
        );
    """),
    step("""
        create table species
        (
            id       serial
                primary key,
            genus_id integer      not null
                references genus,
            caption  varchar(255) not null
        );

        create index species_genus_id
            on species (genus_id);
    """),
    step("""
        create table observation
        (
            id         serial
                primary key,
            species_id integer   not null
                references species,
            timestamp  timestamp not null,
            latitude   real      not null,
            longitude  real      not null
        );

        create index observation_species_id
            on observation (species_id);
    """),
]
