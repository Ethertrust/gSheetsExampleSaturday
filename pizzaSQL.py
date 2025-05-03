import asyncio
from pgsql import read_pg as pg_r
from pgsql import insert_pg as pg_i

async def main():
    print(await pg_r.pizzerias())
    print(await pg_i.ins_pizzeria('Докер пицца'))
    print(await pg_r.pizzerias())

asyncio.run(main())