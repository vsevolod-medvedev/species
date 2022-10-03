from yoyo import step

__depends__ = {'001_init'}

steps = [
    step("""
        INSERT INTO genus (id, caption) VALUES (1, 'Снегири');
        INSERT INTO genus (id, caption) VALUES (2, 'Настоящие дрозды');
    """),
    step("""
        INSERT INTO species (id, genus_id, caption) VALUES (1, 1, 'Снегирь');
        INSERT INTO species (id, genus_id, caption) VALUES (2, 2, 'Певчий дрозд');
    """),
    step("""
        INSERT INTO observation (id, species_id, timestamp, latitude, longitude) VALUES (1, 1, '2022-10-03 05:31:43.000000', 56.425724, 84.991325);
    """)
]
