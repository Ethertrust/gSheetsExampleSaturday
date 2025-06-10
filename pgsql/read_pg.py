import asyncio
import asyncpg
import pandas as pd
from decouple import config

async def read_psql(text:str):
    conn = await asyncpg.connect(
        user=config("user_pg"),
        password=config("password_pg"),
        database=config("database_pg"),
        host=config("host_pg"),
        port=config("port_pg")
    )

    rows = await conn.fetch(text)
    dt_rows = pd.DataFrame(rows)
    # for row in rows:
    #     print(row)
    await conn.close()
    return dt_rows

async def pizzerias():
     df = await read_psql("SELECT * FROM pizzeria")
     return df