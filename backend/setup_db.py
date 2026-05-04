from sqlalchemy import create_engine, text
import os

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql://postgres:Vedant%401612200@db.xjxrphpkvzgxmzcwezmb.supabase.co:5432/postgres",
)

engine = create_engine(DATABASE_URL)
with engine.connect() as conn:
    conn.execute(text("CREATE SCHEMA IF NOT EXISTS analytics"))
    conn.execute(text("CREATE SCHEMA IF NOT EXISTS identity"))
    conn.commit()
    print("Schemas created!")
