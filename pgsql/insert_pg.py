import asyncio
import asyncpg
import pandas as pd
from decouple import config

async def insert_psql(text:str):
    conn = await asyncpg.connect(
        user=config("user_pg"),
        password=config("password_pg"),
        database=config("database_pg"),
        host=config("host_pg"),
        port=config("port_pg")
    )

    rows = await conn.fetch(text)
    # dt_rows = pd.DataFrame(rows)
    # for row in rows:
    #     print(row)
    await conn.close()
    return rows

async def ins_pizzeria(pizzeria_name):
    df = await insert_psql(f"insert into pizzeria values (default ,'{pizzeria_name}', 5.0)")
    return df