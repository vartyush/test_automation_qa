import pytest
import pytest_check as check

components = [("weapon"),
             ("hull"),
             ("engine")]

@pytest.mark.parametrize('component', components)
def test_ships(origin_db, new_db, component):
        print("Тест начался")
        origin_db_component = origin_db.execute(f"SELECT ship, {component} FROM ships;")
        new_db_component = new_db.execute(f"SELECT ship, {component} FROM ships;")
        if component == "weapon":
            sql_select = "SELECT ships.ship, ships.weapon, weapons.diameter, weapons.count," \
                         " weapons.power_volley, weapons.reload_speed,"\
                                                  " weapons.rotational_speed FROM ships  JOIN weapons "\
                                                  "ON ships.weapon = weapons.weapon;"
        elif component == "engine":
            sql_select = "SELECT ships.ship, engines.engine, engines.power, engines.type, engines.type" \
                         " FROM ships JOIN engines ON ships.engine = engines.engine;"
        else:
            sql_select = "SELECT ships.ship, hulls.hull, hulls.armor, hulls.type," \
                                                  " hulls.capacity  FROM ships  JOIN hulls ON ships.hull = hulls.hull;"
        origin_db_state_param = origin_db.execute(sql_select)
        new_db_state_param = new_db.execute(sql_select)
        origin_db_component_read = origin_db_component.fetchall()
        new_db_state_component_read = new_db_component.fetchall()
        origin_db_state_param_read = origin_db_state_param.fetchall()
        new_db_state_param_read = new_db_state_param.fetchall()
        for i in range(0, 201):
            check.equal(origin_db_component_read[i], new_db_state_component_read[i])
            check.equal(origin_db_state_param_read[i], new_db_state_param_read[i])

