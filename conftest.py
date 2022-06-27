import pytest
import sqlite3
import random

from execute_script import ExecuteScript
# Создаем фикстуру для создания первой БД
@pytest.fixture(scope='session')
def origin_db():
    q = ExecuteScript()
    current_state = q.test_script()
    return current_state

# Создаем фикстуру для создания второй БД на основе первой
@pytest.fixture(scope='session')
def new_db(origin_db):
    origin_db.execute("SELECT * FROM ships;")
    ships_table_new = origin_db.fetchall()
    origin_db.execute("SELECT * FROM engines;")
    engines_table_new = origin_db.fetchall()
    origin_db.execute("SELECT * FROM hulls;")
    hulls_table_new = origin_db.fetchall()
    origin_db.execute("SELECT * FROM weapons;")
    weapons_table_new = origin_db.fetchall()
    try:
        new_db = sqlite3.connect('orders1.db')
    except:
        print("Ошибка подключения к базе данных")
    # print(read)
    cur = new_db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS ships(
                          ship TEXT PRIMARY KEY,
                          weapon TEXT,
                          hull TEXT,
                          engine TEXT);
                       """)
    cur.executemany("INSERT INTO ships VALUES(?, ?, ?, ?);", ships_table_new)
    new_db.commit()
    cur.execute("""CREATE TABLE IF NOT EXISTS weapons(
                          weapon TEXT PRIMARY KEY,
                          reload_speed INTEGER,
                          rotational_speed INTEGER,
                          diameter INTEGER,
                          power_volley INTEGER,
                          count INTEGER);
                      """)
    cur.executemany("INSERT INTO weapons VALUES(?, ?, ?, ?, ?, ?);", weapons_table_new)
    new_db.commit()
    cur.execute("""CREATE TABLE IF NOT EXISTS hulls(
                         hull TEXT PRIMARY KEY,
                         armor INTEGER,
                         type INTEGER,
                         capacity INTEGER);
                      """)
    cur.executemany("INSERT INTO hulls VALUES(?, ?, ?, ?);", hulls_table_new)
    new_db.commit()
    cur.execute("""CREATE TABLE IF NOT EXISTS engines(
                          engine TEXT PRIMARY KEY,
                          power INTEGER,
                          type INTEGER);
                       """)
    cur.executemany("INSERT INTO engines VALUES(?, ?, ?);", engines_table_new)
    new_db.commit()
    for row in ships_table_new:
        random_value = random.randrange(1, 4)
        rnd_weapon = random.randrange(1, 21)
        rnd_engine = random.randrange(1, 7)
        rnd_hull = random.randrange(1, 6)
        ship_column = ('ship', 'weapon', 'hull', 'engine')
        ship_value = ('Ship', f'Weapon{rnd_weapon}', f'Hull{rnd_hull}', f'Engine{rnd_engine}')
        random_component= (ship_column[random_value])
        random_ship_value = ship_value[random_value]
        ship = row[0]
        cur.execute(f'''UPDATE ships SET {random_component} = '{random_ship_value}' WHERE ship = ? ''', (ship,))
        new_db.commit()
    for row in engines_table_new:
        random_value = random.randrange(1, 3)
        random_change = random.randrange(1, 21)
        engine_column = ('engine', 'power', 'type')
        random_component = (engine_column[random_value])
        engine = row[0]
        cur.execute(f'''UPDATE engines SET {random_component} = {random_change} WHERE engine = ? ''', (engine,))
        new_db.commit()
    for row in hulls_table_new:
        random_value = random.randrange(1, 4)
        random_change = random.randrange(1, 21)
        hull_column = ('hull', 'armor', 'type', 'capacity')
        random_component = (hull_column[random_value])
        hull = row[0]
        cur.execute(f'''UPDATE hulls SET {random_component} = {random_change} WHERE hull = ? ''',
                        (hull,))
        new_db.commit()
    for row in weapons_table_new:
        random_value = random.randrange(1, 6)
        random_change = random.randrange(1, 21)
        weapon_column = ('weapon', 'reload_speed', 'rotational_speed', 'diameter', 'power_volley', 'count')
        random_component = (weapon_column[random_value])
        weapon = row[0]
        cur.execute(f'''UPDATE weapons SET {random_component} = {random_change} WHERE weapon = ? ''',
                    (weapon,))
        new_db.commit()
    return cur
