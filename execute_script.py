import sqlite3
import random

class ExecuteScript:
     # Функция создает и заполняет
     def test_script(self):
       try:
         conn = sqlite3.connect('orders.db')
       except:
         print("Ошибка подключения к базе данных")

       cur = conn.cursor()

       cur.execute("""CREATE TABLE IF NOT EXISTS ships(
                      ship TEXT PRIMARY KEY,
                      weapon TEXT,
                      hull TEXT,
                      engine TEXT,
                      FOREIGN KEY (weapon) REFERENCES weapons(weapon),
                      FOREIGN KEY (hull) REFERENCES hulls(hull),
                      FOREIGN KEY (engine) REFERENCES engines(engine)
                      );
                   """)

       for i in range(1, 201):
        rnd_weapon = random.randrange(1, 21)
        rnd_engine = random.randrange(1, 7)
        rnd_hull = random.randrange(1, 6)
        ship = (f'Ship{i}', f'Weapon{rnd_weapon}', f'Hull{rnd_hull}', f'Engine{rnd_engine}')
        cur.execute("INSERT INTO ships VALUES(?, ?, ?, ?);", ship)

       cur.execute("""CREATE TABLE IF NOT EXISTS weapons(
                            weapon TEXT PRIMARY KEY,
                            reload_speed INTEGER,
                            rotational_speed INTEGER,
                            diameter INTEGER,
                            power_volley INTEGER,
                            count INTEGER);
                        """)

       for i in range(1, 21):
           reload_speed = random.randrange(1, 21)
           rotational_speed = random.randrange(1, 21)
           diameter = random.randrange(1, 21)
           power_volley = random.randrange(1, 21)
           count = random.randrange(1, 21)
           weapon = (f'Weapon{i}', reload_speed, rotational_speed, diameter, power_volley, count)
           cur.execute("INSERT INTO weapons VALUES(?, ?, ?, ?, ?, ?);", weapon)
           conn.commit()

       cur.execute("""CREATE TABLE IF NOT EXISTS hulls(
                      hull TEXT PRIMARY KEY,
                      armor INTEGER,
                      type INTEGER,
                      capacity INTEGER);
                   """)

       for i in range(1, 6):
        armor = random.randrange(1, 21)
        type = random.randrange(1, 21)
        capacity = random.randrange(1, 21)
        hull = (f'Hull{i}', armor, type, capacity)
        cur.execute("INSERT INTO hulls VALUES(?, ?, ?, ?);", hull)
        conn.commit()

       cur.execute("""CREATE TABLE IF NOT EXISTS engines(
                      engine TEXT PRIMARY KEY,
                      power INTEGER,
                      type INTEGER);
                   """)

       for i in range(1, 7):
        power = random.randrange(1, 21)
        type = random.randrange(1, 21)
        engine = (f'Engine{i}', power, type)
        cur.execute("INSERT INTO engines VALUES(?, ?, ?);", engine)
        conn.commit()

       return cur

