import asyncio
from pgsql import create_pg as pg_c
from pgsql import read_pg as pg_r
from pgsql import insert_pg as pg_i

async def main():
    print(await pg_r.pizzerias())
    print(await pg_i.ins_pizzeria('Докер пицца'))
    print(await pg_r.pizzerias())

    #Создание 2-х таблиц: Матери - Дети
    #связанных первичным и внешним ключом на postgresql
    #(связь один ко многим)
    table = "mothers"
    columns = {
        "id": {"type": "int", "autoinc": True, "nn": True, "pk": True}, #, "fk": "mothers"},
        "fio": {"type": "str", "nn": True},
        "bd": {"type": "date", "nn": True}
    }
    print(await pg_c.create_tbl(table, columns, "public"),  f"{table} table created")

    table = "childs"
    columns = {
        "id": {"type": "int", "autoinc": True, "nn": True, "pk": True},
        "age": {"type": "int", "nn": True},
        "fio": {"type": "str", "nn": True},
        "bd": {"type": "date", "nn": True},
        "height": {"type": "int", "nn": False},
        "weight": {"type": "int", "nn": False},
        "idMother": {"type": "int", "nn": True, "fk": "mothers"}
    }
    print(await pg_c.create_tbl(table, columns, "public"), f"{table} table created")

asyncio.run(main())